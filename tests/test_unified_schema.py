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
    for name in ("isbn.json", "isrc.json", "stm.json", "tdm.json", "genai.json", "iscc-note.json"):
        schema = _load_json(name)
        assert "@context" in schema, f"{name} missing @context"
        assert isinstance(schema["@context"], dict), f"{name} @context not a dict"


def test_standalone_context_terms_match_properties():
    for yaml_name in (
        "isbn.yaml",
        "isrc.yaml",
        "stm.yaml",
        "tdm.yaml",
        "genai.yaml",
        "iscc-note.yaml",
    ):
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


# --- Standalone schema versioning (versioned @context default + archives) ---

STANDALONE_JSON = ("isbn.json", "isrc.json", "stm.json", "tdm.json", "genai.json", "iscc-note.json")
CONTEXT_URL = f"http://purl.org/iscc/context/{iss.__version__}.jsonld"


def test_standalone_schemas_have_versioned_context_default():
    """Every standalone schema pins a versioned @context default matching the package version,
    so JSON Schema consumers resolve the same context the Pydantic model emits with ld=True."""
    for name in STANDALONE_JSON:
        schema = _load_json(name)
        ctx_default = schema["properties"]["@context"].get("default")
        assert ctx_default == CONTEXT_URL, f"{name} @context default is {ctx_default!r}"


def _without_id(schema):
    # type: (dict) -> dict
    """Return a schema dict without its $id, for comparing an archive against the latest file."""
    return {k: v for k, v in schema.items() if k != "$id"}


def test_standalone_versioned_archives_exist():
    """A version-pinned archive copy is written alongside each standalone schema, identical to
    the latest file except for its versioned $id."""
    for name in STANDALONE_JSON:
        base = name.replace(".json", "")
        archive_name = f"{base}-{iss.__version__}.json"
        archive = _load_json(archive_name)
        latest = _load_json(name)
        assert archive["$id"] == f"http://purl.org/iscc/schema/{archive_name}"
        assert _without_id(archive) == _without_id(latest), f"{archive_name} differs beyond $id"


def test_iscc_md_pins_versioned_context_and_schema():
    """The main ISCC Metadata docs page pins @context and $schema to the versioned whole-schema
    URLs in both its examples and its field-reference "Default" column, matching the model output
    and the published iscc.json (which default to the same versioned URLs)."""
    text = (ROOT / "docs" / "schema" / "iscc.md").read_text(encoding="utf-8")
    versioned_ctx = f"http://purl.org/iscc/context/{iss.__version__}.jsonld"
    versioned_schema = f"http://purl.org/iscc/schema/{iss.__version__}.json"
    assert versioned_ctx in text
    assert versioned_schema in text
    # No unversioned base URL survives as a complete JSON value or field-table cell.
    assert '"http://purl.org/iscc/context"' not in text
    assert '"http://purl.org/iscc/schema"' not in text
    assert "| http://purl.org/iscc/context |" not in text
    assert "| http://purl.org/iscc/schema |" not in text


def test_recover_context_from_versioned_seed_archive():
    """recover_context resolves a versioned seed archive $schema URL to the bundled context."""
    data = {
        "$schema": f"http://purl.org/iscc/schema/isbn-{iss.__version__}.json",
        "isbn": "9789295055124",
    }
    result = iss.recover_context(data)
    assert "ISBN" in result["@context"]


def test_recover_context_from_versioned_service_archive():
    """recover_context resolves a versioned service archive $schema URL to the bundled context."""
    data = {
        "$schema": f"http://purl.org/iscc/schema/tdm-{iss.__version__}.json",
        "iscc": "ISCC:MAACAJINXFXA2SQX",
    }
    result = iss.recover_context(data)
    assert "TDM" in result["@context"]


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


def test_form_in_jsonld_context():
    """Test that form property mapping appears in generated JSON-LD context."""
    jsonld = _load_jsonld()
    ctx = jsonld["@context"]
    assert "form" in ctx
    assert ctx["form"] == "http://schema.org/additionalType"


def test_form_enum_values_in_jsonld_context():
    """Test that form enum values have IRI mappings in the JSON-LD context."""
    jsonld = _load_jsonld()
    ctx = jsonld["@context"]
    assert ctx["ScholarlyArticle"] == "http://schema.org/ScholarlyArticle"
    assert ctx["Book"] == "http://schema.org/Book"
    assert ctx["Movie"] == "http://schema.org/Movie"


def test_form_in_iscc_json_schema():
    """Test that form field appears in generated JSON Schema with enum constraint."""
    schema = _load_json("iscc.json")
    props = schema["properties"]
    assert "form" in props
    assert "enum" in props["form"]
    assert "ScholarlyArticle" in props["form"]["enum"]


def test_recover_context_unversioned_url():
    data = {
        "$schema": "http://purl.org/iscc/schema",
        "iscc": "ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY",
    }
    result = iss.recover_context(data)
    assert "@context" in result
    assert "CreativeWork" in result["@context"]


def test_tdm_context_uses_nest():
    schema = _load_json("iscc.json")
    assert schema["@context"]["tdm"] == "@nest"


def test_tdm_context_has_w3c_terms():
    jsonld = _load_jsonld()
    ctx = jsonld["@context"]
    assert ctx["tdm_reservation"] == "http://www.w3.org/ns/tdmrep#reservation"
    assert ctx["tdm_policy"]["@id"] == "http://www.w3.org/ns/tdmrep#policy"
    assert ctx["tdm_policy"]["@type"] == "@id"
