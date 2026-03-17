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

SEED_SCHEMATA = ["isbn.yaml", "isrc.yaml"]
SERVICE_SCHEMATA = ["tdm.yaml", "genai.yaml"]


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


def _build_terms_for_schemas(schemata, outpath):
    # type: (list[str], pathlib.Path) -> None
    """Build vocabulary terms markdown from a list of standalone schema files."""
    doc = ""
    seen = set()
    for schema_file in schemata:
        path = SCHEMAS / schema_file
        with open(path, "rt", encoding="utf-8") as infile:
            data = yaml.safe_load(infile)
        for term, fields in data.get("properties", {}).items():
            if not fields.get("x-iscc-context"):
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
    _build_terms_for_schemas(SERVICE_SCHEMATA, MARKDOWN_TERMS_SERVICE)


def build():
    build_terms_schema()
    build_terms_iscc()
    build_terms_seed()
    build_terms_service()


if __name__ == "__main__":
    build()
