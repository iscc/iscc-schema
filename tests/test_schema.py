# -*- coding: utf-8 -*-
import iscc_schema


def test_schema():
    so = iscc_schema.IsccMetadataSchema(iscc="ISCC:EIAGUJFCEY")
    assert so.dict(exclude_none=True, by_alias=True) == {
        "@context": "https://purl.org/iscc/context/0.2.0.json",
        "$schema": "https://purl.org/iscc/schema/0.2.0.json",
        "iscc": "ISCC:EIAGUJFCEY",
    }
