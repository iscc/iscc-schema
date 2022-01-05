# -*- coding: utf-8 -*-
import pytest
import iscc_schema
from pyld import jsonld


def test_schema():
    so = iscc_schema.ISCC(iscc="ISCC:EIAGUJFCEY")
    assert so.dict(exclude_none=True, by_alias=True) == {
        "@context": "https://purl.org/iscc/terms/",
        "$schema": "https://purl.org/iscc/schema/",
        "iscc": "ISCC:EIAGUJFCEY",
    }


def test_iscc_regex_validation():
    with pytest.raises(ValueError):
        iscc_schema.ISCC(iscc="ISCC:EIAGUJFCE")


def test_json_ld_normalize():
    so = iscc_schema.ISCC(iscc="ISCC:EIAGUJFCEY")
    so.context_ = "http://schema.iscc.codes/context/isccmeta.jsonld"
    data = so.dict(exclude_none=True, by_alias=True)
    assert data == {
        "@context": "http://schema.iscc.codes/context/isccmeta.jsonld",
        "$schema": "https://purl.org/iscc/schema/",
        "iscc": "ISCC:EIAGUJFCEY",
    }

    # jsonld.set_document_loader(jsonld.requests_document_loader(timeout=10))

    # norm = jsonld.normalize(data, {"algorithm": "URDNA2015", "format": "application/n-quads"})
    # assert norm == ""
