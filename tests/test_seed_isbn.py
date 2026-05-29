# -*- coding: utf-8 -*-
import json
import pathlib

import pytest
from pydantic import ValidationError
import iscc_schema
from iscc_schema.seed_isbn import ISBN

ROOT = pathlib.Path(__file__).parent.parent
CONTEXT_URL = f"http://purl.org/iscc/context/{iscc_schema.__version__}.jsonld"
SCHEMA_URL = f"http://purl.org/iscc/schema/isbn-{iscc_schema.__version__}.json"

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
    assert obj.context_ == CONTEXT_URL
    assert obj.type_ == "ISBN"
    assert obj.schema_ == SCHEMA_URL


def test_dict():
    obj = ISBN(**VALID_ISBN_DATA)
    d = obj.dict()
    assert d["isbn"] == "9789295055124"
    assert d["title"] == "The Never Ending Story"


def test_dict_compact():
    obj = ISBN(**VALID_ISBN_DATA)
    d = obj.dict()
    assert "$schema" in d
    assert "@context" not in d
    assert "@type" not in d


def test_dict_ld():
    obj = ISBN(**VALID_ISBN_DATA)
    d = obj.dict(exclude_unset=False, ld=True)
    assert d["@context"] == CONTEXT_URL
    assert d["@type"] == "ISBN"
    assert d["$schema"] == SCHEMA_URL
    assert d["isbn"] == "9789295055124"
    assert d["title"] == "The Never Ending Story"


def test_json_compact():
    obj = ISBN(**VALID_ISBN_DATA)
    j = obj.json()
    assert '"$schema"' in j
    assert '"@context"' not in j
    assert '"@type"' not in j
    assert '"isbn":"9789295055124"' in j


def test_json_ld():
    obj = ISBN(**VALID_ISBN_DATA)
    j = obj.json(ld=True)
    assert f'"@context":"{CONTEXT_URL}"' in j
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


def test_schema_has_jsonld_extension():
    """ISBN serializes compact by default, so its schema documents the JSON-LD upgrade
    path via a top-level x-iscc-jsonld extension pointing at the versioned context."""
    schema = json.loads((ROOT / "docs" / "schema" / "isbn.json").read_text(encoding="utf-8"))
    ext = schema["x-iscc-jsonld"]
    assert ext["context"] == CONTEXT_URL
    assert ext["type"] == "ISBN"
    assert "x-iscc-jsonld" in schema["properties"]["$schema"]["description"]


def test_schema_context_default_is_versioned():
    """The published JSON Schema pins the versioned @context default, matching the value the
    Pydantic model emits with ld=True."""
    schema = json.loads((ROOT / "docs" / "schema" / "isbn.json").read_text(encoding="utf-8"))
    assert schema["properties"]["@context"]["default"] == CONTEXT_URL
    assert ISBN(**VALID_ISBN_DATA).context_ == CONTEXT_URL


def test_latest_schema_const_is_versioned():
    """The latest schema file pins a version-specific $schema const while keeping an unversioned
    $id: records identify the exact schema version; the file is served at the 'latest' URL."""
    schema = json.loads((ROOT / "docs" / "schema" / "isbn.json").read_text(encoding="utf-8"))
    assert schema["properties"]["$schema"]["const"] == SCHEMA_URL
    assert schema["$id"] == "http://purl.org/iscc/schema/isbn.json"


def test_versioned_archive_exists():
    """A version-pinned archive is written alongside the latest schema; its $id and its $schema
    const both carry the version, so records validated against it pin the exact schema version."""
    archive = ROOT / "docs" / "schema" / f"isbn-{iscc_schema.__version__}.json"
    assert archive.exists()
    data = json.loads(archive.read_text(encoding="utf-8"))
    assert data["$id"] == SCHEMA_URL
    assert data["properties"]["$schema"]["const"] == SCHEMA_URL
