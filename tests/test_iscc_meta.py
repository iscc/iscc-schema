# -*- coding: utf-8 -*-
import iscc_schema
from iscc_schema import IsccMeta

V = iscc_schema.__version__
SCHEMA_URL = f"http://purl.org/iscc/schema/{V}.json"
CONTEXT_URL = f"http://purl.org/iscc/context/{V}.jsonld"


def test_iscc_meta_empty():
    m = IsccMeta()
    assert m.iscc is None
    assert m.dict() == {}
    assert (
        m.json()
        == f'{{"@context":"{CONTEXT_URL}","@type":"CreativeWork","$schema":"{SCHEMA_URL}"}}'
    )
    assert (
        m.jcs()
        == f'{{"$schema":"{SCHEMA_URL}","@context":"{CONTEXT_URL}","@type":"CreativeWork"}}'.encode(
            "utf-8"
        )
    )
