"""Build docs/context/<v>.json JSON-LD file from ISCC schemas."""

from typing import Dict
import pathlib
import subprocess

import yaml
import iscc_schema.schema
from os.path import dirname, abspath, join
import json

HERE = dirname(abspath(__file__))
ROOT = pathlib.Path(__file__).parent.parent
MODELS = ROOT / "iscc_schema" / "models"
SEED_SCHEMAS = [MODELS / "isbn.yaml", MODELS / "isrc.yaml", MODELS / "stm.yaml"]
SERVICE_SCHEMAS = [
    MODELS / "tdm.yaml",
    MODELS / "genai.yaml",
    MODELS / "identifiers.yaml",
]
PROTOCOL_SCHEMAS = [MODELS / "iscc-note.yaml"]
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
            "STM": "http://purl.org/iscc/terms/#STM",
            "TDM": "http://purl.org/iscc/terms/#TDM",
            "GenAI": "http://purl.org/iscc/terms/#GenAI",
            "Identifiers": "http://purl.org/iscc/terms/#Identifiers",
            "IsccNote": "http://purl.org/iscc/terms/#IsccNote",
        }
    }
    ctx = context["@context"]
    schema = iscc_schema.IsccMeta.model_json_schema()
    for prop, fields in schema["properties"].items():
        if "x-iscc-context" in fields and prop != "iscc":
            iri = fields["x-iscc-context"]
            if _is_uri_field(fields):
                ctx[prop] = {"@id": iri, "@type": "@id"}
            else:
                ctx[prop] = iri
    _add_enum_iri_mappings(ctx, schema)
    for seed_path in SEED_SCHEMAS:
        _add_schema_terms(ctx, seed_path)
    for service_path in SERVICE_SCHEMAS:
        _add_schema_terms(ctx, service_path)
    for protocol_path in PROTOCOL_SCHEMAS:
        _add_schema_terms(ctx, protocol_path)
    return context


def _add_schema_terms(ctx, yaml_path):
    # type: (dict, pathlib.Path) -> None
    """Add terms from a standalone YAML schema to the JSON-LD context."""
    with open(yaml_path, encoding="utf-8") as f:
        schema = yaml.safe_load(f)

    def iter_context_fields(properties):
        # type: (dict) -> object
        """Yield top-level and explicitly mapped nested property definitions."""
        for prop, fields in properties.items():
            yield prop, fields
            candidates = []
            if fields.get("type") == "object":
                candidates.append(fields)
            items = fields.get("items")
            if isinstance(items, dict):
                candidates.append(items)
            for candidate in candidates:
                for nested_prop, nested_fields in candidate.get("properties", {}).items():
                    if "x-iscc-context" in nested_fields:
                        yield nested_prop, nested_fields

    for prop, fields in iter_context_fields(schema.get("properties", {})):
        if "x-iscc-context" not in fields:
            continue
        iri = fields["x-iscc-context"]
        enum_ctx = fields.get("x-iscc-enum-context")
        if enum_ctx:
            # Enum-valued field: coerce values to IRIs and map each token to its class IRI.
            # setdefault keeps any existing mapping (shared tokens reuse the schema.org IRI).
            if prop not in ctx:
                ctx[prop] = {"@id": iri, "@type": "@id"}
            for token, token_iri in enum_ctx.items():
                ctx.setdefault(token, token_iri)
        elif prop not in ctx:
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


def _add_enum_iri_mappings(ctx, schema):
    # type: (dict, dict) -> None
    """Add IRI mappings for form enum values so they resolve to Schema.org IRIs."""
    form_def = schema.get("$defs", {}).get("Form", {})
    for value in form_def.get("enum", []):
        if value not in ctx:
            ctx[value] = f"http://schema.org/{value}"


def build_latest():
    """Build `iscc.json` JSON-LD context"""
    with open(PATH_LATEST, "wt", encoding="utf-8", newline="\n") as outf:
        outf.write(json.dumps(build_context(), indent=2, ensure_ascii=False))


def build_version():
    """Build `<x.x.x>.json` JSON-LD context"""
    with open(PATH_VERSION, "wt", encoding="utf-8", newline="\n") as outf:
        outf.write(json.dumps(build_context(), indent=2, ensure_ascii=False))


def _check_version_not_released(version):
    # type: (str) -> None
    """Abort the build if the current version is already released (a `v{version}` git tag exists).

    Versioned archive files are immutable once released; overwriting them from a branch that
    forgot to bump the version would silently mutate published artifacts. Local tags mirror the
    GitHub releases after a fetch/pull, so this is equivalent to checking the remote without a
    network call. If git is unavailable the check is skipped (fail-open); the bump-first rule
    and tests/test_versioning.py remain as backstops.
    """
    try:
        result = subprocess.run(["git", "tag", "-l", f"v{version}"], capture_output=True, text=True)
    except OSError:
        return
    if result.stdout.strip():
        raise SystemExit(
            f"ERROR: Version {version} has already been released (tag v{version} exists). "
            "Bump the version in pyproject.toml and iscc_schema/__init__.py before running "
            "the build pipeline."
        )


def build():
    """Build `iscc.json` & `<x.x.x>.json` JSON-LD context"""
    _check_version_not_released(iscc_schema.__version__)
    build_latest()
    build_version()


if __name__ == "__main__":
    build()
