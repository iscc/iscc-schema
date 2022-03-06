# -*- coding: utf-8 -*-
import pytest
import iscc_schema as ics


def test_schema():
    so = ics.IsccMeta(iscc="ISCC:EIAGUJFCEY")
    assert so.dict(exclude_none=True, by_alias=True) == {
        "@context": f"http://purl.org/iscc/context/{ics.__version__}.jsonld",
        "@type": "CreativeWork",
        "$schema": f"http://purl.org/iscc/schema/{ics.__version__}.json",
        "iscc": "ISCC:EIAGUJFCEY",
    }


def test_pydantic_model_full_iscc():
    obj = ics.IsccMeta(iscc="ISCC:KID6X6GUH5F5GAXO2AUKQLUQFCUC4LNBCROR3QEP26N2PEOYVTDO2OY")
    assert obj.iscc == "ISCC:KID6X6GUH5F5GAXO2AUKQLUQFCUC4LNBCROR3QEP26N2PEOYVTDO2OY"


def test_pydantic_model_iscc_to_short_raises():
    with pytest.raises(ValueError):
        ics.IsccMeta(iscc="ISCC:EIAGUJFCE")


def test_pydantic_model_iscc_to_long_raises():
    with pytest.raises(ValueError):
        ics.IsccMeta(
            iscc="ISCC:KAD7LOFDIKZG5M426IITP2XOZ2S6YR3C4YNQ25URPKITNUL2NXLHU3SKFW336BFNK6WQ6"
        )


# def test_json_ld_normalize():
#     so = schema.ISCC(iscc="ISCC:EIAGUJFCEY")
#     data = so.dict(exclude_none=True, by_alias=True)
#     assert data == {
#         "@context": "http://purl.org/iscc/context",
#         "@type": "CreativeWork",
#         "$schema": "http://purl.org/iscc/schema",
#         "iscc": "ISCC:EIAGUJFCEY",
#     }
#
#     norm = jsonld.normalize(data, {"algorithm": "URDNA2015", "format": "application/n-quads"})
#     assert norm == (
#         "<ISCC:EIAGUJFCEY> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/CreativeWork> .\n"
#     )
