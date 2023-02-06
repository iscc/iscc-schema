# -*- coding: utf-8 -*-
from iscc_schema import IsccMeta


def test_iscc_meta_empty():
    m = IsccMeta()
    assert m.iscc is None
    assert m == {}
    assert m.dict() == {}
    assert (
        m.json()
        == '{"@context": "http://purl.org/iscc/context", "@type": '
        '"CreativeWork", "$schema": "http://purl.org/iscc/schema"}'
    )
    assert (
        m.jcs()
        == b'{"$schema":"http://purl.org/iscc/schema","@context":"http://purl.'
        b'org/iscc/context","@type":"CreativeWork"}'
    )
