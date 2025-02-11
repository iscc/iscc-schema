# -*- coding: utf-8 -*-
from iscc_schema.schema import IsccMinimal as IsccMinimalV1
from iscc_schema.schema_v2 import IsccMinimal as IsccMinimalV2


def test_iscc_minimal_longest_v1():
    im = IsccMinimalV1(
        iscc="ISCC:KED572P4AOF5K6QXQA4T6OJD5UGX7UBPFW2TVQNTHBCKFRFCANCZARQ4K6NSFZQSH4GQ"
    )
    assert im.dict() == {
        "iscc": "ISCC:KED572P4AOF5K6QXQA4T6OJD5UGX7UBPFW2TVQNTHBCKFRFCANCZARQ4K6NSFZQSH4GQ"
    }


def test_iscc_minimal_longest_v2():
    im = IsccMinimalV2(
        iscc="ISCC:KAD7LOFDIKZG5M426IITP2XOZ2S6YR3C4YNQ25URPKITNUL2NXLHU3SKFW336BFNK6WQ"
    )
    assert im.dict() == {
        "iscc": "ISCC:KAD7LOFDIKZG5M426IITP2XOZ2S6YR3C4YNQ25URPKITNUL2NXLHU3SKFW336BFNK6WQ"
    }
