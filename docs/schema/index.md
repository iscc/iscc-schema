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

## Service Metadata

Use-case-specific metadata schemas served by ISCC registries and discoverable through ISCC gateways.

- [**TDM Service Metadata**](tdm.md) — Machine-readable TDM rights signals conformant with W3C TDMRep. The tdm_reservation field is semantically equivalent to TDMRep's tdm-reservation property, and tdm_policy links to an ODRL policy document. These signals are designed for use within content identification and discovery protocols that provide additional identity, provenance, and trust context.
- [**GenAI Service Metadata**](genai.md) — Machine-readable generative AI disclosure signals for content transparency. Designed for AI providers to declare the level of AI involvement in content creation, supporting compliance with transparency regulations (e.g., EU AI Act Art. 50) and enabling end users to verify AI-generated content. These signals are designed for use within content identification and discovery protocols that provide additional identity, provenance, and trust context.
