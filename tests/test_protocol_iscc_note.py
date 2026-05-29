# -*- coding: utf-8 -*-
"""Tests for the IsccNote declaration schema.

IsccNote is the permanent, signed ISCC Declaration log record submitted to an
ISCC-HUB. It is a *protocol* schema: it serializes to compact JSON by default
(no @context/@type) and pins a version-specific $schema URL, which is its sole
version anchor and part of the JCS bytes the signature proof is computed over.

These tests cover serialization (compact default and JSON-LD upgrade), JCS
canonicalization, the version-specific $schema, the required field set, the nested
signature object, and the pilot correctness gates: acceptance of full-length 256-bit
ISCC-CODEs / ISCC-UNITs, a signature proof length of 65-89 characters, and an optional
timestamp.

The 256-bit ISCC values below are real codes generated with iscc-core 1.3.0.
"""

import json
import pathlib
import re

import pytest
from pydantic import ValidationError

import iscc_schema
from iscc_schema.protocol_iscc_note import IsccNote

ROOT = pathlib.Path(__file__).parent.parent
CONTEXT_URL = f"http://purl.org/iscc/context/{iscc_schema.__version__}.jsonld"
SCHEMA_URL = f"http://purl.org/iscc/schema/iscc-note-{iscc_schema.__version__}.json"
SCHEMA_BASE_URL = "http://purl.org/iscc/schema/iscc-note.json"

# Full-length 256-bit values (real, from iscc-core 1.3.0). A 256-bit code/unit has a
# 55-character base32 body = 34 bytes (2-byte header + 32-byte/256-bit digest).
ISCC_CODE_256 = "ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY"
UNITS_256 = [
    "ISCC:IADSKPIPGRQAQXBHN4BY3Y2FZDUVHIYG6SQH7H5HP5NPQVR4HVZHJRI",  # Instance-Code
    "ISCC:GADUCK27AIQUBLC3ALIINORUJ6JEC4GHRWXSXLIO5VLKRE65RM6A5RI",  # Data-Code
    "ISCC:AADWN77F727NXSUSUVDFOUS64JFPMZ4GAR5NJ3O5P563LTMXWS5XNSQ",  # Meta-Code
]
DATAHASH = "1e20253d0f3460085c276f038de345c8e953a306f4a07f9fa77f5af8563c3d7274c5"
METAHASH = "1e208bad08ad56b5517e09bc8bc5e2281b2d8f21d096939a310f539cf5007d443772"
NONCE = "0013a3c214c05796673503e6e549446d"
PUBKEY = "z6MkmeDbeC5BecFmVnTHA5PWEBaVUrGLdB3weGE2KYnXfHso"
PROOF = "z5j9nrpPw3oYSAN4XbCvk2sUtkwrueTD6V2Y35gS1KFTode2ED2YQWokPmoXw6QBYtYEFxtAQfzBhdNyr8PMwP79G"

VALID_SIGNATURE = {
    "version": "ISCC-SIG v1.0",
    "controller": "did:web:example.com",
    "pubkey": PUBKEY,
    "proof": PROOF,
}

VALID_NOTE = {
    "iscc_code": ISCC_CODE_256,
    "datahash": DATAHASH,
    "nonce": NONCE,
    "signature": VALID_SIGNATURE,
}


def _note(**overrides):
    # type: (...) -> dict
    """A valid IsccNote payload with the given fields overridden."""
    data = dict(VALID_NOTE)
    data.update(overrides)
    return data


def _proof(length):
    # type: (int) -> str
    """A pattern-valid base58btc proof string of the given total length."""
    return "z" + "1" * (length - 1)


def _load_schema_json():
    # type: () -> dict
    """Load the generated docs/schema/iscc-note.json file."""
    with open(ROOT / "docs" / "schema" / "iscc-note.json", encoding="utf-8") as f:
        return json.load(f)


def _load_shared_context():
    # type: () -> dict
    """Load the @context of the generated shared docs/context/iscc.jsonld file."""
    with open(ROOT / "docs" / "context" / "iscc.jsonld", encoding="utf-8") as f:
        return json.load(f)["@context"]


# --- Construction & defaults ---


def test_valid_construction():
    obj = IsccNote(**VALID_NOTE)
    assert obj.iscc_code == ISCC_CODE_256
    assert obj.datahash == DATAHASH
    assert obj.nonce == NONCE
    assert obj.signature.proof == PROOF


def test_defaults():
    obj = IsccNote(**VALID_NOTE)
    assert obj.context_ == CONTEXT_URL
    assert obj.type_ == "IsccNote"
    assert obj.schema_ == SCHEMA_URL


def test_schema_default_is_version_specific():
    """The $schema default pins the version-specific archive URL (the sole version
    anchor once @context/@type are dropped in compact form)."""
    obj = IsccNote(**VALID_NOTE)
    assert obj.schema_ == SCHEMA_URL
    assert obj.schema_.endswith(f"-{iscc_schema.__version__}.json")


def test_signature_version_defaults():
    """signature.version defaults to 'ISCC-SIG v1.0' without explicit assignment."""
    obj = IsccNote(**_note(signature={"pubkey": PUBKEY, "proof": PROOF}))
    assert obj.signature.version == "ISCC-SIG v1.0"


def test_import_from_package():
    from iscc_schema import IsccNote as IsccNoteFromPkg

    obj = IsccNoteFromPkg(**VALID_NOTE)
    assert obj.type_ == "IsccNote"


# --- Serialization: compact (default) vs JSON-LD upgrade ---


def test_dict_default_is_compact():
    """The default dict() is compact: version-specific $schema, no @context/@type."""
    obj = IsccNote(**VALID_NOTE)
    d = obj.dict()
    assert d["$schema"] == SCHEMA_URL
    assert "@context" not in d
    assert "@type" not in d
    assert d["iscc_code"] == ISCC_CODE_256


def test_dict_jsonld_upgrade():
    obj = IsccNote(**VALID_NOTE)
    d = obj.dict(ld=True, exclude_unset=False)
    assert d["@context"] == CONTEXT_URL
    assert d["@type"] == "IsccNote"
    assert d["$schema"] == SCHEMA_URL
    assert d["iscc_code"] == ISCC_CODE_256


def test_json_default_is_compact():
    obj = IsccNote(**VALID_NOTE)
    j = obj.json()
    assert f'"$schema":"{SCHEMA_URL}"' in j
    assert '"@context"' not in j
    assert '"@type"' not in j
    assert f'"iscc_code":"{ISCC_CODE_256}"' in j


def test_json_jsonld_upgrade():
    obj = IsccNote(**VALID_NOTE)
    j = obj.json(ld=True)
    assert f'"@context":"{CONTEXT_URL}"' in j
    assert '"@type":"IsccNote"' in j
    assert f'"$schema":"{SCHEMA_URL}"' in j


def test_units_serialize_as_strings():
    obj = IsccNote(**_note(units=UNITS_256))
    d = obj.dict()
    assert d["units"] == UNITS_256


# --- JCS canonicalization (the signature proof is computed over this) ---


def test_jcs_default_is_compact():
    """jcs() defaults to the compact form and must succeed with timestamp, nested
    signature and units all set; it is the canonicalization the EdDSA proof is signed
    over. A datetime-typed timestamp would break this, which is why timestamp is a
    plain string."""
    obj = IsccNote(
        **_note(timestamp="2025-08-12T14:30:00.123Z", units=UNITS_256, metahash=METAHASH)
    )
    result = obj.jcs()
    assert isinstance(result, bytes)
    assert b'"@context"' not in result
    assert b'"@type"' not in result
    assert b'"$schema"' in result
    assert b'"iscc_code"' in result
    assert b'"signature"' in result
    assert b'"proof"' in result
    assert b'"timestamp"' in result


def test_jcs_jsonld_upgrade_roundtrips():
    obj = IsccNote(**_note(timestamp="2025-08-12T14:30:00.123Z", units=UNITS_256))
    result = obj.jcs(ld=True)
    assert isinstance(result, bytes)
    assert b'"@context"' in result
    assert b'"iscc_code"' in result


# --- Required fields ---


@pytest.mark.parametrize("missing", ["iscc_code", "datahash", "nonce", "signature"])
def test_required_fields(missing):
    data = dict(VALID_NOTE)
    del data[missing]
    with pytest.raises(ValidationError):
        IsccNote(**data)


def test_timestamp_optional():
    """timestamp is optional (intentional deviation from the ISCC-HUB OpenAPI, which
    marks it required) since the Hub assigns the authoritative timestamp on receipt."""
    obj = IsccNote(**VALID_NOTE)
    assert obj.timestamp is None
    assert "timestamp" not in obj.dict()


def test_timestamp_accepted():
    obj = IsccNote(**_note(timestamp="2025-08-12T14:30:00.123Z"))
    assert obj.timestamp == "2025-08-12T14:30:00.123Z"


def test_timestamp_rejects_non_utc():
    with pytest.raises(ValidationError):
        IsccNote(**_note(timestamp="2025-08-12T14:30:00+02:00"))


# --- Nested signature object ---


@pytest.mark.parametrize("missing", ["pubkey", "proof"])
def test_signature_required_fields(missing):
    sig = dict(VALID_SIGNATURE)
    del sig[missing]
    with pytest.raises(ValidationError):
        IsccNote(**_note(signature=sig))


def test_signature_invalid_pubkey_pattern():
    with pytest.raises(ValidationError):
        IsccNote(**_note(signature={**VALID_SIGNATURE, "pubkey": "not-a-multibase-key!"}))


def test_signature_pubkey_is_fixed_48():
    with pytest.raises(ValidationError):
        IsccNote(**_note(signature={**VALID_SIGNATURE, "pubkey": "z" + "1" * 46}))


def test_signature_controller_optional():
    obj = IsccNote(**_note(signature={"pubkey": PUBKEY, "proof": PROOF}))
    assert obj.signature.controller is None


# --- Gate: full-length 256-bit codes (verify, do not assume) ---


def test_iscc_code_256bit_accepted():
    """The pilot mandates 256-bit components; the iscc_code pattern must accept a
    real full-length 256-bit ISCC-CODE."""
    obj = IsccNote(**VALID_NOTE)
    assert obj.iscc_code == ISCC_CODE_256
    assert len(ISCC_CODE_256.split(":")[1]) == 55


def test_units_256bit_accepted():
    """The units pattern must accept real full-length 256-bit ISCC-UNITs."""
    obj = IsccNote(**_note(units=UNITS_256))
    assert obj.dict()["units"] == UNITS_256
    for unit in UNITS_256:
        assert len(unit.split(":")[1]) == 55


def test_schema_patterns_accept_256bit():
    """The published JSON Schema patterns themselves accept 256-bit codes/units."""
    schema = _load_schema_json()
    code_pattern = schema["properties"]["iscc_code"]["pattern"]
    unit_pattern = schema["properties"]["units"]["items"]["pattern"]
    assert re.match(code_pattern, ISCC_CODE_256)
    for unit in UNITS_256:
        assert re.match(unit_pattern, unit)


def test_units_invalid_rejected():
    with pytest.raises(ValidationError):
        IsccNote(**_note(units=["not-an-iscc-unit"]))


def test_units_max_items():
    with pytest.raises(ValidationError):
        IsccNote(**_note(units=UNITS_256 + UNITS_256))  # 6 items, above maxItems (4)


def test_units_empty_coerced_to_absent():
    """An empty units list is coerced to None (absent) by the base validator."""
    obj = IsccNote(**_note(units=[]))
    assert obj.units is None


# --- Gate: signature proof length 65-89 (not fixed 89) ---


@pytest.mark.parametrize("length", [65, 72, 88, 89])
def test_proof_valid_lengths(length):
    """Base58btc of a 64-byte Ed25519 signature is 65-89 chars; it is shorter when the
    signature has leading zero bytes (~0.4% of signatures). A fixed-89 bound would
    silently reject valid signatures on a permanent record."""
    obj = IsccNote(**_note(signature={**VALID_SIGNATURE, "proof": _proof(length)}))
    assert len(obj.signature.proof) == length


@pytest.mark.parametrize("length", [64, 90])
def test_proof_invalid_lengths(length):
    with pytest.raises(ValidationError):
        IsccNote(**_note(signature={**VALID_SIGNATURE, "proof": _proof(length)}))


def test_proof_invalid_pattern():
    with pytest.raises(ValidationError):
        IsccNote(**_note(signature={**VALID_SIGNATURE, "proof": "0" * 80}))


# --- Field pattern validation ---


@pytest.mark.parametrize(
    "field,bad_value",
    [
        ("iscc_code", "ISCC:lowercase-not-allowed"),
        ("iscc_code", "NOTISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY"),
        ("datahash", "ff20253d0f3460085c276f038de345c8e953a306f4a07f9fa77f5af8563c3d7274c5"),
        ("datahash", "1e20253d"),
        ("nonce", "0013a3c214c05796673503e6e549446"),  # 31 chars
        ("nonce", "0013A3C214C05796673503E6E549446D"),  # uppercase hex
    ],
)
def test_field_pattern_validation(field, bad_value):
    with pytest.raises(ValidationError):
        IsccNote(**_note(**{field: bad_value}))


# --- gateway: HTTP(S) URL or RFC 6570 URI template ---


def test_gateway_accepts_url():
    obj = IsccNote(**_note(gateway="https://gateway.example.com/declaration"))
    assert obj.gateway == "https://gateway.example.com/declaration"


def test_gateway_accepts_uri_template():
    template = "https://gateway.example.com/declaration/{iscc_code}"
    obj = IsccNote(**_note(gateway=template))
    assert obj.gateway == template


def test_gateway_rejects_non_http():
    with pytest.raises(ValidationError):
        IsccNote(**_note(gateway="ftp://example.com/resource"))


# --- additionalProperties: false at both levels ---


def test_extra_field_rejected():
    with pytest.raises(ValidationError):
        IsccNote(**_note(unexpected="value"))


def test_extra_signature_field_rejected():
    with pytest.raises(ValidationError):
        IsccNote(**_note(signature={**VALID_SIGNATURE, "unexpected": "value"}))


# --- Version-specific $schema & archive (reads generated artifacts) ---


def test_schema_json_schema_const_is_versioned():
    """The published JSON Schema requires a version-specific $schema const."""
    schema = _load_schema_json()
    assert schema["properties"]["$schema"]["const"] == SCHEMA_URL


def test_schema_json_requires_schema_field():
    """$schema is required: it is the sole version anchor of a compact declaration."""
    assert "$schema" in _load_schema_json()["required"]


def test_versioned_archive_exists():
    """A version-pinned archive copy is written alongside the latest schema."""
    archive = ROOT / "docs" / "schema" / f"iscc-note-{iscc_schema.__version__}.json"
    assert archive.exists()
    data = json.loads(archive.read_text(encoding="utf-8"))
    assert data["$id"] == SCHEMA_URL
    assert data["properties"]["$schema"]["const"] == SCHEMA_URL


def test_latest_schema_id_is_unversioned():
    """The latest schema file keeps the unversioned $id (it is 'latest')."""
    assert _load_schema_json()["$id"] == SCHEMA_BASE_URL


def test_schema_example_is_compact_and_versioned():
    """The published example is the compact wire form with a version-specific $schema."""
    example = _load_schema_json()["examples"][0]
    assert example["$schema"] == SCHEMA_URL
    assert "@context" not in example
    assert "@type" not in example


# --- JSON-LD context coverage (reads generated artifacts) ---


def test_schema_json_context_has_terms():
    """timestamp and gateway are new ISCC vocabulary terms introduced by IsccNote."""
    ctx = _load_schema_json()["@context"]
    assert ctx["timestamp"] == "http://purl.org/iscc/terms/#timestamp"
    assert ctx["gateway"] == "http://purl.org/iscc/terms/#gateway"
    assert ctx["datahash"] == "http://purl.org/iscc/terms/#datahash"
    assert ctx["nonce"] == "http://purl.org/iscc/terms/#nonce"
    assert ctx["signature"] == "http://purl.org/iscc/terms/#signature"


def test_schema_json_iscc_code_is_id():
    """The declared ISCC-CODE is the JSON-LD subject (@id) of the record."""
    assert _load_schema_json()["@context"]["iscc_code"] == "@id"


def test_new_terms_in_shared_context():
    ctx = _load_shared_context()
    assert ctx["timestamp"] == "http://purl.org/iscc/terms/#timestamp"
    assert ctx["gateway"] == "http://purl.org/iscc/terms/#gateway"
    assert ctx["IsccNote"] == "http://purl.org/iscc/terms/#IsccNote"


def test_recover_context_from_versioned_schema():
    """A compact record carries a version-specific $schema; recovery normalizes the
    version suffix back to the bundled context."""
    data = {"$schema": SCHEMA_URL, "iscc_code": ISCC_CODE_256}
    result = iscc_schema.recover_context(data)
    assert result["@context"]["iscc_code"] == "@id"
    assert result["@context"]["timestamp"] == "http://purl.org/iscc/terms/#timestamp"


def test_recover_context_from_unversioned_schema():
    data = {"$schema": SCHEMA_BASE_URL, "iscc_code": ISCC_CODE_256}
    result = iscc_schema.recover_context(data)
    assert result["@context"]["iscc_code"] == "@id"


def test_recover_context_from_type():
    data = {"@type": "IsccNote", "iscc_code": ISCC_CODE_256}
    result = iscc_schema.recover_context(data)
    assert "IsccNote" in result["@context"]


# --- x-iscc-jsonld extension: the JSON-LD upgrade path documented in the schema ---


def test_schema_has_jsonld_extension():
    """The schema carries a top-level x-iscc-jsonld extension that documents how to turn a
    compact record back into JSON-LD - the recipe a compact record itself cannot carry."""
    ext = _load_schema_json()["x-iscc-jsonld"]
    assert ext["context"] == CONTEXT_URL
    assert ext["type"] == "IsccNote"
    assert "@context" in ext["upgrade"]
    assert "@type" in ext["upgrade"]


def test_jsonld_extension_context_matches_model_output():
    """The extension's context URL is exactly the @context the model emits with ld=True, so
    a record reconstructed by following the recipe matches a model-produced JSON-LD record."""
    ext_context = _load_schema_json()["x-iscc-jsonld"]["context"]
    model_context = IsccNote(**VALID_NOTE).dict(ld=True, exclude_unset=False)["@context"]
    assert ext_context == model_context


def test_jsonld_extension_type_matches_type_const():
    """The extension's type matches the @type const the schema declares."""
    schema = _load_schema_json()
    assert schema["x-iscc-jsonld"]["type"] == schema["properties"]["@type"]["const"]


def test_jsonld_extension_recipe_is_actionable():
    """Following the documented recipe - inline this schema's top-level @context term map and
    set @type from the extension - upgrades a compact record to JSON-LD whose term map resolves
    the record's subject (iscc_code) to the @id keyword."""
    schema = _load_schema_json()
    term_map = schema["@context"]
    ext = schema["x-iscc-jsonld"]
    compact = {"$schema": SCHEMA_URL, "iscc_code": ISCC_CODE_256, "datahash": DATAHASH}
    upgraded = {"@context": term_map, "@type": ext["type"], **compact}
    assert upgraded["@context"]["iscc_code"] == "@id"
    assert upgraded["@type"] == "IsccNote"


def test_schema_description_points_to_jsonld_extension():
    """The $schema property description points humans to the upgrade extension."""
    desc = _load_schema_json()["properties"]["$schema"]["description"]
    assert "x-iscc-jsonld" in desc


def test_jsonld_extension_in_versioned_archive():
    """The version-pinned archive carries the same upgrade extension as the latest schema."""
    archive = ROOT / "docs" / "schema" / f"iscc-note-{iscc_schema.__version__}.json"
    ext = json.loads(archive.read_text(encoding="utf-8"))["x-iscc-jsonld"]
    assert ext["type"] == "IsccNote"
    assert ext["context"] == CONTEXT_URL
