# -*- coding: utf-8 -*-
from iscc_schema.schema import IsccBasic


def test_iscc_meta_data_url():
    ip = IsccBasic(
        meta="data:application/json;charset=utf-8;base64,eyJleHRlbmRlZCI6Im1ldGFkYXRhIn0="
    )
    assert ip.dict(exclude_unset=True) == {
        "meta": "data:application/json;charset=utf-8;base64,eyJleHRlbmRlZCI6Im1ldGFkYXRhIn0="
    }
