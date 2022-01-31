# -*- coding: utf-8 -*-
"""Build Pydantic models for Schema definitions"""
import pathlib
from datamodel_code_generator import InputFileType, generate

ROOT = pathlib.Path(__file__).parent.parent
CODE = ROOT / "iscc_schema"
APIS = CODE / "reference"


def build_apis():
    infile = APIS / "iscc-service-generator.yaml"
    outfile = CODE / "generator.py"
    generate(
        infile,
        input_file_type=InputFileType.OpenAPI,
        output=outfile,
        encoding="UTF-8",
        wrap_string_literal=True,
    )


def build():
    build_apis()


if __name__ == "__main__":
    build_apis()
