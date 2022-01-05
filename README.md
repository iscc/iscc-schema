# **ISCC** - Schema

*OpenAPI representation of the ISCC data model*

[![Build](https://github.com/iscc/iscc-schema/actions/workflows/tests.yml/badge.svg)](https://github.com/iscc/iscc-schema/actions/workflows/tests.yml)
[![Version](https://img.shields.io/pypi/v/iscc-schema.svg)](https://pypi.python.org/pypi/iscc-schema/)

## Introduction

This repository hosts all schema definitions of the ISCC. Schemas are defined in
[OpenAPI v3.1.0](https://spec.openapis.org/oas/v3.1.0.html) format and serve as a
single source of truth for auto-generated [JSON Schema](https://json-schema.org/)
definitions, [JSON-LD](https://json-ld.org/) contexts, and other schema related
artifacts.

## Generated files:

The source of code generation are the files at `iscc_schema/models/*`.
The outputs produced when running `poe build` are:

- `docs/schema/iscc.json` - JSON Schema for ISCC Metadata
- `docs/schema/index.md` - JSON Schema Markdown documentation
- `docs/context/iscc.jsonld` - JSON-LD context for ISCC Metadata
- `docs/terms/index.md` - ISCC Metadata Vocabulary documentation
- `iscc_schema/schema.py` - Pydantic models for ISCC Metadata

## Published files:

The generated files are published under the following canonical URLs:

- [`http://purl.org/iscc/schema`](http://purl.org/iscc/schema) - JSON Schema latest version
- [`http://purl.org/iscc/context`](http://purl.org/iscc/context) - JSON-LD Context latest version
- [`http://purl.org/iscc/terms`](http://purl.org/iscc/terms) - ISCC Metadata Vocabulary latest version
- [`http://pypi.org/project/iscc-schema`](http://pypi.org/project/iscc-schema) - Python package with pydantic models

## OpenAPI Extensions

The OpenAPI Specification allows for
[extending](https://spec.openapis.org/oas/latest.html#specification-extensions) the
specification with custom fields. Extensions must start with `x-`.
All ISCC extensions start with `x-iscc-`:

- `x-iscc-context` - for documenting JSON-LD contexts.
- `x-iscc-schema-doc` - for original descriptions from [schema.org](https://schema.org)


## Changelog

### 0.1.0 - 2022-01-05
- Initial release
