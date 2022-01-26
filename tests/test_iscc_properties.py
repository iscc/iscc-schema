# -*- coding: utf-8 -*-
import pytest
import base64
from pydantic import ValidationError

from iscc_schema.schema import IsccNft


def test_iscc_properties_base64():
    b64 = base64.b64encode(b"Hello!")
    ip = IsccNft(properties=b64)
    assert ip.dict(exclude_unset=True) == {"properties": "SGVsbG8h"}


def test_iscc_properties_object():
    obj = IsccNft(properties={"any": "kind", "off": 64.43, "object": True})
    assert obj.dict(exclude_unset=True) == {
        "properties": {"any": "kind", "object": True, "off": 64.43}
    }


def test_iscc_properties_raises():
    with pytest.raises(ValidationError):
        IsccNft(properties="Hello!")
