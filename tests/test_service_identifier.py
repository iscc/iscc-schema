# -*- coding: utf-8 -*-
import json
import pathlib

import pytest
from pydantic import ValidationError

import iscc_schema as iss
from iscc_schema import Identifier

ROOT = pathlib.Path(__file__).parent.parent
TOKEN_PATTERN = "^[a-z0-9]+([._-][a-z0-9]+)*$"


def _load_schema(name):
    # type: (str) -> dict
    return json.loads((ROOT / "docs" / "schema" / name).read_text(encoding="utf-8"))


def _contains_key(data, key):
    # type: (object, str) -> bool
    if isinstance(data, dict):
        return key in data or any(_contains_key(value, key) for value in data.values())
    if isinstance(data, list):
        return any(_contains_key(item, key) for item in data)
    return False


def _has_error(errors, type_, input_):
    # type: (list[dict], str, object) -> bool
    return any(error["type"] == type_ and error.get("input") == input_ for error in errors)


def test_iscc_meta_identifier_legacy_forms_still_validate():
    assert iss.IsccMeta(identifier="urn:isbn:3-8273-7019-1").identifier == "urn:isbn:3-8273-7019-1"
    meta = iss.IsccMeta(identifier=["urn:isbn:3-8273-7019-1", "https://doi.org/10.1234/x"])
    assert meta.identifier == ["urn:isbn:3-8273-7019-1", "https://doi.org/10.1234/x"]


def test_iscc_meta_identifier_accepts_single_object():
    meta = iss.IsccMeta(
        identifier={
            "scheme": "doi",
            "code": "10.1234/example.2024.001",
            "scope": "work",
            "primary": True,
        }
    )
    assert meta.identifier.scheme == "doi"
    assert meta.identifier.code == "10.1234/example.2024.001"
    assert meta.identifier.scope == "work"
    assert meta.identifier.primary is True
    assert meta.dict()["identifier"]["primary"] is True


def test_iscc_meta_identifier_accepts_mixed_list():
    meta = iss.IsccMeta(
        identifier=[
            "urn:isbn:3-8273-7019-1",
            {"scheme": "isrc", "code": "USRC17607839", "scope": "manifestation"},
        ]
    )
    assert meta.identifier[0] == "urn:isbn:3-8273-7019-1"
    assert meta.identifier[1].scheme == "isrc"
    assert meta.dict()["identifier"][1]["scope"] == "manifestation"


def test_identifier_rejects_non_empty_malformed_objects():
    with pytest.raises(ValidationError):
        iss.IsccMeta(identifier={"scheme": "doi"})
    with pytest.raises(ValidationError):
        iss.IsccMeta(identifier={"scheme": "DOI", "code": "10.1234/x"})
    with pytest.raises(ValidationError):
        iss.IsccMeta(identifier={"scheme": " doi ", "code": "10.1234/x"})
    with pytest.raises(ValidationError):
        iss.IsccMeta(identifier={"scheme": "doi!", "code": "10.1234/x"})
    with pytest.raises(ValidationError):
        iss.IsccMeta(identifier={"scheme": "doi", "code": "10.1234/x", "scope": "Work"})
    with pytest.raises(ValidationError):
        iss.IsccMeta(identifier={"scheme": "doi", "code": ""})


def test_identifier_empty_values_follow_global_coercion_policy():
    assert iss.IsccMeta(identifier={}).identifier is None
    assert iss.IsccMeta(identifier="").identifier is None

    meta = iss.IsccMeta(identifier={"scheme": "doi", "code": "10.1234/x", "scope": ""})
    assert meta.identifier.scope is None
    assert "scope" not in meta.dict()["identifier"]

    with pytest.raises(ValidationError):
        iss.IsccMeta(identifier=[{}])
    with pytest.raises(ValidationError) as exc_info:
        iss.IsccMeta(identifier=[""])
    assert _has_error(exc_info.value.errors(), "string_too_short", "")
    with pytest.raises(ValidationError) as exc_info:
        iss.IsccMeta(identifier=["", {"scheme": "doi", "code": "10.1234/x"}])
    assert _has_error(exc_info.value.errors(), "string_too_short", "")


def test_primary_true_round_trips_and_false_normalizes_to_absent():
    with_primary = iss.IsccMeta(identifier={"scheme": "doi", "code": "10.1234/x", "primary": True})
    assert with_primary.dict()["identifier"]["primary"] is True
    assert b'"primary":true' in with_primary.jcs()

    omitted = iss.IsccMeta(identifier={"scheme": "doi", "code": "10.1234/x"})
    false_value = iss.IsccMeta(identifier={"scheme": "doi", "code": "10.1234/x", "primary": False})
    assert false_value.identifier.primary is None
    assert "primary" not in false_value.dict()["identifier"]
    assert false_value.jcs() == omitted.jcs()


def test_nested_identifier_has_no_jsonld_wrapper_or_default_leaks():
    meta = iss.IsccMeta(identifier={"scheme": "doi", "code": "10.1234/x"})
    data = json.loads(meta.jcs())
    identifier = data["identifier"]
    assert identifier == {"code": "10.1234/x", "scheme": "doi"}
    assert "@context" not in identifier
    assert "@type" not in identifier
    assert "$schema" not in identifier
    assert "primary" not in identifier


def test_exported_identifier_model_is_bare_item_shape():
    obj = Identifier(scheme="doi", code="10.1234/example.2024.001", scope="work")

    data = obj.dict(exclude_unset=False)
    assert data["scheme"] == "doi"
    assert data["scope"] == "work"
    assert "@context" not in data
    assert "@type" not in data
    assert "$schema" not in data

    compact = obj.json(ld=False)
    assert '"scheme":"doi"' in compact
    assert '"$schema"' not in compact
    assert '"@context"' not in compact
    assert '"@type"' not in compact


def test_exported_identifier_primary_false_normalizes_to_absent():
    omitted = Identifier(scheme="doi", code="10.1234/x")
    false_value = Identifier(scheme="doi", code="10.1234/x", primary=False)
    assert false_value.primary is None
    assert "primary" not in false_value.dict()
    assert false_value.jcs() == omitted.jcs()


def _brick_shape(schema):
    # type: (dict) -> dict
    props = schema["properties"]
    return {
        "additionalProperties": schema.get("additionalProperties"),
        "required": sorted(
            name for name in schema.get("required", []) if name in {"scheme", "code"}
        ),
        "properties": {
            name: {
                key: props[name][key]
                for key in ("type", "minLength", "pattern", "const")
                if key in props[name]
            }
            for name in ("scheme", "code", "scope", "primary")
        },
    }


def test_identifier_brick_validation_shape_is_copied_without_drift():
    iscc = _load_schema("iscc.json")
    identifiers = _load_schema("identifiers.json")

    iscc_identifier = iscc["properties"]["identifier"]
    iscc_object = next(item for item in iscc_identifier["oneOf"] if item.get("type") == "object")
    iscc_array_object = next(
        item
        for item in next(item for item in iscc_identifier["oneOf"] if item.get("type") == "array")[
            "items"
        ]["oneOf"]
        if item.get("type") == "object"
    )
    identifiers_item = identifiers["properties"]["identifier"]["items"]

    expected = _brick_shape(identifiers_item)
    assert _brick_shape(iscc_object) == expected
    assert _brick_shape(iscc_array_object) == expected
    assert expected["additionalProperties"] is True
    assert expected["required"] == ["code", "scheme"]


def test_iscc_json_has_no_unresolved_refs():
    schema = _load_schema("iscc.json")
    assert not _contains_key(schema, "$ref")


def test_identifier_context_terms_match_model_fields():
    schema = _load_schema("identifiers.json")
    iscc = _load_schema("iscc.json")
    ctx = schema["@context"]
    assert "Identifier" not in ctx
    assert ctx["Identifiers"] == "http://purl.org/iscc/terms/#Identifiers"
    assert ctx["scheme"] == "http://schema.org/propertyID"
    assert ctx["code"] == "http://schema.org/value"
    assert ctx["scope"] == "http://purl.org/iscc/terms/#scope"
    assert ctx["primary"] == "http://purl.org/iscc/terms/#primary"
    item = schema["properties"]["identifier"]["items"]
    assert set(("scheme", "code", "scope", "primary")).issubset(item["properties"])
    assert item["properties"]["scheme"]["pattern"] == TOKEN_PATTERN
    assert item["properties"]["scope"]["pattern"] == TOKEN_PATTERN

    identifier = iscc["properties"]["identifier"]
    string_branch = next(item for item in identifier["oneOf"] if item.get("type") == "string")
    array_branch = next(item for item in identifier["oneOf"] if item.get("type") == "array")
    array_string_branch = next(
        item for item in array_branch["items"]["oneOf"] if item.get("type") == "string"
    )
    assert string_branch["minLength"] == 1
    assert array_string_branch["minLength"] == 1
