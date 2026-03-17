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
        "train": "reserved",
        "inference": "open",
        "derive": "reserved",
        "search": "open",
        "analyze": "open",
    }
    m = iss.IsccMeta(tdm=tdm_data)
    d = m.dict()
    assert d["tdm"]["train"] == "reserved"
    assert d["tdm"]["inference"] == "open"
    assert d["tdm"]["derive"] == "reserved"
    assert d["tdm"]["search"] == "open"
    assert d["tdm"]["analyze"] == "open"


def test_tdm_field_json():
    tdm_data = {
        "train": "reserved",
        "inference": "open",
        "derive": "reserved",
        "search": "open",
        "analyze": "open",
    }
    m = iss.IsccMeta(tdm=tdm_data)
    j = m.json()
    assert '"tdm"' in j
    assert '"train":"reserved"' in j


def test_tdm_field_invalid_value():
    tdm_data = {
        "train": "blocked",
        "inference": "open",
        "derive": "reserved",
        "search": "open",
        "analyze": "open",
    }
    with pytest.raises(ValidationError):
        iss.IsccMeta(tdm=tdm_data)


def test_tdm_field_partial():
    tdm_data = {"train": "reserved"}
    m = iss.IsccMeta(tdm=tdm_data)
    d = m.dict()
    assert d["tdm"]["train"] == "reserved"
    assert "inference" not in d["tdm"]


def test_tdm_field_optional():
    m = iss.IsccMeta()
    assert m.tdm is None
