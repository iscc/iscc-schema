# -*- coding: utf-8 -*-
import pytest
from pydantic import ValidationError
from iscc_schema.seed_isbn import ISBN

VALID_ISBN_DATA = {
    "isbn": "9789295055124",
    "productform": "EA",
    "title": "The Never Ending Story",
    "language": "eng",
    "imprint": "Penguin Classics",
    "publisher": "Penguin Random House",
    "country": "US",
    "pubdate": "20240214",
}


def test_valid_construction():
    obj = ISBN(**VALID_ISBN_DATA)
    assert obj.isbn == "9789295055124"
    assert obj.title == "The Never Ending Story"
    assert obj.language == "eng"
    assert obj.country == "US"


def test_defaults():
    obj = ISBN(**VALID_ISBN_DATA)
    assert obj.context_ == "http://purl.org/iscc/context"
    assert obj.type_ == "ISBN"
    assert obj.schema_ == "http://purl.org/iscc/schema/isbn.json"


def test_dict():
    obj = ISBN(**VALID_ISBN_DATA)
    d = obj.dict()
    assert d["isbn"] == "9789295055124"
    assert d["title"] == "The Never Ending Story"


def test_dict_with_defaults():
    obj = ISBN(**VALID_ISBN_DATA)
    d = obj.dict(exclude_unset=False)
    assert d["@context"] == "http://purl.org/iscc/context"
    assert d["@type"] == "ISBN"
    assert d["$schema"] == "http://purl.org/iscc/schema/isbn.json"
    assert d["isbn"] == "9789295055124"
    assert d["title"] == "The Never Ending Story"


def test_json():
    obj = ISBN(**VALID_ISBN_DATA)
    j = obj.json()
    assert '"@context":"http://purl.org/iscc/context"' in j
    assert '"@type":"ISBN"' in j
    assert '"isbn":"9789295055124"' in j


def test_jcs():
    obj = ISBN(**VALID_ISBN_DATA)
    result = obj.jcs()
    assert isinstance(result, bytes)
    assert b'"isbn":"9789295055124"' in result
    assert b'"$schema"' in result


def test_missing_required_isbn():
    data = {k: v for k, v in VALID_ISBN_DATA.items() if k != "isbn"}
    with pytest.raises(ValidationError):
        ISBN(**data)


def test_missing_required_title():
    data = {k: v for k, v in VALID_ISBN_DATA.items() if k != "title"}
    with pytest.raises(ValidationError):
        ISBN(**data)


def test_invalid_isbn_pattern():
    data = {**VALID_ISBN_DATA, "isbn": "123"}
    with pytest.raises(ValidationError):
        ISBN(**data)


def test_invalid_language_pattern():
    data = {**VALID_ISBN_DATA, "language": "EN"}
    with pytest.raises(ValidationError):
        ISBN(**data)


def test_invalid_country_pattern():
    data = {**VALID_ISBN_DATA, "country": "us"}
    with pytest.raises(ValidationError):
        ISBN(**data)


def test_invalid_pubdate_pattern():
    data = {**VALID_ISBN_DATA, "pubdate": "2024-02-14"}
    with pytest.raises(ValidationError):
        ISBN(**data)


def test_invalid_productform_too_long():
    data = {**VALID_ISBN_DATA, "productform": "EAB"}
    with pytest.raises(ValidationError):
        ISBN(**data)


def test_extra_fields_forbidden():
    data = {**VALID_ISBN_DATA, "extra": "value"}
    with pytest.raises(ValidationError):
        ISBN(**data)


def test_import_from_package():
    from iscc_schema import ISBN as ISBNFromPkg

    obj = ISBNFromPkg(**VALID_ISBN_DATA)
    assert obj.isbn == "9789295055124"
