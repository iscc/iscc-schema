# -*- coding: utf-8 -*-
import pytest
from pydantic.v1 import ValidationError as ValidationErrorV1
from pydantic import ValidationError as ValidationErrorV2
from iscc_schema.schema import IsccMeta as IsccMetaV1
from iscc_schema.schema_v2 import IsccMeta as IsccMetaV2


def test_embeddable_non_uri_v1():
    m = IsccMetaV1.construct(license="Hello License")
    assert m.dict() == {"license": "Hello License"}
    with pytest.raises(ValidationErrorV1):
        IsccMetaV1(license="Hello License")


def test_embeddable_non_uri_v2():
    m = IsccMetaV2.construct(license="Hello License")
    assert m.dict() == {"license": "Hello License"}
    with pytest.raises(ValidationErrorV2):
        IsccMetaV2(license="Hello License")
