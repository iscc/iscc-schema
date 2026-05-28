# -*- coding: utf-8 -*-
import pytest
from pydantic import ValidationError
import iscc_schema
from iscc_schema.service_tdm import TDM

CONTEXT_URL = f"http://purl.org/iscc/context/{iscc_schema.__version__}.jsonld"

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
    assert obj.schema_ == "http://purl.org/iscc/schema/tdm.json"


def test_dict():
    obj = TDM(**VALID_TDM_DATA)
    d = obj.dict()
    assert d["iscc"] == "ISCC:MAACAJINXFXA2SQX"
    assert d["tdm_reservation"] == 1
    assert d["tdm_policy"] == "https://example.com/policy.json"


def test_dict_compact():
    obj = TDM(**VALID_TDM_DATA)
    d = obj.dict()
    assert "$schema" in d
    assert "@context" not in d
    assert "@type" not in d


def test_dict_ld():
    obj = TDM(**VALID_TDM_DATA)
    d = obj.dict(exclude_unset=False, ld=True)
    assert d["@context"] == CONTEXT_URL
    assert d["@type"] == "TDM"
    assert d["$schema"] == "http://purl.org/iscc/schema/tdm.json"
    assert d["tdm_reservation"] == 1


def test_json_compact():
    obj = TDM(**VALID_TDM_DATA)
    j = obj.json()
    assert '"$schema"' in j
    assert '"@context"' not in j
    assert '"@type"' not in j
    assert '"tdm_reservation":1' in j
    assert '"tdm_policy":"https://example.com/policy.json"' in j
    assert '"iscc":"ISCC:MAACAJINXFXA2SQX"' in j


def test_json_ld():
    obj = TDM(**VALID_TDM_DATA)
    j = obj.json(ld=True)
    assert f'"@context":"{CONTEXT_URL}"' in j
    assert '"@type":"TDM"' in j
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
