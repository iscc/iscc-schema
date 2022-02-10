"""Build docs/context/<v>.json JSON-LD file from iscc_core.schema"""
from typing import Dict

import iscc_schema.schema
from os.path import dirname, abspath, join
import json

HERE = dirname(abspath(__file__))
PATH_LATEST = join(HERE, f"../docs/context/iscc.jsonld")
PATH_VERSION = join(HERE, f"../docs/context/{iscc_schema.__version__}.jsonld")


def build_context():
    # type: () -> Dict
    """
    Build JSON-LD context from ISCC pydantic model for publishing

    TODO: build directly from OpenAPI definitions instead of pydantic schema.

    :return: Serialized JSON-LD context for publishing.
    :rtype: Dict
    """
    context = {
        "@context": {
            "iscc": "@id",
            "CreativeWork": "http://schema.org/CreativeWork",
            "TextDigitalDocument": "http://schema.org/TextDigitalDocument",
            "ImageObject": "http://schema.org/ImageObject",
            "AudioObject": "http://schema.org/AudioObject",
            "VideoObject": "http://schema.org/VideoObject",
        }
    }
    ctx = context["@context"]
    for prop, fields in iscc_schema.schema.ISCC.schema()["properties"].items():
        if "x_iscc_context" in fields:
            ctx[prop] = fields["x_iscc_context"]
    return context


def build_latest():
    """Build `iscc.json` JSON-LD context"""
    with open(PATH_LATEST, "wt", encoding="utf-8", newline="\n") as outf:
        outf.write(json.dumps(build_context(), indent=2, ensure_ascii=False))


def build_version():
    """Build `<x.x.x>.json` JSON-LD context"""
    with open(PATH_VERSION, "wt", encoding="utf-8", newline="\n") as outf:
        outf.write(json.dumps(build_context(), indent=2, ensure_ascii=False))


def build():
    """Build `iscc.json` & `<x.x.x>.json` JSON-LD context"""
    build_latest()
    build_version()


if __name__ == "__main__":
    build()
