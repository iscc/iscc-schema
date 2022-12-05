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
        output=outfile,
        encoding="UTF-8",
        aliases=aliases,
        class_name="IsccMeta",
        disable_timestamp=True,
        use_schema_description=True,
        use_annotated=False,
        reuse_model=True,
        disable_appending_item_suffix=True,
        field_constraints=True,
        field_extra_keys={"x-iscc-context"},
        target_python_version=PythonVersion.PY_37,
        validation=True,
    )
    # Patch Generated Code
    marker = "from pydantic import AnyUrl, BaseModel, Field\n"
    replace = (
        "from pydantic import Field\n"
        "from iscc_schema.fields import AnyUrl\n"
        "from iscc_schema.base import BaseModel"
    )
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
        disable_timestamp=True,
        use_schema_description=True,
        openapi_scopes=[OpenAPIScope.Schemas, OpenAPIScope.Paths],
        reuse_model=True,
        disable_appending_item_suffix=True,
        target_python_version=PythonVersion.PY_37,
        field_constraints=True,  # This does not allow format-uri with maxLength constraint
    )
    # Patch AnyUrl
    marker = "from pydantic import AnyUrl, BaseModel, Field\n"
    replace = (
        "from pydantic import Field\n"
        "from iscc_schema.fields import AnyUrl\n"
        "from iscc_schema.base import BaseModel\n"
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
