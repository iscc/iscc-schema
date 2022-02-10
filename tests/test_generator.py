# -*- coding: utf-8 -*-
from iscc_schema import generator


def test_iscc_request():
    r = generator.IsccRequest(source_url="https://example.com")
    assert r.json(exclude_unset=True) == '{"source_url": "https://example.com"}'
