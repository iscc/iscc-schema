# -*- coding: utf-8 -*-
import pytest
import base64
from pydantic import ValidationError
from iscc_schema.schema import IsccBasic


def test_iscc_metadata_base64():
    b64 = base64.b64encode(b"Hello!")
    ip = IsccBasic(meta=b64)
    assert ip.dict(exclude_unset=True) == {"meta": "SGVsbG8h"}


def test_iscc_metadata_object():
    obj = IsccBasic(meta={"any": "kind", "off": 64.43, "object": True})
    assert obj.dict(exclude_unset=True) == {"meta": {"any": "kind", "object": True, "off": 64.43}}


def test_iscc_metadata_raises():
    with pytest.raises(ValidationError):
        IsccBasic(meta="Hello!")
