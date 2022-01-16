# -*- coding: utf-8 -*-
import pytest
from iscc_schema.schema import IsccMinimal


def test_iscc_minimal_longest():
    im = IsccMinimal(
        iscc="ISCC:KAD7LOFDIKZG5M426IITP2XOZ2S6YR3C4YNQ25URPKITNUL2NXLHU3SKFW336BFNK6WQ"
    )
    assert im.dict() == {
        "iscc": "ISCC:KAD7LOFDIKZG5M426IITP2XOZ2S6YR3C4YNQ25URPKITNUL2NXLHU3SKFW336BFNK6WQ"
    }
