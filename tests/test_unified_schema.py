"""Tests for embedded JSON-LD contexts in JSON Schema files and context recovery."""

import json
import pathlib

import pytest
import yaml

import iscc_schema as iss

ROOT = pathlib.Path(__file__).parent.parent
MODELS = ROOT / "iscc_schema" / "models"


def _load_json(name):
    # type: (str) -> dict
    path = ROOT / "docs" / "schema" / name
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _load_jsonld():
    # type: () -> dict
    path = ROOT / "docs" / "context" / "iscc.jsonld"
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# --- Schema embedding tests ---


def test_iscc_json_has_context():
    schema = _load_json("iscc.json")
    assert "@context" in schema
    assert isinstance(schema["@context"], dict)


def test_iscc_json_context_matches_jsonld():
    schema = _load_json("iscc.json")
    jsonld = _load_jsonld()
    assert schema["@context"] == jsonld["@context"]


def test_standalone_schemas_have_context():
    for name in ("isbn.json", "isrc.json", "tdm.json"):
        schema = _load_json(name)
        assert "@context" in schema, f"{name} missing @context"
        assert isinstance(schema["@context"], dict), f"{name} @context not a dict"


def test_standalone_context_terms_match_properties():
    for yaml_name in ("isbn.yaml", "isrc.yaml", "tdm.yaml"):
        with open(MODELS / yaml_name, encoding="utf-8") as f:
            yaml_schema = yaml.safe_load(f)
        json_name = yaml_name.replace(".yaml", ".json")
        json_schema = _load_json(json_name)
        ctx = json_schema["@context"]
        for prop_name, prop_def in yaml_schema.get("properties", {}).items():
            if prop_name in ("@context", "@type", "$schema"):
                continue
            if "x-iscc-context" in prop_def:
                assert prop_name in ctx, f"{json_name}: {prop_name} missing from @context"


def test_context_property_accepts_string_and_object():
    schema = _load_json("iscc.json")
    ctx_prop = schema["properties"]["@context"]
    assert "oneOf" in ctx_prop
    types = [item.get("type") for item in ctx_prop["oneOf"]]
    assert "string" in types
    assert "object" in types


def test_context_at_root_does_not_break_structure():
    schema = _load_json("iscc.json")
    assert schema["title"] == "iscc-collection"
    assert schema["type"] == "object"
    assert "properties" in schema


# --- Recovery function tests ---


def test_recover_context_from_schema_field():
    data = {"$schema": "http://purl.org/iscc/schema/isbn.json", "isbn": "9789295055124"}
    result = iss.recover_context(data)
    assert "@context" in result
    assert "ISBN" in result["@context"]
    assert result["isbn"] == "9789295055124"


def test_recover_context_from_type_field():
    data = {"@type": "ISBN", "isbn": "9789295055124"}
    result = iss.recover_context(data)
    assert "@context" in result
    assert "ISBN" in result["@context"]


def test_recover_context_explicit_param():
    data = {
        "@type": "CreativeWork",
        "iscc": "ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY",
    }
    result = iss.recover_context(data, schema="isbn")
    assert "ISBN" in result["@context"]


def test_recover_context_default():
    data = {"iscc": "ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY"}
    result = iss.recover_context(data)
    assert "@context" in result
    assert "CreativeWork" in result["@context"]


def test_recover_context_already_present():
    data = {
        "@context": "http://purl.org/iscc/context",
        "iscc": "ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY",
    }
    result = iss.recover_context(data)
    assert result is data


def test_recover_context_unknown_schema():
    data = {"$schema": "http://example.com/unknown.json"}
    with pytest.raises(ValueError, match="Unknown schema"):
        iss.recover_context(data)


def test_recover_context_versioned_url():
    data = {
        "$schema": "http://purl.org/iscc/schema/0.5.0.json",
        "iscc": "ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY",
    }
    result = iss.recover_context(data)
    assert "@context" in result
    assert "CreativeWork" in result["@context"]


def test_recover_context_unversioned_url():
    data = {
        "$schema": "http://purl.org/iscc/schema",
        "iscc": "ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY",
    }
    result = iss.recover_context(data)
    assert "@context" in result
    assert "CreativeWork" in result["@context"]
