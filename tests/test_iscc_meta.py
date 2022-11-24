# -*- coding: utf-8 -*-
from iscc_schema import IsccMeta


def test_iscc_meta_empty():
    m = IsccMeta()
    assert m.iscc is None
    assert m == {}
    assert m.dict() == {}
    assert m.json() == (
        '{"@context": "http://purl.org/iscc/context/0.4.0.jsonld", "@type": '
        '"CreativeWork", "$schema": "http://purl.org/iscc/schema/0.4.0.json"}'
    )
    assert m.jcs() == (
        b'{"$schema":"http://purl.org/iscc/schema/0.4.0.json","@context":"http://purl.'
        b'org/iscc/context/0.4.0.jsonld","@type":"CreativeWork"}'
    )
