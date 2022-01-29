# -*- coding: utf-8 -*-
import pathlib
import yaml


ROOT = pathlib.Path(__file__).parent.parent.absolute()
SCHEMAS = ROOT / "iscc_schema/models"
MARKDOWN_TERMS_SCHEMA = ROOT / "docs/includes/terms-schema.md"
MARKDOWN_TERMS_ISCC = ROOT / "docs/includes/terms-iscc.md"


def terms(context):
    """Filter terms by x-iscc-context"""

    schemata = [
        "iscc-minimal.yaml",
        "iscc-basic.yaml",
        "iscc-extended.yaml",
        "iscc-technical.yaml",
        "iscc-nft.yaml",
        "iscc-crypto.yaml",
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

    for term, data in terms("http://schema.org"):
        doc += f"### **{term}**\n\n"
        doc += f'!!! term "<small><{data["x-iscc-context"]}></small>"\n\n'
        doc += f"    {data['x-iscc-schema-doc']}\n\n"
        doc += f"    **Comment**:  {data['description']}\n\n"
        if data.get("x-iscc-embed"):
            doc += f"    **Embedding**:  {data['x-iscc-embed']}\n\n"

    with open(MARKDOWN_TERMS_SCHEMA, "wt", encoding="utf-8") as outf:
        outf.write(doc)


def build_terms_iscc():
    """Build ISCC terms markdown for inclusion into /terms/index.md"""
    doc = ""

    for term, data in terms("http://purl.org/iscc"):
        doc += f"### **{term}**\n\n"
        doc += f'!!! term "<small><{data["x-iscc-context"]}></small>"\n\n'
        doc += f"    {data['description']}\n\n"

    with open(MARKDOWN_TERMS_ISCC, "wt", encoding="utf-8") as outf:
        outf.write(doc)


def build():
    build_terms_schema()
    build_terms_iscc()


if __name__ == "__main__":
    build()
