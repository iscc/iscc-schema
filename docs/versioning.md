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

## Field Stability

Every schema property is annotated with an `x-iscc-status` of either `stable` or `draft`. This
status is surfaced in the vocabulary documentation as a **Status** badge.

- **Stable** fields are covered by the semver compatibility guarantees above. They will not be
  removed or have their type or semantics changed in a minor version. Additive changes (relaxing
  constraints, adding enum values) are permitted in minor versions; breaking changes require a
  major version bump.

- **Draft** fields carry no compatibility guarantee between minor versions. They may be renamed,
  retyped, or removed without a major version bump. Implementors who depend on draft fields should
  pin to a specific schema version and re-test against new releases before upgrading.

- Promotion from `draft` to `stable` is one-way and happens at release boundaries. Once a field is
  `stable` it is not demoted back to `draft`.

- Standalone schemas (ISBN, ISRC, STM, TDM, GenAI, IsccNote) are versioned as a whole via semver.
  Their field-level `x-iscc-status` follows the same contract: a stable field in a standalone
  schema is covered by the package's semver guarantees.

## Standalone Schemas

Seed, service, and protocol schemas (ISBN, ISRC, STM, TDM, GenAI, IsccNote) follow the same
versioned-URL strategy as the main schema, with per-schema names. Every serialized record carries a
versioned `$schema` (e.g., `http://purl.org/iscc/schema/isbn-0.7.0.json`); records serialized as
full JSON-LD additionally carry a versioned `@context` (e.g.,
`http://purl.org/iscc/context/0.7.0.jsonld`). Seed and protocol schemas default to compact JSON
(`$schema` only), while service schemas default to full JSON-LD (see below) — pinning the schema
version, and the vocabulary version where an `@context` is present, to a specific release.

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

## Release Workflow

When starting work on a new version, the **first commit** on the feature branch bumps the version
in `pyproject.toml` and `iscc_schema/__init__.py` to the target release. This guarantees the build
pipeline writes to fresh versioned archive filenames from the start and never overwrites the
archives of an already-released version.

The discipline is enforced in two places:

- A **build guard** (`_check_version_not_released`) runs at the top of the JSON Schema and JSON-LD
  context builds. If a `v<version>` git tag already exists for the current version, the build aborts
  with an error telling you to bump the version first. Local tags mirror the GitHub releases after a
  fetch or pull, so the check needs no network access.
- A **test** (`tests/test_versioning.py`) verifies that `pyproject.toml` and
  `iscc_schema.__version__` agree, and that, once a version is tagged, its versioned archive files
  on disk stay byte-identical to the content committed at that tag.
