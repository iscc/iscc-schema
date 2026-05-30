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

## Identifiers vs. Locators

ISCC URLs play two distinct roles. Conflating them is what makes the `http`-vs-`https` choice
feel ambiguous:

- **Identity** — the IRI that *names* a term, context, or schema: the `@context` value, every
  `@type` and term IRI, and the `$schema` value carried in records. In JSON-LD/RDF these are
  compared by exact string match ([RDF 1.1 Concepts §3.1](https://www.w3.org/TR/rdf11-concepts/#section-IRIs)),
  so the scheme is part of the identifier — `http://schema.org/name` and
  `https://schema.org/name` are **different** properties. ISCC identity IRIs are `http://` and
  are **frozen**: changing the scheme would mint a new, incompatible term, break graph merges
  with the dominant `http://schema.org/` vocabulary, and — for signed protocol records —
  invalidate the signature, because `$schema` is part of the JCS bytes the signature is computed
  over.

- **Location** — where the bytes are actually served. The identity IRIs resolve through a
  purl.org redirect to the hosting server, which is served over **https**. The scheme used to
  *fetch* a document is independent of the IRI's identity and can be upgraded freely.

In short: identity IRIs stay `http://` for stability and signature integrity; resolution and
hosting use `https`. The single `https` identity value is the JSON Schema dialect
(`https://json-schema.org/draft/2020-12/schema`), which is the canonical 2020-12 meta-schema IRI.

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
versioned `$schema` (e.g., `http://purl.org/iscc/schema/isbn-{{ version }}.json`); records serialized as
full JSON-LD additionally carry a versioned `@context` (e.g.,
`http://purl.org/iscc/context/{{ version }}.jsonld`). Seed and protocol schemas default to compact JSON
(`$schema` only), while service schemas default to full JSON-LD (see below) — pinning the schema
version, and the vocabulary version where an `@context` is present, to a specific release.

The latest schema document is published at the unversioned URL (its `$id`, e.g.,
`http://purl.org/iscc/schema/isbn.json`), while its `$schema` const points at the versioned
archive so records always carry the version. A version-pinned archive copy is written alongside
each latest file (e.g., `isbn-{{ version }}.json` next to `isbn.json`), preserving the schema as it
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
