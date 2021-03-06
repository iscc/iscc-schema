# **ISCC** - Schema

*ISCC - JSON-LD Metadata and OpenAPI Service Descriptions*

[![Build](https://github.com/iscc/iscc-schema/actions/workflows/tests.yml/badge.svg)](https://github.com/iscc/iscc-schema/actions/workflows/tests.yml)
[![Version](https://img.shields.io/pypi/v/iscc-schema.svg)](https://pypi.python.org/pypi/iscc-schema/)

## Introduction

This repository hosts all schema definitions of the ISCC. Schemas are defined in
[OpenAPI v3.1.0](https://spec.openapis.org/oas/v3.1.0.html) format and serve as a
single source of truth for auto-generated [JSON Schema](https://json-schema.org/)
definitions, [JSON-LD](https://json-ld.org/) contexts, and other schema related
artifacts.

## Metadata for Digital Content

Metadata is data about data. For digital content, metadata may describe assets for different
purposes such as data management, data provenance, allocation of royalties, indexing,
disambiguation, process automation, etc.

## ISCC Metadata

Calculating ISCC codes requires extensive processing of media assets. As a by-product, an ISCC
processor can automatically produce and retain metadata that describes the asset and helps with
comparing and matching digital content. ISCC creation is also an opportunity to embed metadata
into a digital asset. Once the metadata is embedded, an ISCC processor will automatically
regenerate the same ISCC Meta-Code without manually supplying custom metadata for processing.
As the ISCC targets a broad set of use-cases, it comes with a minimal and generic metadata schema.
This site documents the ISCC metadata model.

## Types of Metadata

For the identification of digital assets, ISCC distinguishes between two major types of metadata:

### Implicit Metadata

Implicit metadata is data that can be measured by analyzing a media asset. For example, an ISCC
processor can infer pixel width and height from an image or duration from an audio file. The use
of implicit metadata is very efficient and robust. It does not require a human to verify the
correctness of the data because it can be measured and verified automatically.

### Explicit Metadata

Explicit metadata is data about media assets assembled and curated by people. It is often stored
separately from the files in databases but may also be embedded into media assets. In contrast to
implicit metadata, human-curated metadata is prone to errors, laborious to manage, and often not
up to date. Platforms also tend to remove embedded metadata from the files they are hosting.

## Documentation

Documentation is hosted at [schema.iscc.codes](https://schema.iscc.codes)

## Status

Under development. Expect breaking changes until we reach a version 1.0 release.

## Generated files

The source of code generation are the files at `iscc_schema/models/*`.
The outputs produced when running `poe build` are:

- [`docs/schema/iscc.json`](https://github.com/iscc/iscc-schema/blob/main/docs/schema/iscc.json) - JSON Schema for ISCC Metadata
- [`docs/schema/index.md`](https://github.com/iscc/iscc-schema/blob/main/docs/schema/index.md) - JSON Schema Markdown documentation
- [`docs/context/iscc.jsonld`](https://github.com/iscc/iscc-schema/blob/main/docs/context/iscc.jsonld) - JSON-LD context for ISCC Metadata
- [`docs/terms/index.md`](https://github.com/iscc/iscc-schema/blob/main/docs/context/index.md) - ISCC Metadata Vocabulary documentation
- [`iscc_schema/schema.py`](https://github.com/iscc/iscc-schema/blob/main/iscc_schema/schema.py) - Pydantic models for ISCC Metadata
- [`iscc_schema/generator.py`](https://github.com/iscc/iscc-schema/blob/main/iscc_schema/generator.py) - Pydantic models for Generator Service API


## Published files

The generated files are published under the following canonical URLs:

- [`http://purl.org/iscc/schema`](http://purl.org/iscc/schema) - JSON Schema latest version
- [`http://purl.org/iscc/context`](http://purl.org/iscc/context) - JSON-LD Context latest version
- [`http://purl.org/iscc/terms`](http://purl.org/iscc/terms) - ISCC Metadata Vocabulary latest version
- [`http://pypi.org/project/iscc-schema`](http://pypi.org/project/iscc-schema) - Python package with pydantic models

## OpenAPI Docs

- [ISCC Generator Service](https://schema.iscc.codes/api)

## OpenAPI Extensions

The OpenAPI Specification allows for
[extending](https://spec.openapis.org/oas/latest.html#specification-extensions) the
specification with custom fields. Extensions must start with `x-`.
All ISCC extensions start with `x-iscc-`:

- `x-iscc-context` - for documenting JSON-LD contexts.
- `x-iscc-schema-doc` - for original descriptions from [schema.org](https://schema.org).
- `x-iscc-embed` - for information on how to embed fields into media assets.
- `x-iscc-status` - for information about status of the field
