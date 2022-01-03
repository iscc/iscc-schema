"""Copy README.md to documentation index.md"""
from os.path import abspath, dirname, join
from textwrap import indent

import yaml
import pathlib
import json

ROOT = pathlib.Path(__file__).parent.parent
SCHEMAS = ROOT / "iscc_schema/models"
MARKDOWN_SCHEMA = ROOT / "docs/schema/index.md"
MARKDOWN_CONTEXT = ROOT / "docs/context/index.md"

HERE = dirname(abspath(__file__))
SRC = join(HERE, "../README.md")
DST = join(HERE, "../docs/index.md")


# TODO group terms by schame/isccmeta
# TODO publish to terms
# TODO add notes to original terms
# TODO update purl.org forwardings
# TODO test json-ld normalization
# TODO add more examples
# TODO add logging to tool actions
# TODO maybe don`t redefine json-ld type to §schema


def copy_readme():
    """Copy README.md to documentation index.md"""
    with open(SRC, "rt", encoding="utf-8") as infile:
        text = infile.read()

    with open(DST, "wt", encoding="utf-8") as outf:
        outf.write(text)


def build_json_schema_docs():
    """Build markdown from JSON Schema"""
    header = "# JSON Schema for ISCC Metadata\n\n"
    schemata = [
        # "iscc-jsonld.yaml",
        "iscc-minimal.yaml",
        "iscc-basic.yaml",
        "iscc-extended.yaml",
        "iscc-properties.yaml",
        "iscc-technical.yaml",
        "iscc-crypto.yaml",
    ]
    content = header
    for schema in schemata:
        path = SCHEMAS / schema
        with open(path) as infile:
            data = yaml.safe_load(infile)
        content += f"## {data['title']}\n"
        content += f"{data['description']}\n"
        if data.get("examples"):
            pretty = json.dumps(data.get("examples")[0], indent=2)
            content += f"""
!!! example

    ```json
{indent(pretty, prefix="    ")}
    ```
"""

        for prop, attrs in data["properties"].items():
            type_ = attrs.get("type")
            if attrs.get("format"):
                type_ += "-" + attrs.get("format")
            title = f"**{prop}**\n"
            if attrs.get("x-iscc-context"):
                title += f"<{attrs.get('x-iscc-context')}>\n"
            description = attrs.get("description")
            content += f"### {title}\n"
            content += f"| Name | Type | Definition                               |\n"
            content += f"| ---- | ---- | -----------------------------------------|\n"
            content += f"| {prop} | `{type_}` | {description}                     |\n\n"

    with open(MARKDOWN_SCHEMA, "wt", encoding="utf-8") as outf:
        outf.write(content)


def build_json_ld_context_docs():

    doc = f"# **ISCC** - Metadata Vocabulary\n\n"

    schemata = [
        # "iscc-jsonld.yaml",
        "iscc-minimal.yaml",
        "iscc-basic.yaml",
        "iscc-extended.yaml",
        "iscc-properties.yaml",
        "iscc-technical.yaml",
        "iscc-crypto.yaml",
    ]

    for schema in schemata:
        path = SCHEMAS / schema
        with open(path) as infile:
            data = yaml.safe_load(infile)

        for prop, fields in data["properties"].items():
            if fields.get("x-iscc-context"):
                doc += f"## {prop}\n\n"
                doc += f"<small><{fields.get('x-iscc-context')}></small>\n"
                doc += '!!! term ""\n'
                doc += f"    {fields['description']}\n\n"

    with open(MARKDOWN_CONTEXT, "wt", encoding="UTF-8") as outf:
        outf.write(doc)


def build():
    copy_readme()
    build_json_schema_docs()
    build_json_ld_context_docs()


if __name__ == "__main__":
    build()
