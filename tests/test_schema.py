# -*- coding: utf-8 -*-
import pytest
import iscc_schema as iss


def test_empty():
    assert iss.IsccMeta().dict() == {}


def test_empty_str_to_none():
    empty = iss.IsccMeta(name="")
    assert empty.name is None
    assert empty.dict() == {}


def test_empty_url_to_none():
    empty = iss.IsccMeta(license="")
    assert empty.license is None
    assert empty.dict() == {}


def test_validate_assignment():
    obj = iss.IsccMeta()
    with pytest.raises(ValueError):
        obj.license = "https://in valid.com"


def test_validate_uri_ipfs():
    assert iss.IsccMeta(license="ipfs://some")


def test_json():
    assert (
        iss.IsccMeta().json() == "{"
        f'"@context": "http://purl.org/iscc/context/{iss.__version__}.jsonld", "@type": '
        f'"CreativeWork", "$schema": "http://purl.org/iscc/schema/{iss.__version__}.json"'
        "}"
    )


def test_jcs():
    assert iss.IsccMeta().jcs() == bytes(
        "{"
        f'"$schema":"http://purl.org/iscc/schema/{iss.__version__}.json","@context":"http://purl.'
        f'org/iscc/context/{iss.__version__}.jsonld","@type":"CreativeWork"'
        "}",
        encoding="utf-8",
    )


def test_jcs_big_int_raises():
    obj = iss.IsccMeta(duration=2**60)
    assert obj.dict() == {"duration": 1152921504606846976}
    with pytest.raises(ValueError):
        obj.jcs()


def test_iscc_obj_raises():
    obj = iss.IsccMeta()
    with pytest.raises(ImportError):
        assert obj.iscc_obj


def test_schema():
    so = iss.IsccMeta(iscc="ISCC:EIAGUJFCEY")
    assert so.dict(exclude_none=True, by_alias=True, exclude_unset=False) == {
        "@context": f"http://purl.org/iscc/context/{iss.__version__}.jsonld",
        "@type": "CreativeWork",
        "$schema": f"http://purl.org/iscc/schema/{iss.__version__}.json",
        "iscc": "ISCC:EIAGUJFCEY",
    }


def test_pydantic_model_full_iscc():
    obj = iss.IsccMeta(iscc="ISCC:KID6X6GUH5F5GAXO2AUKQLUQFCUC4LNBCROR3QEP26N2PEOYVTDO2OY")
    assert obj.iscc == "ISCC:KID6X6GUH5F5GAXO2AUKQLUQFCUC4LNBCROR3QEP26N2PEOYVTDO2OY"


def test_pydantic_model_iscc_to_short_raises():
    with pytest.raises(ValueError):
        iss.IsccMeta(iscc="ISCC:EIAGUJFCE")


def test_pydantic_model_iscc_to_long_raises():
    with pytest.raises(ValueError):
        iss.IsccMeta(
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
