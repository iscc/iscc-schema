# -*- coding: utf-8 -*-
import pytest
from iscc_schema.schema import IsccMeta as IsccMetaV1
from iscc_schema.schema_v2 import IsccMeta as IsccMetaV2


def test_empty_v1():
    assert IsccMetaV1().dict() == {}


def test_empty_v2():
    assert IsccMetaV2().dict() == {}


def test_empty_str_to_none_v1():
    empty = IsccMetaV1(name="")
    assert empty.name is None
    assert empty.dict() == {}


def test_empty_str_to_none_v2():
    empty = IsccMetaV2(name="")
    assert empty.name is None
    assert empty.dict() == {}


def test_empty_url_to_none_v1():
    empty = IsccMetaV1(license="")
    assert empty.license is None
    assert empty.dict() == {}


def test_empty_url_to_none_v2():
    empty = IsccMetaV2(license="")
    assert empty.license is None
    assert empty.dict() == {}


def test_validate_assignment_v1():
    obj = IsccMetaV1()
    with pytest.raises(ValueError):
        obj.license = "https://in valid.com"


def test_validate_assignment_v2():
    obj = IsccMetaV2()
    with pytest.raises(ValueError):
        obj.license = "https://in valid.com"


def test_validate_uri_ipfs_v1():
    assert IsccMetaV1(license="ipfs://some")


def test_json_v1():
    assert (
        IsccMetaV1().json() == f"{{"
        f'"@context": "http://purl.org/iscc/context", "@type": '
        f'"CreativeWork", "$schema": "http://purl.org/iscc/schema"'
        f"}}"
    )


def test_jcs_v1():
    assert IsccMetaV1().jcs() == bytes(
        (
            f"{{"
            f'"$schema":"http://purl.org/iscc/schema","@context":"http://purl.'
            f'org/iscc/context","@type":"CreativeWork"'
            f"}}"
        ),
        encoding="utf-8",
    )


def test_jcs_big_int_raises_v1():
    obj = IsccMetaV1(duration=2**60)
    assert obj.dict() == {"duration": 1152921504606846976}
    with pytest.raises(ValueError):
        obj.jcs()


def test_iscc_obj_raises_v1():
    obj = IsccMetaV1()
    with pytest.raises(ImportError):
        assert obj.iscc_obj


def test_schema_v1():
    so = IsccMetaV1(iscc="ISCC:EIAGUJFCEY")
    assert so.dict(exclude_none=True, by_alias=True, exclude_unset=False) == {
        "@context": f"http://purl.org/iscc/context",
        "@type": "CreativeWork",
        "$schema": f"http://purl.org/iscc/schema",
        "iscc": "ISCC:EIAGUJFCEY",
    }


def test_pydantic_model_full_iscc_v1():
    obj = IsccMetaV1(iscc="ISCC:KID6X6GUH5F5GAXO2AUKQLUQFCUC4LNBCROR3QEP26N2PEOYVTDO2OY")
    assert obj.iscc == "ISCC:KID6X6GUH5F5GAXO2AUKQLUQFCUC4LNBCROR3QEP26N2PEOYVTDO2OY"


def test_pydantic_model_iscc_to_short_raises_v1():
    with pytest.raises(ValueError):
        IsccMetaV1(iscc="ISCC:EIAGUJFCE")


def test_pydantic_model_iscc_to_long_raises_v1():
    with pytest.raises(ValueError):
        IsccMetaV1(
            iscc="ISCC:KAD7LOFDIKZG5M426IITP2XOZ2S6YR3C4YNQ25URPKITNUL2NXLHU3SKFW336BFNK6WQ6"
        )


def test_identifier_string_v1():
    assert IsccMetaV1(identifier="some-id").dict() == {"identifier": "some-id"}


def test_identifier_list_v1():
    assert IsccMetaV1(identifier=["some-id", "other-id"]).dict() == {
        "identifier": ["some-id", "other-id"]
    }


def test_forbid_extra_fields_v1():
    from pydantic.v1 import ValidationError

    with pytest.raises(ValidationError):
        IsccMetaV1(
            iscc="ISCC:KID6X6GUH5F5GAXO2AUKQLUQFCUC4LNBCROR3QEP26N2PEOYVTDO2OY",
            other="other",
        )
