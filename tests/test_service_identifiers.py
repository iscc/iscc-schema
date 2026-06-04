# -*- coding: utf-8 -*-
import json
import pathlib

import pytest
from pydantic import ValidationError

import iscc_schema as iss
from iscc_schema import Identifiers

ROOT = pathlib.Path(__file__).parent.parent
CONTEXT_URL = f"http://purl.org/iscc/context/{iss.__version__}.jsonld"
SCHEMA_URL = f"http://purl.org/iscc/schema/identifiers-{iss.__version__}.json"

VALID_DATA = {
    "iscc": "ISCC:MAACAJINXFXA2SQX",
    "identifier": [
        {"scheme": "iswc", "code": "T-034.524.680-1", "scope": "work", "primary": True},
        {"scheme": "isrc", "code": "USRC17607839", "scope": "manifestation"},
    ],
}


def _load_schema(name):
    # type: (str) -> dict
    return json.loads((ROOT / "docs" / "schema" / name).read_text(encoding="utf-8"))


def test_valid_identifiers_record():
    obj = Identifiers(**VALID_DATA)
    assert obj.iscc == "ISCC:MAACAJINXFXA2SQX"
    assert obj.identifier[0].scheme == "iswc"
    assert obj.identifier[0].primary is True
    assert obj.identifier[1].scope == "manifestation"


def test_iscc_is_optional_but_identifier_list_is_required():
    obj = Identifiers(identifier=[{"scheme": "doi", "code": "10.1234/x"}])
    data = obj.dict()
    assert "iscc" not in data
    assert data["identifier"][0]["scheme"] == "doi"

    with pytest.raises(ValidationError):
        Identifiers()


def test_identifier_min_items_is_enforced():
    with pytest.raises(ValidationError) as exc_info:
        Identifiers(identifier=[])
    errors = exc_info.value.errors()
    assert errors[0]["type"] == "too_short"
    assert errors[0]["loc"] == ("identifier",)
    assert errors[0]["input"] == []
    assert errors[0]["ctx"]["min_length"] == 1


def test_dict_json_and_jcs_round_trip_shapes():
    obj = Identifiers(**VALID_DATA)
    data = obj.dict()
    assert data["identifier"][0]["primary"] is True
    assert data["identifier"][1]["code"] == "USRC17607839"

    full = obj.json()
    assert f'"@context":"{CONTEXT_URL}"' in full
    assert '"@type":"Identifiers"' in full
    assert f'"$schema":"{SCHEMA_URL}"' in full
    assert '"scheme":"iswc"' in full

    compact = obj.json(ld=False)
    assert '"$schema"' in compact
    assert '"@context"' not in compact
    assert '"@type"' not in compact

    canonical = obj.jcs()
    assert isinstance(canonical, bytes)
    assert b'"identifier"' in canonical
    assert b'"primary":true' in canonical


def test_full_standalone_defaults_are_versioned():
    obj = Identifiers(**VALID_DATA)
    assert obj.context_ == CONTEXT_URL
    assert obj.type_ == "Identifiers"
    assert obj.schema_ == SCHEMA_URL

    data = obj.dict(exclude_unset=False)
    assert data["@context"] == CONTEXT_URL
    assert data["@type"] == "Identifiers"
    assert data["$schema"] == SCHEMA_URL


def test_recover_context_for_compact_identifiers_record_includes_nested_terms():
    data = {
        "$schema": SCHEMA_URL,
        "identifier": [{"scheme": "doi", "code": "10.1234/x", "scope": "work"}],
    }
    recovered = iss.recover_context(data)
    ctx = recovered["@context"]
    assert ctx["Identifiers"] == "http://purl.org/iscc/terms/#Identifiers"
    assert ctx["identifier"] == "http://schema.org/identifier"
    assert ctx["scheme"] == "http://schema.org/propertyID"
    assert ctx["code"] == "http://schema.org/value"
    assert ctx["scope"] == "http://purl.org/iscc/terms/#scope"
    assert ctx["primary"] == "http://purl.org/iscc/terms/#primary"


def test_published_example_validates_against_model():
    schema = _load_schema("identifiers.json")
    example = schema["examples"][0]
    obj = Identifiers(**example)
    assert obj.context_ == CONTEXT_URL
    assert obj.schema_ == SCHEMA_URL
    assert obj.identifier[0].scheme == "iswc"


def test_identifiers_schema_has_expected_context_and_constraints():
    schema = _load_schema("identifiers.json")
    assert schema["@context"]["iscc"] == "@id"
    assert schema["@context"]["identifier"] == "http://schema.org/identifier"
    assert schema["@context"]["scheme"] == "http://schema.org/propertyID"
    assert schema["required"] == ["identifier"]
    assert schema["properties"]["identifier"]["minItems"] == 1
    assert "@type" not in schema["properties"]["identifier"]["items"]["properties"]
