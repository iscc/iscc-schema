# -*- coding: utf-8 -*-
from iscc_schema import generator


def test_iscc_request():
    r = generator.IsccCodePostRequest(source_url="https://example.com")
    assert r.json(exclude_unset=True) == '{"source_url": "https://example.com"}'


def test_data_uri():
    durl = "data:application/json;charset=utf-8;base64,eyJleHRlbmRlZCI6Im1ldGFkYXRhIn0="
    r = generator.IsccCodePostRequest(meta=durl)
    assert r.meta == durl


def test_ipfs_uri():
    ipfs = "ipfs://f01551220b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
    r = generator.MediaEmbeddedMetadata(license=ipfs)
    assert r.license == ipfs
