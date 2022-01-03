# **ISCC** - Schema Definitions

[![Build](https://github.com/iscc/iscc-schema/actions/workflows/tests.yml/badge.svg)](https://github.com/iscc/iscc-schema/actions/workflows/tests.yml)
[![Version](https://img.shields.io/pypi/v/iscc-schema.svg)](https://pypi.python.org/pypi/iscc-schema/)

## Introduction

This repository hosts all schema definitions of the ISCC. Schemas are defined in
[OpenAPI v3.1.0](https://spec.openapis.org/oas/v3.1.0.html) format and serve as a
single source of truth for auto-generated [JSON Schema](https://json-schema.org/)
definitions, [JSON-LD](https://json-ld.org/) contexts, and other schema related
artifacts.

## Generated files:

The source of code generation is `iscc_schema/models/iscc.yaml`.
The outputs produced when running `poe build` are:

- `docs/schema/iscc.json` - JSON Schema for ISCC Metadata
- `docs/context/iscc.json` - JSON-LD context for ISCC Metadata
- `iscc_schema/schema.py` - Pydantic model for ISCC Metadata

## OpenAPI Extensions

The OpenAPI Specification allows for
[extending](https://spec.openapis.org/oas/latest.html#specification-extensions) the
specification with custom fields. Extensions must start with `x-`.
All ISCC extensions start with `x-iscc-`:

- `x-iscc-context` - for documenting JSON-LD contexts.
- `x-iscc-schema-doc` - for original descriptions from [schema.org](https://schema.org)


## Changelog

### 0.1.0 - Unreleased
- Initial release

*[ISCC]: International Standard Content Code
