"""Copy README.md to documentation index.md"""

from os.path import abspath, dirname, join
from textwrap import indent

import yaml
import pathlib
import json

ROOT = pathlib.Path(__file__).parent.parent
SCHEMAS = ROOT / "iscc_schema/models"
MARKDOWN_SCHEMA = ROOT / "docs/schema/iscc.md"
MARKDOWN_SCHEMA_INDEX = ROOT / "docs/schema/index.md"
MARKDOWN_CONTEXT = ROOT / "docs/context/index.md"

HERE = dirname(abspath(__file__))
SRC = join(HERE, "../README.md")
DST = join(HERE, "../docs/index.md")
CHANGELOG_SRC = join(HERE, "../CHANGELOG.md")
CHANGELOG_DST = join(HERE, "../docs/changelog.md")


# TODO test json-ld normalization
# TODO add more examples
# TODO add logging to tool actions


def copy_root_files():
    """Copy README and CHANGELOG to documentation"""
    with open(SRC, "rt", encoding="utf-8") as infile:
        text = infile.read()

    with open(DST, "wt", encoding="utf-8", newline="\n") as outf:
        outf.write(text)

    with open(CHANGELOG_SRC, "rt", encoding="utf-8") as infile:
        text = infile.read()

    with open(CHANGELOG_DST, "wt", encoding="utf-8", newline="\n") as outf:
        outf.write(text)


SEED_SCHEMATA = ["isbn.yaml", "isrc.yaml"]
SERVICE_SCHEMATA = ["tdm.yaml", "genai.yaml"]


def _render_schema_sections(schemata):
    # type: (list[str]) -> str
    """Render markdown documentation sections from a list of YAML schema files."""
    content = ""
    for schema in schemata:
        path = SCHEMAS / schema
        with open(path, "rt", encoding="utf-8") as infile:
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
        if data.get("required"):
            content += f"**Required fields**: `{'`, `'.join(data['required'])}`\n\n"

        for prop, attrs in data["properties"].items():
            type_ = attrs.get("type")
            if attrs.get("format"):
                type_ += "-" + attrs.get("format")
            title = f"**{prop}**\n"
            if attrs.get("x-iscc-context"):
                title += f"<{attrs.get('x-iscc-context')}>\n"
            if attrs.get("x-iscc-standard"):
                title += f"<small>{attrs.get('x-iscc-standard')}</small>\n"
            description = attrs.get("description")
            if attrs.get("example"):
                description += f"<br><br>**Example**: `{attrs['example']}`"
            default = attrs.get("default") or attrs.get("const", "none")
            content += f"### {title}\n"
            content += f"| Name | Type | Default | Definition                     |\n"
            content += f"| ---- | ---- | --------|--------------------------------|\n"
            content += f"| {prop} | `{type_}` | {default} | {description}         |\n\n"
    return content


def build_json_schema_docs():
    """Build markdown for ISCC Metadata schema page."""
    iscc_schemata = [
        "iscc-jsonld.yaml",
        "iscc-minimal.yaml",
        "iscc-basic.yaml",
        "iscc-embeddable.yaml",
        "iscc-extended.yaml",
        "iscc-technical.yaml",
        "iscc-nft.yaml",
        "iscc-crypto.yaml",
        "iscc-declaration.yaml",
    ]
    content = "# JSON Schema for ISCC Metadata\n\n"
    content += _render_schema_sections(iscc_schemata)

    with open(MARKDOWN_SCHEMA, "wt", encoding="utf-8", newline="\n") as outf:
        outf.write(content)


def _build_standalone_doc(schema_file, category, extra_text=""):
    # type: (str, str, str) -> None
    """Build a markdown documentation page for a standalone schema."""
    path = SCHEMAS / schema_file
    with open(path, "rt", encoding="utf-8") as infile:
        data = yaml.safe_load(infile)

    name = schema_file.replace(".yaml", "")
    title = data["title"]
    content = f"# {title} {category}\n\n"
    content += f"{data['description']}"
    if extra_text:
        content += f" {extra_text}"
    content += "\n\n"
    content += f"**JSON Schema**: [`{name}.json`]({name}.json)\n\n"

    if data.get("examples"):
        pretty = json.dumps(data["examples"][0], indent=2)
        content += f"!!! example\n\n    ```json\n{indent(pretty, prefix='    ')}\n    ```\n\n"

    if data.get("required"):
        content += f"**Required fields**: `{'`, `'.join(data['required'])}`\n\n"

    for prop, attrs in data["properties"].items():
        type_ = attrs.get("type")
        if attrs.get("format"):
            type_ += "-" + attrs.get("format")
        heading = f"**{prop}**\n"
        if attrs.get("x-iscc-context"):
            heading += f"<{attrs.get('x-iscc-context')}>\n"
        description = attrs.get("description")
        if attrs.get("example"):
            description += f"<br><br>**Example**: `{attrs['example']}`"
        default = attrs.get("default") or attrs.get("const", "none")
        content += f"## {heading}\n"
        content += f"| Name | Type | Default | Definition                     |\n"
        content += f"| ---- | ---- | --------|--------------------------------|\n"
        content += f"| {prop} | `{type_}` | {default} | {description}         |\n\n"

    outpath = ROOT / "docs" / "schema" / f"{name}.md"
    with open(outpath, "wt", encoding="utf-8", newline="\n") as outf:
        outf.write(content)


def build_seed_schema_docs():
    """Build a separate markdown page for each seed metadata schema."""
    iep_link = (
        "See [IEP-0002](https://github.com/iscc/iscc-ieps/blob/main/ieps/iep-0002.md)"
        " for details on Meta-Code generation."
    )
    for schema_file in SEED_SCHEMATA:
        _build_standalone_doc(schema_file, "Seed Metadata", iep_link)


def build_service_schema_docs():
    """Build a separate markdown page for each service metadata schema."""
    for schema_file in SERVICE_SCHEMATA:
        _build_standalone_doc(schema_file, "Service Metadata")


def _render_context_terms(schemata):
    # type: (list[str]) -> str
    """Render vocabulary terms from a list of YAML schema files."""
    doc = ""
    seen = set()
    for schema in schemata:
        path = SCHEMAS / schema
        with open(path, "rt", encoding="utf-8") as infile:
            data = yaml.safe_load(infile)
        for prop, fields in data["properties"].items():
            if fields.get("x-iscc-context") and prop not in seen:
                seen.add(prop)
                doc += f"## {prop}\n\n"
                doc += f"<small><{fields.get('x-iscc-context')}></small>\n"
                if fields.get("x-iscc-standard"):
                    doc += f"<small>{fields.get('x-iscc-standard')}</small>\n"
                doc += '!!! term ""\n'
                doc += f"    {fields['description']}\n\n"
    return doc


def build_json_ld_context_docs():
    # type: () -> None
    """Build vocabulary documentation for JSON-LD context terms."""
    iscc_schemata = [
        # "iscc-jsonld.yaml",
        "iscc-minimal.yaml",
        "iscc-basic.yaml",
        "iscc-embeddable.yaml",
        "iscc-extended.yaml",
        "iscc-technical.yaml",
        "iscc-nft.yaml",
        "iscc-crypto.yaml",
        "iscc-declaration.yaml",
    ]
    doc = "# **ISCC** - Metadata Vocabulary\n\n"
    doc += _render_context_terms(iscc_schemata)
    doc += "\n---\n\n"
    doc += "# Seed Metadata Vocabulary\n\n"
    doc += _render_context_terms(SEED_SCHEMATA)
    doc += "\n---\n\n"
    doc += "# Service Metadata Vocabulary\n\n"
    doc += _render_context_terms(SERVICE_SCHEMATA)

    with open(MARKDOWN_CONTEXT, "wt", encoding="utf-8", newline="\n") as outf:
        outf.write(doc)


def build_schema_index():
    # type: () -> None
    """Build the schema section landing page with links to all schema pages."""
    content = "# Schema Documentation\n\n"
    content += "Schema definitions for the International Standard Content Code (ISCC).\n\n"
    content += "## ISCC Metadata\n\n"
    content += "- [**ISCC Metadata**](iscc.md) — "
    content += (
        "Core metadata vocabulary for digital content identified by the ISCC (ISO 24138:2024)\n\n"
    )
    content += "## Seed Metadata\n\n"
    content += "Industry-specific seed metadata schemas for interoperable Meta-Code generation. "
    content += "See [IEP-0002](https://github.com/iscc/iscc-ieps/blob/main/ieps/iep-0002.md) "
    content += "for details.\n\n"
    for schema_file in SEED_SCHEMATA:
        path = SCHEMAS / schema_file
        with open(path, "rt", encoding="utf-8") as infile:
            data = yaml.safe_load(infile)
        name = schema_file.replace(".yaml", "")
        content += f"- [**{data['title']} Seed Metadata**]({name}.md) — {data['description']}\n"
    content += "\n"
    content += "## Service Metadata\n\n"
    content += "Use-case-specific metadata schemas served by ISCC registries "
    content += "and discoverable through ISCC gateways.\n\n"
    for schema_file in SERVICE_SCHEMATA:
        path = SCHEMAS / schema_file
        with open(path, "rt", encoding="utf-8") as infile:
            data = yaml.safe_load(infile)
        name = schema_file.replace(".yaml", "")
        content += f"- [**{data['title']} Service Metadata**]({name}.md) — {data['description']}\n"

    with open(MARKDOWN_SCHEMA_INDEX, "wt", encoding="utf-8", newline="\n") as outf:
        outf.write(content)


def build():
    # type: () -> None
    """Build all documentation artifacts."""
    copy_root_files()
    build_json_schema_docs()
    build_seed_schema_docs()
    build_service_schema_docs()
    build_schema_index()
    build_json_ld_context_docs()


if __name__ == "__main__":
    build()
