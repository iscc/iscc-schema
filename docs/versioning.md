---
icon: lucide/git-branch
title: Versioning
description: Schema versioning strategy, URL patterns, and compatibility guarantees.
---

# Schema Versioning

## Version Numbers

iscc-schema uses semantic versioning:

- **Patch** (0.5.0 -> 0.5.1): Bug fixes, documentation updates. No schema changes.
- **Minor** (0.5.x -> 0.6.0): Additive changes (new optional fields, new standalone schemas).
  Backward compatible: data produced by older versions validates against the new schema.
- **Major** (0.x -> 1.0): Breaking changes (removed/renamed fields, changed types, changed
  required fields). Documented in changelog with migration guidance.

## URL Strategy

Each schema artifact has two URL forms:

| Form | Example | Resolves to |
|------|---------|-------------|
| Unversioned | `http://purl.org/iscc/schema` | Latest version (redirect) |
| Versioned | `http://purl.org/iscc/schema/0.5.0.json` | Pinned version |

The same pattern applies to JSON-LD contexts:

| Form | Example | Resolves to |
|------|---------|-------------|
| Unversioned | `http://purl.org/iscc/context` | Latest version (redirect) |
| Versioned | `http://purl.org/iscc/context/0.5.0.jsonld` | Pinned version |

**Serialized ISCC data always carries versioned URLs.** The Pydantic models produce versioned
`$schema` and `@context` URLs by default, so you can always identify which schema version
produced a given piece of data.

The unversioned URLs are for documentation, human convenience, and "give me the latest" use
cases.

## Compatibility Guarantees

- Minor version bumps are additive only: data produced by an older version validates against
  the new schema.
- Consumers should accept both versioned and unversioned URLs gracefully.
- The `recover_context()` function resolves both versioned and unversioned URLs to the bundled
  JSON-LD context of the installed package version.

## Standalone Schemas

Seed, service, and protocol schemas (ISBN, ISRC, TDM, GenAI, IsccNote) follow the same
versioned-URL strategy as the main schema, with per-schema names. Serialized records carry a
versioned `@context` (e.g., `http://purl.org/iscc/context/0.7.0.jsonld`) **and** a versioned
`$schema` (e.g., `http://purl.org/iscc/schema/isbn-0.7.0.json`), pinning both the vocabulary and
the schema version to a specific release.

The latest schema document is published at the unversioned URL (its `$id`, e.g.,
`http://purl.org/iscc/schema/isbn.json`), while its `$schema` const points at the versioned
archive so records always carry the version. A version-pinned archive copy is written alongside
each latest file (e.g., `isbn-0.7.0.json` next to `isbn.json`), preserving the schema as it
existed at that release. `recover_context()` resolves both unversioned `$schema` URLs (older
records, or the "latest" document URL) and versioned archive URLs to the bundled JSON-LD context.

## Protocol Schemas

Protocol schemas (IsccNote) serialize to compact JSON by default: the `@context` and `@type`
fields are dropped, leaving the versioned `$schema` as the **sole** version anchor. For these
schemas `$schema` is therefore a **required** field.

This matters because protocol records are permanent, signed log entries: the `$schema` value is
part of the JCS bytes the signature is computed over, so the schema version is pinned into the
signed record itself.
