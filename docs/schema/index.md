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

- [**TDM Service Metadata**](tdm.md) — Machine-readable TDM reservation signals for AI-related content usage categories. A 'reserved' status indicates an explicit opt-out from TDM exceptions (e.g., EU DSM Directive Art. 4). An 'open' status indicates that no rights are reserved. Omitted fields indicate that the reservation status has not been determined. These signals are designed for use within content identification and discovery protocols that provide additional identity, provenance, and trust context.
