# -*- coding: utf-8 -*-
import pytest
from pydantic import ValidationError
import iscc_schema
from iscc_schema.seed_isrc import ISRC

CONTEXT_URL = f"http://purl.org/iscc/context/{iscc_schema.__version__}.jsonld"

VALID_ISRC_DATA = {
    "isrc": "AA6Q72000047",
    "main_artist": "The Beatles",
    "track_title": "Yesterday",
    "version_title": "Remastered 2009",
    "duration": 125,
    "content_type": "sound",
    "pubdate": "20090909",
}


def test_valid_construction():
    obj = ISRC(**VALID_ISRC_DATA)
    assert obj.isrc == "AA6Q72000047"
    assert obj.main_artist == "The Beatles"
    assert obj.track_title == "Yesterday"
    assert obj.duration == 125


def test_defaults():
    obj = ISRC(**VALID_ISRC_DATA)
    assert obj.context_ == CONTEXT_URL
    assert obj.type_ == "ISRC"
    assert obj.schema_ == "http://purl.org/iscc/schema/isrc.json"


def test_content_type_enum():
    obj = ISRC(**VALID_ISRC_DATA)
    assert obj.content_type == "sound"

    data = {**VALID_ISRC_DATA, "content_type": "video"}
    obj2 = ISRC(**data)
    assert obj2.content_type == "video"


def test_content_type_invalid():
    data = {**VALID_ISRC_DATA, "content_type": "text"}
    with pytest.raises(ValidationError):
        ISRC(**data)


def test_dict():
    obj = ISRC(**VALID_ISRC_DATA)
    d = obj.dict()
    assert d["isrc"] == "AA6Q72000047"
    assert d["duration"] == 125
    assert d["content_type"] == "sound"


def test_dict_with_defaults():
    obj = ISRC(**VALID_ISRC_DATA)
    d = obj.dict(exclude_unset=False)
    assert d["@context"] == CONTEXT_URL
    assert d["@type"] == "ISRC"
    assert d["$schema"] == "http://purl.org/iscc/schema/isrc.json"
    assert d["isrc"] == "AA6Q72000047"
    assert d["duration"] == 125
    assert d["content_type"] == "sound"


def test_json():
    obj = ISRC(**VALID_ISRC_DATA)
    j = obj.json()
    assert '"@type":"ISRC"' in j
    assert '"isrc":"AA6Q72000047"' in j
    assert '"duration":125' in j


def test_jcs():
    obj = ISRC(**VALID_ISRC_DATA)
    result = obj.jcs()
    assert isinstance(result, bytes)
    assert b'"isrc":"AA6Q72000047"' in result


def test_missing_required_isrc():
    data = {k: v for k, v in VALID_ISRC_DATA.items() if k != "isrc"}
    with pytest.raises(ValidationError):
        ISRC(**data)


def test_missing_required_main_artist():
    data = {k: v for k, v in VALID_ISRC_DATA.items() if k != "main_artist"}
    with pytest.raises(ValidationError):
        ISRC(**data)


def test_invalid_isrc_pattern():
    data = {**VALID_ISRC_DATA, "isrc": "invalid"}
    with pytest.raises(ValidationError):
        ISRC(**data)


def test_invalid_pubdate_pattern():
    data = {**VALID_ISRC_DATA, "pubdate": "2009-09-09"}
    with pytest.raises(ValidationError):
        ISRC(**data)


def test_duration_must_be_integer():
    data = {**VALID_ISRC_DATA, "duration": "125"}
    obj = ISRC(**data)
    assert obj.duration == 125


def test_extra_fields_forbidden():
    data = {**VALID_ISRC_DATA, "extra": "value"}
    with pytest.raises(ValidationError):
        ISRC(**data)


def test_import_from_package():
    from iscc_schema import ISRC as ISRCFromPkg

    obj = ISRCFromPkg(**VALID_ISRC_DATA)
    assert obj.isrc == "AA6Q72000047"
