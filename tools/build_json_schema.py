"""Build JSON Schema by auto-flattening individual YAML schema files."""

import json
import pathlib
import yaml
import iscc_schema

ROOT = pathlib.Path(__file__).parent.parent
MODELS = ROOT / "iscc_schema" / "models"
COMPOSITION = MODELS / "iscc-all.yaml"
PATH_LATEST = ROOT / "docs" / "schema" / "iscc.json"
PATH_VERSION = ROOT / "docs" / "schema" / f"{iscc_schema.__version__}.json"

# Versioned URL overrides (individual schemas use unversioned URLs by design)
VERSION_OVERRIDES = {
    "@context": {"default": f"http://purl.org/iscc/context/{iscc_schema.__version__}.jsonld"},
    "$schema": {"default": f"http://purl.org/iscc/schema/{iscc_schema.__version__}.json"},
}


def flatten_schemas():
    # type: () -> dict
    """Load individual schemas referenced by iscc-all.yaml and merge into flat JSON Schema."""
    with open(COMPOSITION, encoding="utf-8") as f:
        composition = yaml.safe_load(f)

    merged_properties = {}
    for ref_entry in composition["allOf"]:
        ref_path = MODELS / ref_entry["$ref"]
        with open(ref_path, encoding="utf-8") as f:
            schema = yaml.safe_load(f)
        for prop_name, prop_def in schema.get("properties", {}).items():
            merged_properties[prop_name] = prop_def

    for prop_name, overrides in VERSION_OVERRIDES.items():
        if prop_name in merged_properties:
            merged_properties[prop_name].update(overrides)

    # Order properties for readability (jsonld first, then by importance)
    ordered = {}
    priority = [
        "@context",
        "@type",
        "$schema",
        "iscc",
        "iscc_id",
        "iscc_code",
        "name",
        "description",
        "meta",
        "mode",
        "creator",
        "license",
        "acquire",
        "credit",
        "rights",
        "original",
        "credentials",
        "verifications",
        "media_id",
        "image",
        "identifier",
        "content",
        "keywords",
        "redirect",
        "previous",
        "version",
        "created",
        "filename",
        "filesize",
        "mediatype",
        "duration",
        "fps",
        "width",
        "height",
        "characters",
        "pages",
        "language",
        "parts",
        "part_of",
        "features",
        "units",
        "generator",
        "text",
        "external_url",
        "animation_url",
        "properties",
        "attributes",
        "nft",
        "tophash",
        "metahash",
        "datahash",
        "nonce",
        "signature",
        "chain",
        "wallet",
        "thumbnail",
    ]
    for key in priority:
        if key in merged_properties:
            ordered[key] = merged_properties.pop(key)
    ordered.update(merged_properties)

    return {
        "title": "iscc-collection",
        "type": "object",
        "description": "Collection of all ISCC Metadata fields",
        "examples": [{"iscc": "ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY"}],
        "properties": ordered,
    }


SEED_SCHEMAS = ["isbn.yaml", "isrc.yaml"]
SERVICE_SCHEMAS = ["tdm.yaml"]


def build_seed_schema(yaml_file):
    # type: (str) -> None
    """Build a standalone JSON Schema file for a seed metadata definition."""
    path = MODELS / yaml_file
    with open(path, encoding="utf-8") as f:
        schema = yaml.safe_load(f)

    name = yaml_file.replace(".yaml", "")
    output = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": f"http://purl.org/iscc/schema/{name}.json",
        "title": schema["title"],
        "type": "object",
        "description": schema["description"],
        "required": schema.get("required", []),
        "properties": schema.get("properties", {}),
    }
    if schema.get("examples"):
        output["examples"] = schema["examples"]

    outpath = ROOT / "docs" / "schema" / f"{name}.json"
    with open(outpath, "wt", encoding="utf-8", newline="\n") as outf:
        outf.write(json.dumps(output, indent=2, ensure_ascii=False))


def build():
    # type: () -> None
    """Build `iscc.json` & `<version>.json` schema, plus seed metadata schemas."""
    data = flatten_schemas()
    for path in (PATH_LATEST, PATH_VERSION):
        with open(path, "wt", encoding="utf-8", newline="\n") as outf:
            outf.write(json.dumps(data, indent=2, ensure_ascii=False))
    for yaml_file in SEED_SCHEMAS + SERVICE_SCHEMAS:
        build_seed_schema(yaml_file)


if __name__ == "__main__":
    build()
