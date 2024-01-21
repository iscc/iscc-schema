# -*- coding: utf-8 -*-
import pytest

try:
    from pydantic.v1 import ValidationError
except ImportError:
    from pydantic import ValidationError

import iscc_schema as iss


def test_embeddable_non_uri():
    m = iss.IsccMeta.construct(license="Hello License")
    assert m.dict() == {"license": "Hello License"}
    with pytest.raises(ValidationError):
        iss.IsccMeta(license="Hello License")
