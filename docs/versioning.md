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

Standalone schemas (ISBN, ISRC, TDM) use schema-specific `$schema` URLs that are not versioned
per release (e.g., `http://purl.org/iscc/schema/isbn.json`). Their `@context` URLs are versioned
to pin the context mapping to a specific package version.
