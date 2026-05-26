# -*- coding: utf-8 -*-
import pytest
from pydantic import ValidationError

import iscc_schema as iss


def test_embeddable_non_uri():
    m = iss.IsccMeta.model_construct(license="Hello License")
    assert m.dict() == {"license": "Hello License"}
    with pytest.raises(ValidationError):
        iss.IsccMeta(license="Hello License")


def test_tdm_field():
    tdm_data = {
        "tdm_reservation": 1,
        "tdm_policy": "https://example.com/policy.json",
    }
    m = iss.IsccMeta(tdm=tdm_data)
    d = m.dict()
    assert d["tdm"]["tdm_reservation"] == 1
    assert d["tdm"]["tdm_policy"] == "https://example.com/policy.json"


def test_tdm_field_json():
    tdm_data = {
        "tdm_reservation": 1,
        "tdm_policy": "https://example.com/policy.json",
    }
    m = iss.IsccMeta(tdm=tdm_data)
    j = m.json()
    assert '"tdm"' in j
    assert '"tdm_reservation":1' in j


def test_tdm_field_invalid_value():
    tdm_data = {"tdm_reservation": 3}
    with pytest.raises(ValidationError):
        iss.IsccMeta(tdm=tdm_data)


def test_tdm_field_partial():
    tdm_data = {"tdm_reservation": 1}
    m = iss.IsccMeta(tdm=tdm_data)
    d = m.dict()
    assert d["tdm"]["tdm_reservation"] == 1
    assert "tdm_policy" not in d["tdm"]


def test_tdm_reservation_zero():
    m = iss.IsccMeta(tdm={"tdm_reservation": 0})
    d = m.dict()
    assert d["tdm"]["tdm_reservation"] == 0


def test_tdm_field_optional():
    m = iss.IsccMeta()
    assert m.tdm is None


def test_tdm_backward_compat_v050():
    tdm_data = {"train": "reserved", "inference": "open"}
    m = iss.IsccMeta(tdm=tdm_data)
    d = m.dict()
    assert d["tdm"]["train"] == "reserved"
    assert d["tdm"]["inference"] == "open"
