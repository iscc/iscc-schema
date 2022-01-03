"""Build docs/context/<v>.json JSON-LD file from iscc_core.schema"""
from typing import Dict

import iscc_schema
from os.path import dirname, abspath, join
import json

HERE = dirname(abspath(__file__))
PATH_LATEST = join(HERE, f"../docs/context/iscc.json")
PATH_VERSION = join(HERE, f"../docs/context/{iscc_schema.__version__}.json")


def build_context():
    # type: () -> Dict
    """
    Build JSON-LD context from ISCC pydantic model for publishing

    :return: Serialized JSON-LD context for publishing.
    :rtype: Dict
    """
    context = {
        "@context": [
            "https://schema.org/docs/jsonldcontext.jsonld",
            {
                "§schema": "@type",
                "iscc": "@id",
            },
        ]
    }
    ctx = context["@context"][1]
    for prop, fields in iscc_schema.ISCC.schema()["properties"].items():
        if "x_iscc_context" in fields:
            ctx[prop] = fields["x_iscc_context"]
    return context


def build_latest():
    """Build `iscc.json` JSON-LD context"""
    with open(PATH_LATEST, "wt", encoding="UTF-8") as outf:
        outf.write(json.dumps(build_context(), indent=2, ensure_ascii=False))


def build_version():
    """Build `<x.x.x>.json` JSON-LD context"""
    with open(PATH_VERSION, "wt", encoding="UTF-8") as outf:
        outf.write(json.dumps(build_context(), indent=2, ensure_ascii=False))


def build():
    """Build `iscc.json` & `<x.x.x>.json` JSON-LD context"""
    build_latest()
    build_version()


if __name__ == "__main__":
    build()
