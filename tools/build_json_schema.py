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
PATH_CONTEXT = ROOT / "docs" / "context" / "iscc.jsonld"

# Versioned URL overrides (individual schemas use unversioned URLs by design)
VERSION_OVERRIDES = {
    "@context": {"default": f"http://purl.org/iscc/context/{iscc_schema.__version__}.jsonld"},
    "$schema": {"default": f"http://purl.org/iscc/schema/{iscc_schema.__version__}.json"},
}


def _load_full_context():
    # type: () -> dict
    """Load the full ISCC JSON-LD context from the pre-generated .jsonld file."""
    with open(PATH_CONTEXT, encoding="utf-8") as f:
        return json.load(f)["@context"]


def _is_uri_field(field_schema):
    # type: (dict) -> bool
    """Check if a JSON Schema field definition has format 'uri'."""
    if field_schema.get("format") == "uri":
        return True
    for variant in field_schema.get("anyOf", []):
        if variant.get("format") == "uri":
            return True
    return False


def _build_standalone_context(schema, full_context):
    # type: (dict, dict) -> dict
    """Build schema-specific @context from YAML properties and the full ISCC context."""
    ctx = {}
    type_name = schema.get("properties", {}).get("@type", {}).get("const")
    if type_name and type_name in full_context:
        ctx[type_name] = full_context[type_name]
    for prop_name, prop_def in schema.get("properties", {}).items():
        if prop_name in ("@context", "@type", "$schema"):
            continue
        if "x-iscc-context" not in prop_def:
            continue
        iri = prop_def["x-iscc-context"]
        if _is_uri_field(prop_def):
            ctx[prop_name] = {"@id": iri, "@type": "@id"}
        else:
            ctx[prop_name] = iri
    return ctx


def _patch_context_property(properties):
    # type: (dict) -> None
    """Patch @context property to accept both URI string and inline object (JSON-LD spec)."""
    if "@context" not in properties:
        return
    ctx_prop = properties["@context"]
    patched = {
        "oneOf": [
            {"type": "string", "format": "uri"},
            {"type": "object"},
        ],
    }
    for key in ("default", "description", "readOnly"):
        if key in ctx_prop:
            patched[key] = ctx_prop[key]
    properties["@context"] = patched


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

    _patch_context_property(merged_properties)

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
        "form",
        "creator",
        "license",
        "acquire",
        "credit",
        "rights",
        "tdm",
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

    full_context = _load_full_context()

    return {
        "@context": full_context,
        "title": "iscc-collection",
        "type": "object",
        "description": "Collection of all ISCC Metadata fields",
        "examples": [{"iscc": "ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY"}],
        "properties": ordered,
    }


SEED_SCHEMAS = ["isbn.yaml", "isrc.yaml"]
SERVICE_SCHEMAS = ["tdm.yaml"]


def build_seed_schema(yaml_file, full_context):
    # type: (str, dict) -> dict
    """Build a standalone JSON Schema file for a seed/service metadata definition.

    Returns the loaded YAML schema for context building.
    """
    path = MODELS / yaml_file
    with open(path, encoding="utf-8") as f:
        schema = yaml.safe_load(f)

    name = yaml_file.replace(".yaml", "")
    properties = dict(schema.get("properties", {}))
    _patch_context_property(properties)
    standalone_context = _build_standalone_context(schema, full_context)

    output = {"@context": standalone_context}
    output["$schema"] = "https://json-schema.org/draft/2020-12/schema"
    output["$id"] = f"http://purl.org/iscc/schema/{name}.json"
    output["title"] = schema["title"]
    output["type"] = "object"
    output["description"] = schema["description"]
    output["properties"] = properties
    if schema.get("required"):
        output["required"] = schema["required"]
    if "additionalProperties" in schema:
        output["additionalProperties"] = schema["additionalProperties"]
    if schema.get("examples"):
        output["examples"] = schema["examples"]

    outpath = ROOT / "docs" / "schema" / f"{name}.json"
    with open(outpath, "wt", encoding="utf-8", newline="\n") as outf:
        outf.write(json.dumps(output, indent=2, ensure_ascii=False))

    return schema


def _build_contexts_module(full_context, standalone_schemas):
    # type: (dict, dict[str, dict]) -> None
    """Generate iscc_schema/contexts.py with embedded context data for runtime recovery."""
    schema_iscc = "http://purl.org/iscc/schema"

    # Build standalone schema URLs and their contexts
    standalone_contexts = {}
    type_schemas = {}
    for yaml_file, schema in standalone_schemas.items():
        name = yaml_file.replace(".yaml", "")
        url = f"http://purl.org/iscc/schema/{name}.json"
        ctx = _build_standalone_context(schema, full_context)
        standalone_contexts[url] = ctx
        type_name = schema.get("properties", {}).get("@type", {}).get("const")
        if type_name:
            type_schemas[type_name] = url

    # Main schema type mappings
    main_schema = flatten_main_types()
    for type_name in main_schema:
        type_schemas[type_name] = schema_iscc

    # Format context dicts for source code
    lines = [
        '"""Generated JSON-LD context mappings for schema-driven context recovery.',
        "DO NOT EDIT MANUALLY. Auto-generated by tools/build_json_schema.py.",
        '"""',
        "",
    ]

    # Schema URL constants
    lines.append(f'SCHEMA_ISCC = "{schema_iscc}"')
    for yaml_file in sorted(standalone_schemas):
        name = yaml_file.replace(".yaml", "")
        const_name = f"SCHEMA_{name.upper()}"
        url = f"http://purl.org/iscc/schema/{name}.json"
        lines.append(f'{const_name} = "{url}"')
    lines.append("")

    # SCHEMA_CONTEXTS dict
    lines.append("SCHEMA_CONTEXTS = {")
    lines.append(f"    SCHEMA_ISCC: {_format_context(full_context)},")
    for yaml_file in sorted(standalone_schemas):
        name = yaml_file.replace(".yaml", "")
        const_name = f"SCHEMA_{name.upper()}"
        url = f"http://purl.org/iscc/schema/{name}.json"
        lines.append(f"    {const_name}: {_format_context(standalone_contexts[url])},")
    lines.append("}")
    lines.append("")

    # TYPE_SCHEMAS dict
    lines.append("TYPE_SCHEMAS = {")
    for type_name, schema_url in sorted(type_schemas.items()):
        if schema_url == schema_iscc:
            lines.append(f'    "{type_name}": SCHEMA_ISCC,')
        else:
            name = schema_url.split("/")[-1].replace(".json", "")
            const_name = f"SCHEMA_{name.upper()}"
            lines.append(f'    "{type_name}": {const_name},')
    lines.append("}")
    lines.append("")

    outpath = ROOT / "iscc_schema" / "contexts.py"
    with open(outpath, "wt", encoding="utf-8", newline="\n") as outf:
        outf.write("\n".join(lines))


def _format_context(ctx):
    # type: (dict) -> str
    """Format a context dict as a Python literal string."""
    return json.dumps(ctx, ensure_ascii=False)


def flatten_main_types():
    # type: () -> list[str]
    """Extract @type enum values from the main ISCC schema composition."""
    with open(COMPOSITION, encoding="utf-8") as f:
        composition = yaml.safe_load(f)
    for ref_entry in composition["allOf"]:
        ref_path = MODELS / ref_entry["$ref"]
        with open(ref_path, encoding="utf-8") as f:
            schema = yaml.safe_load(f)
        type_prop = schema.get("properties", {}).get("@type", {})
        if "enum" in type_prop:
            return type_prop["enum"]
    return []


def build():
    # type: () -> None
    """Build `iscc.json` & `<version>.json` schema, plus seed/service metadata schemas."""
    full_context = _load_full_context()

    data = flatten_schemas()
    for path in (PATH_LATEST, PATH_VERSION):
        with open(path, "wt", encoding="utf-8", newline="\n") as outf:
            outf.write(json.dumps(data, indent=2, ensure_ascii=False))

    standalone_schemas = {}
    for yaml_file in SEED_SCHEMAS + SERVICE_SCHEMAS:
        schema = build_seed_schema(yaml_file, full_context)
        standalone_schemas[yaml_file] = schema

    _build_contexts_module(full_context, standalone_schemas)


if __name__ == "__main__":
    build()
