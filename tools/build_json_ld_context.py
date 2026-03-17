"""Build docs/context/<v>.json JSON-LD file from ISCC schemas."""

from typing import Dict
import pathlib

import yaml
import iscc_schema.schema
from os.path import dirname, abspath, join
import json

HERE = dirname(abspath(__file__))
ROOT = pathlib.Path(__file__).parent.parent
MODELS = ROOT / "iscc_schema" / "models"
SEED_SCHEMAS = [MODELS / "isbn.yaml", MODELS / "isrc.yaml"]
SERVICE_SCHEMAS = [MODELS / "tdm.yaml"]
PATH_LATEST = join(HERE, f"../docs/context/iscc.jsonld")
PATH_VERSION = join(HERE, f"../docs/context/{iscc_schema.__version__}.jsonld")


def build_context():
    # type: () -> Dict
    """Build JSON-LD context from ISCC schemas including seed metadata."""
    context = {
        "@context": {
            "iscc": "@id",
            "CreativeWork": "http://schema.org/CreativeWork",
            "TextDigitalDocument": "http://schema.org/TextDigitalDocument",
            "ImageObject": "http://schema.org/ImageObject",
            "AudioObject": "http://schema.org/AudioObject",
            "VideoObject": "http://schema.org/VideoObject",
            "ISBN": "http://purl.org/iscc/terms/#ISBN",
            "ISRC": "http://purl.org/iscc/terms/#ISRC",
            "TDM": "http://purl.org/iscc/terms/#TDM",
        }
    }
    ctx = context["@context"]
    for prop, fields in iscc_schema.IsccMeta.model_json_schema()["properties"].items():
        if "x-iscc-context" in fields and prop != "iscc":
            iri = fields["x-iscc-context"]
            if _is_uri_field(fields):
                ctx[prop] = {"@id": iri, "@type": "@id"}
            else:
                ctx[prop] = iri
    for seed_path in SEED_SCHEMAS:
        _add_schema_terms(ctx, seed_path)
    for service_path in SERVICE_SCHEMAS:
        _add_schema_terms(ctx, service_path)
    return context


def _add_schema_terms(ctx, yaml_path):
    # type: (dict, pathlib.Path) -> None
    """Add terms from a standalone YAML schema to the JSON-LD context."""
    with open(yaml_path, encoding="utf-8") as f:
        schema = yaml.safe_load(f)
    for prop, fields in schema.get("properties", {}).items():
        if "x-iscc-context" in fields and prop not in ctx:
            iri = fields["x-iscc-context"]
            if _is_uri_field(fields):
                ctx[prop] = {"@id": iri, "@type": "@id"}
            else:
                ctx[prop] = iri


def _is_uri_field(field_schema):
    # type: (dict) -> bool
    """Check if a JSON Schema field definition has format 'uri'."""
    if field_schema.get("format") == "uri":
        return True
    for variant in field_schema.get("anyOf", []):
        if variant.get("format") == "uri":
            return True
    return False


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
