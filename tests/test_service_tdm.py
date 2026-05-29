# -*- coding: utf-8 -*-
import json
import pathlib

import pytest
from pydantic import ValidationError
import iscc_schema
from iscc_schema.service_tdm import TDM

ROOT = pathlib.Path(__file__).parent.parent
CONTEXT_URL = f"http://purl.org/iscc/context/{iscc_schema.__version__}.jsonld"
SCHEMA_URL = f"http://purl.org/iscc/schema/tdm-{iscc_schema.__version__}.json"

VALID_TDM_DATA = {
    "iscc": "ISCC:MAACAJINXFXA2SQX",
    "tdm_reservation": 1,
    "tdm_policy": "https://example.com/policy.json",
}


def test_valid_construction():
    obj = TDM(**VALID_TDM_DATA)
    assert obj.iscc == "ISCC:MAACAJINXFXA2SQX"
    assert obj.tdm_reservation == 1
    assert str(obj.tdm_policy) == "https://example.com/policy.json"


def test_defaults():
    obj = TDM(**VALID_TDM_DATA)
    assert obj.context_ == CONTEXT_URL
    assert obj.type_ == "TDM"
    assert obj.schema_ == SCHEMA_URL


def test_dict():
    obj = TDM(**VALID_TDM_DATA)
    d = obj.dict()
    assert d["iscc"] == "ISCC:MAACAJINXFXA2SQX"
    assert d["tdm_reservation"] == 1
    assert d["tdm_policy"] == "https://example.com/policy.json"


def test_dict_with_defaults():
    obj = TDM(**VALID_TDM_DATA)
    d = obj.dict(exclude_unset=False)
    assert d["@context"] == CONTEXT_URL
    assert d["@type"] == "TDM"
    assert d["$schema"] == SCHEMA_URL
    assert d["tdm_reservation"] == 1


def test_json():
    obj = TDM(**VALID_TDM_DATA)
    j = obj.json()
    assert f'"@context":"{CONTEXT_URL}"' in j
    assert '"@type":"TDM"' in j
    assert '"tdm_reservation":1' in j
    assert '"tdm_policy":"https://example.com/policy.json"' in j
    assert '"iscc":"ISCC:MAACAJINXFXA2SQX"' in j


def test_json_compact():
    obj = TDM(**VALID_TDM_DATA)
    j = obj.json(ld=False)
    assert '"$schema"' in j
    assert '"@context"' not in j
    assert '"@type"' not in j
    assert '"tdm_reservation":1' in j


def test_jcs():
    obj = TDM(**VALID_TDM_DATA)
    result = obj.jcs()
    assert isinstance(result, bytes)
    assert b'"tdm_reservation":1' in result
    assert b'"$schema"' in result


def test_reservation_values():
    obj0 = TDM(tdm_reservation=0)
    assert obj0.tdm_reservation == 0
    obj1 = TDM(tdm_reservation=1)
    assert obj1.tdm_reservation == 1


def test_invalid_reservation_value():
    with pytest.raises(ValidationError):
        TDM(tdm_reservation=2)


def test_invalid_policy_not_uri():
    with pytest.raises(ValidationError):
        TDM(tdm_policy="not-a-url")


def test_partial_fields():
    obj = TDM(tdm_reservation=1)
    d = obj.dict()
    assert d["tdm_reservation"] == 1
    assert "tdm_policy" not in d
    assert "iscc" not in d


def test_empty_construction():
    obj = TDM()
    d = obj.dict()
    assert "tdm_reservation" not in d
    assert "tdm_policy" not in d
    assert "iscc" not in d


def test_backward_compat_v050():
    obj = TDM(train="reserved", inference="open")
    d = obj.dict()
    assert d["train"] == "reserved"
    assert d["inference"] == "open"


def test_import_from_package():
    from iscc_schema import TDM as TDMFromPkg

    obj = TDMFromPkg(**VALID_TDM_DATA)
    assert obj.tdm_reservation == 1


def test_schema_has_jsonld_extension():
    """Standalone schemas carry a top-level x-iscc-jsonld extension; TDM defaults to JSON-LD
    but may serialize compact, so it documents the upgrade path like the other categories."""
    schema = json.loads((ROOT / "docs" / "schema" / "tdm.json").read_text(encoding="utf-8"))
    ext = schema["x-iscc-jsonld"]
    assert ext["context"] == CONTEXT_URL
    assert ext["type"] == "TDM"
    assert "x-iscc-jsonld" in schema["properties"]["$schema"]["description"]


def test_schema_context_default_is_versioned():
    """The published JSON Schema pins the versioned @context default, matching the value the
    Pydantic model emits with ld=True."""
    schema = json.loads((ROOT / "docs" / "schema" / "tdm.json").read_text(encoding="utf-8"))
    assert schema["properties"]["@context"]["default"] == CONTEXT_URL
    assert TDM(**VALID_TDM_DATA).context_ == CONTEXT_URL


def test_schema_example_anchors_are_versioned():
    """TDM defaults to JSON-LD, so its published example carries the versioned @context and
    $schema URLs the model emits, not the unversioned bases from the YAML source."""
    schema = json.loads((ROOT / "docs" / "schema" / "tdm.json").read_text(encoding="utf-8"))
    example = schema["examples"][0]
    assert example["@context"] == CONTEXT_URL
    assert example["$schema"] == SCHEMA_URL


def test_latest_schema_const_is_versioned():
    """The latest schema file pins a version-specific $schema const while keeping an unversioned
    $id: records identify the exact schema version; the file is served at the 'latest' URL."""
    schema = json.loads((ROOT / "docs" / "schema" / "tdm.json").read_text(encoding="utf-8"))
    assert schema["properties"]["$schema"]["const"] == SCHEMA_URL
    assert schema["$id"] == "http://purl.org/iscc/schema/tdm.json"


def test_versioned_archive_exists():
    """A version-pinned archive is written alongside the latest schema; its $id and its $schema
    const both carry the version, so records validated against it pin the exact schema version."""
    archive = ROOT / "docs" / "schema" / f"tdm-{iscc_schema.__version__}.json"
    assert archive.exists()
    data = json.loads(archive.read_text(encoding="utf-8"))
    assert data["$id"] == SCHEMA_URL
    assert data["properties"]["$schema"]["const"] == SCHEMA_URL
