# -*- coding: utf-8 -*-
"""Build Pydantic models for Schema definitions."""

import json
import re
import pathlib
from datamodel_code_generator import InputFileType, generate, OpenAPIScope, PythonVersion

ROOT = pathlib.Path(__file__).parent.parent
CODE = ROOT / "iscc_schema"
APIS = CODE / "reference"
MODELS = CODE / "models"


def _patch_imports(outfile):
    # type: (pathlib.Path) -> None
    """Replace generated Pydantic imports with custom BaseModel and AnyUrl."""
    with outfile.open("rt", encoding="utf-8") as f:
        text = f.read()

    # Replace the pydantic import line, keeping other imports but swapping AnyUrl and BaseModel
    def replace_import(match):
        # type: (re.Match) -> str
        names = [n.strip() for n in match.group(1).split(",")]
        # Remove AnyUrl and BaseModel from pydantic imports
        remaining = [n for n in names if n not in ("AnyUrl", "BaseModel")]
        lines = []
        if remaining:
            lines.append(f"from pydantic import {', '.join(remaining)}")
        lines.append("from iscc_schema.fields import AnyUrl")
        lines.append("from iscc_schema.base import BaseModel")
        return "\n".join(lines)

    text = re.sub(r"^from pydantic import (.+)$", replace_import, text, count=1, flags=re.MULTILINE)
    with outfile.open("wt", encoding="utf-8", newline="\n") as f:
        f.write(text)


def build_schema():
    # type: () -> None
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
        target_python_version=PythonVersion.PY_310,
        validation=True,
    )
    _patch_imports(outfile)


def build_apis():
    # type: () -> None
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
        target_python_version=PythonVersion.PY_310,
        field_constraints=True,
    )
    _patch_imports(outfile)


def build():
    # type: () -> None
    build_schema()
    build_apis()


if __name__ == "__main__":
    build()
