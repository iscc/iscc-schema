# -*- coding: utf-8 -*-
import pytest
from pydantic import ValidationError

import iscc_schema as iss

V = iss.__version__
SCHEMA_URL = f"http://purl.org/iscc/schema/{V}.json"
CONTEXT_URL = f"http://purl.org/iscc/context/{V}.jsonld"


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
    with pytest.raises(ValidationError):
        obj.license = "https://in valid.com"


def test_validate_uri_ipfs():
    assert iss.IsccMeta(license="ipfs://some")


def test_json():
    assert (
        iss.IsccMeta().json()
        == f'{{"@context":"{CONTEXT_URL}","@type":"CreativeWork","$schema":"{SCHEMA_URL}"}}'
    )


def test_jcs():
    assert iss.IsccMeta().jcs() == (
        f'{{"$schema":"{SCHEMA_URL}","@context":"{CONTEXT_URL}","@type":"CreativeWork"}}'
    ).encode("utf-8")


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
        "@context": CONTEXT_URL,
        "@type": "CreativeWork",
        "$schema": SCHEMA_URL,
        "iscc": "ISCC:EIAGUJFCEY",
    }


def test_pydantic_model_full_iscc():
    obj = iss.IsccMeta(iscc="ISCC:KID6X6GUH5F5GAXO2AUKQLUQFCUC4LNBCROR3QEP26N2PEOYVTDO2OY")
    assert obj.iscc == "ISCC:KID6X6GUH5F5GAXO2AUKQLUQFCUC4LNBCROR3QEP26N2PEOYVTDO2OY"


def test_pydantic_model_iscc_to_short_raises():
    with pytest.raises(ValidationError):
        iss.IsccMeta(iscc="ISCC:EIAGUJFCE")


def test_pydantic_model_iscc_to_long_raises():
    with pytest.raises(ValidationError):
        iss.IsccMeta(
            iscc="ISCC:KAD7LOFDIKZG5M426IITP2XOZ2S6YR3C4YNQ25URPKITNUL2NXLHU3SKFW336BFNK6WQ6"
        )


def test_identifier_string():
    assert iss.IsccMeta(identifier="some-id").dict() == {"identifier": "some-id"}


def test_identifier_list():
    assert iss.IsccMeta(identifier=["some-id", "other-id"]).dict() == {
        "identifier": ["some-id", "other-id"]
    }


def test_form_field():
    """Test that form field accepts valid Schema.org CreativeWork subtypes."""
    meta = iss.IsccMeta(form="ScholarlyArticle")
    assert meta.form == "ScholarlyArticle"


def test_form_field_optional():
    """Test that form field is optional and absent by default."""
    meta = iss.IsccMeta()
    data = meta.dict()
    assert "form" not in data


def test_form_field_enum_validation():
    """Test that form field rejects invalid values."""
    with pytest.raises(ValidationError):
        iss.IsccMeta(form="InvalidType")


def test_form_with_type():
    """Test form alongside @type — both can coexist."""
    meta = iss.IsccMeta(type_="TextDigitalDocument", form="ScholarlyArticle")
    data = meta.dict()
    assert data["@type"] == "TextDigitalDocument"
    assert data["form"] == "ScholarlyArticle"


def test_forbid_extra_fields():
    with pytest.raises(ValidationError):
        iss.IsccMeta(
            iscc="ISCC:KID6X6GUH5F5GAXO2AUKQLUQFCUC4LNBCROR3QEP26N2PEOYVTDO2OY",
            other="other",
        )
