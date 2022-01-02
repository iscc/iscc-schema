# -*- coding: utf-8 -*-
import iscc_schema


def test_schema():
    so = iscc_schema.ISCC(iscc="ISCC:EIAGUJFCEY")
    assert so.dict(exclude_none=True, by_alias=True) == {
        "@context": "https://purl.org/iscc/context/iscc.json",
        "$schema": "https://purl.org/iscc/schema/iscc.json",
        "iscc": "ISCC:EIAGUJFCEY",
    }
