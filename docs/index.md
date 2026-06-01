---
icon: lucide/house
description: ISCC JSON-LD Metadata and OpenAPI Service Descriptions.
---

# iscc-schema

[![Tests](https://github.com/iscc/iscc-schema/actions/workflows/tests.yml/badge.svg)](https://github.com/iscc/iscc-schema/actions/workflows/tests.yml)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/iscc/iscc-schema)

**JSON Schema and JSON-LD Contexts for ISCC Metadata**

## What is iscc-schema?

`iscc-schema` provides the official schema definitions for the International Standard Content Code
([ISO 24138:2024](https://www.iso.org/standard/77899.html)). YAML-based OpenAPI 3.1.0 definitions
are the single source of truth for auto-generated [JSON Schema](https://json-schema.org/),
[JSON-LD](https://json-ld.org/) contexts, [Python](https://python.org/) models, and vocabulary
documentation.

## Install

```bash
pip install iscc-schema
```

## Quick Start

Core and Service metadata serialize as full JSON-LD by default:

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
# JSON-LD: includes @context, @type and a version-pinned $schema
```

Seed and Protocol records serialize as **compact JSON** — just the fields plus a version-pinned
`$schema` that anchors the schema version and lets any consumer recover full JSON-LD on demand:

```python
from iscc_schema import STM, recover_context

seed = STM(
    doi="10.5555/example.2020.0001",
    resource_type="JournalArticle",
    title="On the Stability of Quasilinear Forms",
    publisher="Meridian Academic Press",
    pubyear=2020,
)

# Compact JSON by default: fields plus the version-pinned $schema, no @context/@type
seed.json()

# Opt into full JSON-LD when you need it
seed.json(ld=True)

# Recover the JSON-LD @context from compact data using its $schema
recover_context(seed.dict())
```

## Schema Categories

- **ISCC Metadata.** Core vocabulary for digital content identified by the ISCC. All fields
  are optional, covering content description, rights, technical properties, and cryptographic
  declarations.
- **Seed Metadata.** Industry-specific input for Meta-Code generation (`ISBN`, `ISRC`, `STM`).
  Required fields ensure interoperable content fingerprinting across platforms.
- **Service Metadata.** Use-case-specific schemas for ISCC registries (`TDM`, `GenAI`).
  Machine-readable signals for text and data mining rights and generative AI disclosure.
- **Protocol Schemas.** ISCC Discovery Protocol wire records (`IsccNote`). Compact,
  signature-anchored declaration records for ISCC-HUB timestamping and registration.

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
