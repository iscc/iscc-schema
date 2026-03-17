---
icon: lucide/house
description: ISCC JSON-LD Metadata and OpenAPI Service Descriptions.
---

# iscc-schema

[![Tests](https://github.com/iscc/iscc-schema/actions/workflows/tests.yml/badge.svg)](https://github.com/iscc/iscc-schema/actions/workflows/tests.yml)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/iscc/iscc-schema)

**JSON-LD Metadata and OpenAPI Service Descriptions for the International Standard Content Code.**

## What is iscc-schema?

`iscc-schema` provides the official schema definitions for the International Standard Content Code
([ISO 24138:2024](https://www.iso.org/standard/77899.html)). YAML-based OpenAPI 3.1.0 definitions
are the single source of truth for auto-generated [JSON Schema](https://json-schema.org/),
[JSON-LD](https://json-ld.org/) contexts, and [Python](https://python.org/) models.

## Install

```bash
pip install iscc-schema
```

## Quick Start

```python
from iscc_schema import IsccMeta

meta = IsccMeta(
    iscc="ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY",
    name="The Never Ending Story",
)

# Serialize as dict (set fields only)
meta.dict()
# {'iscc': 'ISCC:KACY...', 'name': 'The Never Ending Story'}

# Serialize as JSON (includes schema defaults)
meta.json()
# '{"@context":"http://purl.org/iscc/context","@type":"CreativeWork",...}'
```

## Schema Categories

- **ISCC Metadata.** Core vocabulary for digital content identified by the ISCC. All fields
  are optional, covering content description, rights, technical properties, and cryptographic
  declarations.
- **Seed Metadata.** Industry-specific input for Meta-Code generation (`ISBN`, `ISRC`).
  Required fields ensure interoperable content fingerprinting across platforms.
- **Service Metadata.** Use-case-specific schemas for ISCC registries (`TDM`, `GenAI`).
  Machine-readable signals for text and data mining rights and generative AI disclosure.

## Published Artifacts

| Artifact | URL |
|----------|-----|
| JSON Schema | [`http://purl.org/iscc/schema`](http://purl.org/iscc/schema) |
| JSON-LD Context | [`http://purl.org/iscc/context`](http://purl.org/iscc/context) |
| Vocabulary | [`http://purl.org/iscc/terms`](http://purl.org/iscc/terms) |
| Python Package | [`https://pypi.org/project/iscc-schema`](https://pypi.org/project/iscc-schema) |

## Documentation

Documentation is hosted at [schema.iscc.codes](https://schema.iscc.codes)

## Development

```bash
uv sync              # Install dependencies
uv run poe all       # Full build pipeline (codegen, tests, docs)
```

## Status

Under development. Expect breaking changes until we reach a version 1.0 release.
