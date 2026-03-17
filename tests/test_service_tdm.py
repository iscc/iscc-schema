# -*- coding: utf-8 -*-
import pytest
from pydantic import ValidationError
import iscc_schema
from iscc_schema.service_tdm import TDM

CONTEXT_URL = f"http://purl.org/iscc/context/{iscc_schema.__version__}.jsonld"

VALID_TDM_DATA = {
    "train": "reserved",
    "inference": "open",
    "derive": "reserved",
    "search": "open",
    "analyze": "open",
}


def test_valid_construction():
    obj = TDM(**VALID_TDM_DATA)
    assert obj.train == "reserved"
    assert obj.inference == "open"
    assert obj.derive == "reserved"
    assert obj.search == "open"
    assert obj.analyze == "open"


def test_defaults():
    obj = TDM(**VALID_TDM_DATA)
    assert obj.context_ == CONTEXT_URL
    assert obj.type_ == "TDM"
    assert obj.schema_ == "http://purl.org/iscc/schema/tdm.json"


def test_dict():
    obj = TDM(**VALID_TDM_DATA)
    d = obj.dict()
    assert d["train"] == "reserved"
    assert d["inference"] == "open"
    assert d["derive"] == "reserved"
    assert d["search"] == "open"
    assert d["analyze"] == "open"


def test_dict_with_defaults():
    obj = TDM(**VALID_TDM_DATA)
    d = obj.dict(exclude_unset=False)
    assert d["@context"] == CONTEXT_URL
    assert d["@type"] == "TDM"
    assert d["$schema"] == "http://purl.org/iscc/schema/tdm.json"
    assert d["train"] == "reserved"
    assert d["inference"] == "open"


def test_json():
    obj = TDM(**VALID_TDM_DATA)
    j = obj.json()
    assert f'"@context":"{CONTEXT_URL}"' in j
    assert '"@type":"TDM"' in j
    assert '"train":"reserved"' in j
    assert '"inference":"open"' in j


def test_jcs():
    obj = TDM(**VALID_TDM_DATA)
    result = obj.jcs()
    assert isinstance(result, bytes)
    assert b'"train":"reserved"' in result
    assert b'"$schema"' in result


def test_all_reserved():
    data = {k: "reserved" for k in VALID_TDM_DATA}
    obj = TDM(**data)
    d = obj.dict()
    for field in ("train", "inference", "derive", "search", "analyze"):
        assert d[field] == "reserved"


def test_all_open():
    data = {k: "open" for k in VALID_TDM_DATA}
    obj = TDM(**data)
    d = obj.dict()
    for field in ("train", "inference", "derive", "search", "analyze"):
        assert d[field] == "open"


def test_invalid_enum_value():
    data = {**VALID_TDM_DATA, "train": "blocked"}
    with pytest.raises(ValidationError):
        TDM(**data)


def test_invalid_enum_value_inference():
    data = {**VALID_TDM_DATA, "inference": "yes"}
    with pytest.raises(ValidationError):
        TDM(**data)


def test_partial_fields():
    obj = TDM(train="reserved")
    d = obj.dict()
    assert d["train"] == "reserved"
    assert "inference" not in d
    assert "derive" not in d
    assert "search" not in d
    assert "analyze" not in d


def test_empty_construction():
    obj = TDM()
    d = obj.dict()
    assert "train" not in d
    assert "inference" not in d


def test_omitted_means_undetermined():
    obj = TDM(train="reserved", search="open")
    d = obj.dict()
    assert d["train"] == "reserved"
    assert d["search"] == "open"
    assert "inference" not in d
    assert "derive" not in d
    assert "analyze" not in d


def test_extra_fields_forbidden():
    data = {**VALID_TDM_DATA, "extra": "value"}
    with pytest.raises(ValidationError):
        TDM(**data)


def test_import_from_package():
    from iscc_schema import TDM as TDMFromPkg

    obj = TDMFromPkg(**VALID_TDM_DATA)
    assert obj.train == "reserved"
