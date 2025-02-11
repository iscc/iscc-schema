# -*- coding: utf-8 -*-
from iscc_schema.schema import IsccBasic as IsccBasicV1
from iscc_schema.schema_v2 import IsccBasic as IsccBasicV2


def test_iscc_meta_data_url_v1():
    ip = IsccBasicV1(
        meta="data:application/json;charset=utf-8;base64,eyJleHRlbmRlZCI6Im1ldGFkYXRhIn0="
    )
    assert ip.dict(exclude_unset=True) == {
        "meta": "data:application/json;charset=utf-8;base64,eyJleHRlbmRlZCI6Im1ldGFkYXRhIn0="
    }


def test_iscc_meta_data_url_v2():
    ip = IsccBasicV2(
        meta="data:application/json;charset=utf-8;base64,eyJleHRlbmRlZCI6Im1ldGFkYXRhIn0="
    )
    assert ip.dict(exclude_unset=True) == {
        "meta": "data:application/json;charset=utf-8;base64,eyJleHRlbmRlZCI6Im1ldGFkYXRhIn0="
    }
