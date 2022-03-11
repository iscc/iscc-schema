# -*- coding: utf-8 -*-
"""Build Pydantic models for Schema definitions"""
import json
import pathlib
from datamodel_code_generator import InputFileType, generate, OpenAPIScope, PythonVersion


ROOT = pathlib.Path(__file__).parent.parent
CODE = ROOT / "iscc_schema"
APIS = CODE / "reference"
MODELS = CODE / "models"


def build_schema():
    infile = MODELS / "iscc-all.yaml"
    outfile = CODE / "schema.py"
    aliases = CODE / "aliases.json"
    aliases = json.load(aliases.open("rb"))
    generate(
        infile,
        field_constraints=True,
        aliases=aliases,
        output=outfile,
        field_extra_keys={"x-iscc-context"},
        use_schema_description=True,
        wrap_string_literal=True,
        use_annotated=False,
        class_name="IsccMeta",
        disable_timestamp=True,
        target_python_version=PythonVersion.PY_37,
        validation=True,
        encoding="UTF-8",
        reuse_model=True,
        disable_appending_item_suffix=True,
    )
    # Patch AnyUrl
    marker = "from pydantic import AnyUrl, BaseModel, Field\n"
    replace = "from pydantic import BaseModel, Field\nfrom iscc_schema.fields import AnyUrl\n"
    with outfile.open("rt", encoding="utf-8") as infile:
        text = infile.read()
        text = text.replace(marker, replace)
    with outfile.open("wt", encoding="utf-8", newline="\n") as patched:
        patched.write(text)


def build_apis():
    infile = APIS / "iscc-generator.yaml"
    outfile = CODE / "generator.py"
    generate(
        infile,
        input_file_type=InputFileType.OpenAPI,
        output=outfile,
        encoding="UTF-8",
        wrap_string_literal=True,
        disable_timestamp=True,
        use_schema_description=True,
        openapi_scopes=[OpenAPIScope.Schemas, OpenAPIScope.Paths],
        reuse_model=True,
        disable_appending_item_suffix=True,
    )
    # Patch AnyUrl
    marker = "from pydantic import AnyUrl, BaseModel, Field, constr\n"
    replace = (
        "from pydantic import BaseModel, Field, constr\nfrom iscc_schema.fields import AnyUrl\n"
    )
    with outfile.open("rt", encoding="utf-8") as infile:
        text = infile.read()
        text = text.replace(marker, replace)
    with outfile.open("wt", encoding="utf-8", newline="\n") as patched:
        patched.write(text)


def build():
    build_schema()
    build_apis()


if __name__ == "__main__":
    build()
