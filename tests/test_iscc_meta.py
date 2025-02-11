# -*- coding: utf-8 -*-
from iscc_schema import IsccMeta as IsccMetaV1
from iscc_schema.schema_v2 import IsccMeta as IsccMetaV2


def test_iscc_meta_empty_v1():
    m = IsccMetaV1()
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


def test_iscc_meta_empty_v2():
    m = IsccMetaV2()
    assert m.iscc is None
    # TODO Check if we can keep it compatible with v1
    # assert m == {}
    assert m.dict() == {}
    assert (
        m.json()
        == '{"@context":"http://purl.org/iscc/context","@type":'
        '"CreativeWork","$schema":"http://purl.org/iscc/schema"}'
    )
    assert (
        m.jcs()
        == b'{"$schema":"http://purl.org/iscc/schema","@context":"http://purl.'
        b'org/iscc/context","@type":"CreativeWork"}'
    )
