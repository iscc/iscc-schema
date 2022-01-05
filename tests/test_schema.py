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


def test_pydantic_model_full_iscc():
    obj = iscc_schema.ISCC(iscc="ISCC:KID6X6GUH5F5GAXO2AUKQLUQFCUC4LNBCROR3QEP26N2PEOYVTDO2OY")
    assert obj.iscc == "ISCC:KID6X6GUH5F5GAXO2AUKQLUQFCUC4LNBCROR3QEP26N2PEOYVTDO2OY"


def test_pydantic_model_iscc_to_short_raises():
    with pytest.raises(ValueError):
        iscc_schema.ISCC(iscc="ISCC:EIAGUJFCE")


def test_pydantic_model_iscc_to_long_raises():
    with pytest.raises(ValueError):
        iscc_schema.ISCC(iscc="ISCC:KID6X6GUH5F5GAXO2AUKQLUQFCUC4LNBCROR3QEP26N2PEOYVTDO2OYK")


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
