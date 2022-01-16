# -*- coding: utf-8 -*-
import pytest
import base64
from pydantic import ValidationError

from iscc_schema.schema import IsccProperties


def test_iscc_properties_base64():
    b64 = base64.b64encode(b"Hello!")
    ip = IsccProperties(properties=b64)
    assert ip.dict() == {"properties": "SGVsbG8h"}


def test_iscc_properties_object():
    obj = IsccProperties(properties={"any": "kind", "off": 64.43, "object": True})
    assert obj.dict() == {"properties": {"any": "kind", "object": True, "off": 64.43}}


def test_iscc_properties_raises():
    with pytest.raises(ValidationError):
        IsccProperties(properties="Hello!")
