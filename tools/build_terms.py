# -*- coding: utf-8 -*-
"""Build vocabulary term documentation from YAML schema definitions."""

import pathlib
import yaml

ROOT = pathlib.Path(__file__).parent.parent.absolute()
SCHEMAS = ROOT / "iscc_schema/models"
MARKDOWN_TERMS_SCHEMA = ROOT / "docs/includes/terms-schema.md"
MARKDOWN_TERMS_ISCC = ROOT / "docs/includes/terms-iscc.md"
MARKDOWN_TERMS_SEED = ROOT / "docs/includes/terms-seed.md"
MARKDOWN_TERMS_SERVICE = ROOT / "docs/includes/terms-service.md"
MARKDOWN_TERMS_PROTOCOL = ROOT / "docs/includes/terms-protocol.md"

SEED_SCHEMATA = ["isbn.yaml", "isrc.yaml", "stm.yaml"]
SERVICE_SCHEMATA = ["tdm.yaml", "genai.yaml", "identifiers.yaml"]
PROTOCOL_SCHEMATA = ["iscc-note.yaml"]
SERVICE_TYPE_CONTEXTS = {
    "TDM": "http://purl.org/iscc/terms/#TDM",
    "GenAI": "http://purl.org/iscc/terms/#GenAI",
    "Identifiers": "http://purl.org/iscc/terms/#Identifiers",
}


def terms(context):
    """Filter terms by x-iscc-context"""

    schemata = [
        "iscc-minimal.yaml",
        "iscc-basic.yaml",
        "iscc-embeddable.yaml",
        "iscc-extended.yaml",
        "iscc-technical.yaml",
        "iscc-nft.yaml",
        "iscc-crypto.yaml",
        "iscc-declaration.yaml",
    ]

    for schema in schemata:
        path = SCHEMAS / schema
        with open(path, "rt", encoding="utf-8") as infile:
            data = yaml.safe_load(infile)
        for term, fields in data["properties"].items():
            if fields.get("x-iscc-context", "").startswith(context):
                yield term, fields


def build_terms_schema():
    """Build schema.org terms markdown for inclusion into /terms/index.md"""
    doc = ""

    contexts = ["http://schema.org", "https://www.w3.org/2018/credentials"]

    for cont in contexts:
        for term, data in terms(cont):
            doc += f"### **{term}**\n\n"
            doc += f'!!! term "<small><{data["x-iscc-context"]}></small>"\n\n'
            doc += f"    {data['x-iscc-schema-doc']}\n\n"
            doc += f"    **Comment**:  {data['description']}\n\n"
            if data.get("x-iscc-embed"):
                doc += f"    **Embedding**:  {data['x-iscc-embed']}\n\n"
            if data.get("x-iscc-standard"):
                doc += f"    **Standard**:  {data['x-iscc-standard']}\n\n"
            if data.get("x-iscc-status"):
                doc += f"    **Status**:  {data['x-iscc-status']}\n\n"

    with open(MARKDOWN_TERMS_SCHEMA, "wt", encoding="utf-8", newline="\n") as outf:
        outf.write(doc)


def build_terms_iscc():
    """Build ISCC terms markdown for inclusion into /terms/index.md"""
    doc = ""

    for term, data in terms("http://purl.org/iscc"):
        doc += f"### **{term}**\n\n"
        doc += f'!!! term "<small><{data["x-iscc-context"]}></small>"\n\n'
        doc += f"    {data['description']}\n\n"
        if data.get("x-iscc-standard"):
            doc += f"    **Standard**:  {data['x-iscc-standard']}\n\n"
        if data.get("x-iscc-status"):
            doc += f"    **Status**:  {data['x-iscc-status']}\n\n"

    with open(MARKDOWN_TERMS_ISCC, "wt", encoding="utf-8", newline="\n") as outf:
        outf.write(doc)


def _build_terms_for_schemas(schemata, outpath, type_contexts=None, skip_contexts=None):
    # type: (list[str], pathlib.Path, dict|None, set[str]|None) -> None
    """Build vocabulary terms markdown from a list of standalone schema files."""
    doc = ""
    seen = set()
    skip_contexts = skip_contexts or set()

    def iter_term_fields(properties):
        # type: (dict) -> object
        """Yield top-level and explicitly mapped nested property definitions."""
        for term, fields in properties.items():
            yield term, fields
            candidates = []
            if fields.get("type") == "object":
                candidates.append(fields)
            items = fields.get("items")
            if isinstance(items, dict):
                candidates.append(items)
            for candidate in candidates:
                for nested_term, nested_fields in candidate.get("properties", {}).items():
                    if "x-iscc-context" in nested_fields:
                        yield nested_term, nested_fields

    for schema_file in schemata:
        path = SCHEMAS / schema_file
        with open(path, "rt", encoding="utf-8") as infile:
            data = yaml.safe_load(infile)
        type_name = data.get("properties", {}).get("@type", {}).get("const")
        if type_contexts and type_name in type_contexts and type_name not in seen:
            seen.add(type_name)
            doc += f"### **{type_name}**\n\n"
            doc += f'!!! term "<small><{type_contexts[type_name]}></small>"\n\n'
            doc += f"    {data['description']}\n\n"
        for term, fields in iter_term_fields(data.get("properties", {})):
            if not fields.get("x-iscc-context"):
                continue
            if fields["x-iscc-context"] in skip_contexts:
                continue
            if term in seen:
                continue
            seen.add(term)
            doc += f"### **{term}**\n\n"
            doc += f'!!! term "<small><{fields["x-iscc-context"]}></small>"\n\n'
            doc += f"    {fields['description']}\n\n"
            if fields.get("x-iscc-status"):
                doc += f"    **Status**:  {fields['x-iscc-status']}\n\n"

    with open(outpath, "wt", encoding="utf-8", newline="\n") as outf:
        outf.write(doc)


def build_terms_seed():
    """Build seed metadata terms markdown for inclusion into /terms/index.md"""
    _build_terms_for_schemas(SEED_SCHEMATA, MARKDOWN_TERMS_SEED)


def build_terms_service():
    """Build service metadata terms markdown for inclusion into /terms/index.md"""
    schema_contexts = {
        fields["x-iscc-context"]
        for context in ("http://schema.org", "https://www.w3.org/2018/credentials")
        for _, fields in terms(context)
    }
    _build_terms_for_schemas(
        SERVICE_SCHEMATA,
        MARKDOWN_TERMS_SERVICE,
        SERVICE_TYPE_CONTEXTS,
        skip_contexts=schema_contexts,
    )


def build_terms_protocol():
    """Build protocol schema terms markdown for inclusion into /terms/index.md"""
    _build_terms_for_schemas(PROTOCOL_SCHEMATA, MARKDOWN_TERMS_PROTOCOL)


def build():
    build_terms_schema()
    build_terms_iscc()
    build_terms_seed()
    build_terms_service()
    build_terms_protocol()


if __name__ == "__main__":
    build()
