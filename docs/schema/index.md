---
icon: lucide/file-json
title: Overview
description: Schema definitions for the ISCC.
---

# Schema Documentation

Schema definitions for the International Standard Content Code (ISCC).

## ISCC Metadata

- [**ISCC Metadata**](iscc.md) — Core metadata vocabulary for digital content identified by the ISCC (ISO 24138:2024)

## Seed Metadata

Industry-specific seed metadata schemas for interoperable Meta-Code generation. See [IEP-0002](https://github.com/iscc/iscc-ieps/blob/main/ieps/iep-0002.md) for details.

- [**ISBN Seed Metadata**](isbn.md) — ISBN Seed Metadata for interoperable Meta-Code generation.
- [**ISRC Seed Metadata**](isrc.md) — ISRC Seed Metadata for interoperable Meta-Code generation.
- [**STM Seed Metadata**](stm.md) — STM (Scientific/Technical/Medical) Seed Metadata for interoperable Meta-Code generation. Minimal distinguishing metadata for scholarly works identified by a DOI, populatable from any DOI via Crossref/DataCite content negotiation (CSL-JSON).

## Service Metadata

Use-case-specific metadata schemas served by ISCC registries and discoverable through ISCC gateways.

- [**TDM Service Metadata**](tdm.md) — Machine-readable TDM rights signals conformant with W3C TDMRep, providing content-addressed delivery of tdm-reservation and tdm-policy properties via ISCC. Designed for content identification and discovery where identity, provenance, and trust context complement the reservation signal.
- [**GenAI Service Metadata**](genai.md) — Machine-readable generative AI disclosure signals for content transparency. Designed for AI providers to declare the level of AI involvement in content creation, supporting compliance with transparency regulations (e.g., EU AI Act Art. 50) and enabling end users to verify AI-generated content. These signals are designed for use within content identification and discovery protocols that provide additional identity, provenance, and trust context.
- [**Identifiers Service Metadata**](identifiers.md) — Set of typed external identifiers served for an asset identified by an ISCC.

## Protocol Schemas

ISCC Discovery Protocol records exchanged with ISCC-HUBs and registries. These default to compact JSON with a version-specific `$schema` and recover JSON-LD on demand.

- [**IsccNote**](iscc-note.md) — An ISCC Declaration record submitted to an ISCC-HUB for timestamping and registration. IsccNote is the permanent, self-describing log entry that binds an ISCC-CODE to its content hashes and a cryptographic signature. Stored in an append-only log, declarations are immutable once accepted, so the record is version-pinned and carries resolvable schema and context URLs.
