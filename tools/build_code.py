# -*- coding: utf-8 -*-
"""Build Pydantic models for Schema definitions."""

import json
import re
import subprocess
import sys
import pathlib
from datamodel_code_generator import Formatter, InputFileType, generate, OpenAPIScope, PythonVersion

ROOT = pathlib.Path(__file__).parent.parent
CODE = ROOT / "iscc_schema"
APIS = CODE / "reference"
MODELS = CODE / "models"


def _get_version():
    # type: () -> str
    """Read the package version from __init__.py without importing the module."""
    init_file = CODE / "__init__.py"
    text = init_file.read_text(encoding="utf-8")
    match = re.search(r'^__version__\s*=\s*["\']([^"\']+)["\']', text, re.MULTILINE)
    return match.group(1)


def _patch_imports(outfile):
    # type: (pathlib.Path) -> None
    """Replace generated Pydantic imports with custom BaseModel and AnyUrl."""
    with outfile.open("rt", encoding="utf-8") as f:
        text = f.read()

    # Replace the pydantic import line, keeping other imports but swapping AnyUrl and BaseModel
    def replace_import(match):
        # type: (re.Match) -> str
        names = [n.strip() for n in match.group(1).split(",")]
        had_anyurl = "AnyUrl" in names
        remaining = [n for n in names if n not in ("AnyUrl", "BaseModel")]
        lines = []
        if remaining:
            lines.append(f"from pydantic import {', '.join(remaining)}")
        if had_anyurl:
            lines.append("from iscc_schema.fields import AnyUrl")
        lines.append("from iscc_schema.base import BaseModel")
        return "\n".join(lines)

    text = re.sub(r"^from pydantic import (.+)$", replace_import, text, count=1, flags=re.MULTILINE)
    with outfile.open("wt", encoding="utf-8", newline="\n") as f:
        f.write(text)


def _patch_versioned_urls(outfile, patch_schema=True):
    # type: (pathlib.Path, bool) -> None
    """Replace unversioned ISCC URLs with versioned ones in generated models."""
    version = _get_version()
    with outfile.open("rt", encoding="utf-8") as f:
        text = f.read()
    for q in ('"', "'"):
        text = text.replace(
            f"{q}http://purl.org/iscc/context{q}",
            f"{q}http://purl.org/iscc/context/{version}.jsonld{q}",
        )
        if patch_schema:
            text = text.replace(
                f"{q}http://purl.org/iscc/schema{q}",
                f"{q}http://purl.org/iscc/schema/{version}.json{q}",
            )
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
        input_file_type=InputFileType.JsonSchema,
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
        formatters=[],
    )
    _patch_imports(outfile)
    _patch_versioned_urls(outfile)


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
        formatters=[],
    )
    _patch_imports(outfile)


SEED_SCHEMAS = {
    "isbn": ("isbn.yaml", "seed_isbn.py", "ISBN"),
    "isrc": ("isrc.yaml", "seed_isrc.py", "ISRC"),
}

SERVICE_SCHEMAS = {
    "tdm": ("tdm.yaml", "service_tdm.py", "TDM"),
    "genai": ("genai.yaml", "service_genai.py", "GenAI"),
}


def _build_standalone_models(schemas):
    # type: (dict) -> None
    """Generate Pydantic v2 models from standalone YAML schema definitions."""
    aliases = CODE / "aliases.json"
    aliases_data = json.load(aliases.open("rb"))
    for yaml_file, py_file, class_name in schemas.values():
        infile = MODELS / yaml_file
        outfile = CODE / py_file
        generate(
            infile,
            input_file_type=InputFileType.JsonSchema,
            output=outfile,
            encoding="UTF-8",
            aliases=aliases_data,
            class_name=class_name,
            disable_timestamp=True,
            use_schema_description=True,
            use_annotated=False,
            reuse_model=True,
            disable_appending_item_suffix=True,
            field_constraints=True,
            field_extra_keys={"x-iscc-context"},
            target_python_version=PythonVersion.PY_310,
            validation=True,
            formatters=[],
        )
        _patch_imports(outfile)
        _patch_versioned_urls(outfile, patch_schema=False)


def build_seed_metadata():
    # type: () -> None
    """Generate Pydantic v2 models for industry-specific seed metadata schemas."""
    _build_standalone_models(SEED_SCHEMAS)


def build_service_metadata():
    # type: () -> None
    """Generate Pydantic v2 models for use-case-specific service metadata schemas."""
    _build_standalone_models(SERVICE_SCHEMAS)


def _format_generated(outfiles):
    # type: (list[pathlib.Path]) -> None
    """Format generated files with black using project settings."""
    subprocess.run(
        [sys.executable, "-m", "black", "--quiet"] + [str(f) for f in outfiles],
        check=True,
    )


def build():
    # type: () -> None
    build_schema()
    build_apis()
    build_seed_metadata()
    build_service_metadata()
    _format_generated(
        [
            CODE / "schema.py",
            CODE / "generator.py",
            CODE / "seed_isbn.py",
            CODE / "seed_isrc.py",
            CODE / "service_tdm.py",
            CODE / "service_genai.py",
        ]
    )


if __name__ == "__main__":
    build()
