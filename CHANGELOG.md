## Changelog

### 0.7.0 - 2026-06-01

This release adds the **Protocol** schema category (ISCC Discovery Protocol wire records) alongside
the existing Metadata, Seed, and Service categories, introduces an **STM** seed schema for scholarly
works, makes compact self-describing JSON the default for seed and protocol records, and version-pins
the `$schema` and `@context` of every standalone schema. The `$schema` reference makes compact data
recoverable to JSON-LD on demand, conformant with IEP-0002 which accepts both `application/json` and
`application/ld+json` as meta element formats.

**Breaking changes:**
- **`IsccMeta` is unaffected.** It still defaults to `ld=True` and serializes full JSON-LD exactly as
  before. The breaking changes below apply only to the standalone Seed/Service/Protocol models.
- Seed models (ISBN, ISRC, STM) now default to **compact JSON** (`ld=False`): `.dict()`, `.json()`,
  and `.jcs()` emit `$schema` only, with no `@context`/`@type`. Pass `ld=True` to restore full JSON-LD.
- Standalone schema `$schema` URLs are now **version-pinned** (e.g. `…/isbn-0.7.0.json`,
  `…/tdm-0.7.0.json`, `…/iscc-note-0.7.0.json`). Code that matched the old unversioned `$schema`
  string must account for the `-X.Y.Z` suffix. `recover_context()` resolves both forms, so v0.6.0
  records still recover.
- `$schema` is now a **required** field on the ISBN, ISRC, STM, and IsccNote schemas (auto-populated
  from its const default on construction, so existing construction code keeps working).

**New schemas:**
- Added **IsccNote** protocol schema (exported as `iscc_schema.IsccNote`) — the permanent ISCC
  Declaration log record for the ISCC Discovery Protocol HUB, and the first member of the new
  Protocol category. Serializes to compact JSON by default and requires `$schema` as the sole version
  anchor; `$schema` is part of the signed `jcs()` bytes, pinning the schema version into the signed
  record. Required: `$schema`, `iscc_code`, `datahash`, `nonce`, `signature`.
- Added **STM** seed schema (exported as `iscc_schema.STM`) — Scientific/Technical/Medical seed
  metadata for DOI-identified scholarly works, for interoperable Meta-Code generation (IEP-0002).
  Required: `doi`, `resource_type`, `title`, `publisher`, `pubyear`. Optional: `version_type` (NISO
  JAV stage), `container_title`, `issn`. `resource_type` carries 17 DataCite-style work-type tokens
  mapped to resolvable schema.org/FaBiO class IRIs.

**Serialization:**
- Added `ld` parameter to `.dict()`, `.json()`, `.jcs()` for controlling JSON-LD output
- Seed models (ISBN, ISRC, STM) default to `ld=False` (compact JSON with `$schema` only)
- Service models (TDM, GenAI) default to `ld=True` (full JSON-LD for registry/gateway interop)
- Protocol model (IsccNote) defaults to `ld=False` (compact JSON, `$schema` as version anchor)
- IsccMeta defaults to `ld=True` (full JSON-LD, backward compatible)
- Changed seed metadata examples to compact recoverable JSON format (no `@context`/`@type`)
- Added "Recommended Format" documentation to ISBN and ISRC schema pages
- Added code-gen post-processing for const field defaults and `_default_ld` class attribute
- `.json()` now accepts an `indent` argument for pretty-printing compact records and forwards
  `exclude_unset`, so the compact path offers the same formatting controls as the JSON-LD path

**Fixes:**
- End-anchored the IsccNote `gateway` URL pattern (`$`) so values with embedded whitespace or
  trailing characters are rejected rather than silently accepted into a permanent declaration record
- Corrected the IsccNote `@type` description ("service metadata" → "protocol metadata")

**Versioning:**
- All standalone schemas (seed, service, protocol) now uniformly version both `$schema` and the
  default `@context`, and write a version-pinned archive (`<name>-0.7.0.json`) next to the latest
  file; the latest file keeps an unversioned `$id`
- Added `x-iscc-jsonld` extension to every standalone JSON Schema documenting the JSON-LD upgrade
  path (versioned context URL, `@type`, human-readable recipe) for compact records
- Versioned the `@context`/`$schema` URLs shown in the main IsccMeta docs example

**Field status & tooling:**
- Promoted `$schema`, `nonce`, `signature`, `generator`, and `tdm_reservation` to `stable`
- Documented the field-stability contract (stable/draft, one-way promotion) and the bump-first
  release workflow in the versioning guide
- Added a release-archive build guard: the schema and context builds abort if a git tag already
  exists for the current version, preventing silent mutation of released archives (fails open when
  git is unavailable)

**Documentation:**
- Templated the version string in hand-written docs (guide, examples, versioning) via Zensical's
  `macros` extension, so version-pinned example URLs derive from `iscc_schema.__version__` and never
  go stale on a release bump; the `{{ version }}` variable is supplied by `tools/docs_macros.py`
- Made the README version-free (it renders on GitHub/PyPI where macros do not run) and taught the
  `llms-full.txt` generator to resolve the version token

### 0.6.0 - 2026-05-26
- Replaced five per-category TDM fields (train, inference, derive, search, analyze) with two W3C TDMRep-conformant fields (tdm_reservation, tdm_policy)
- Added `tdm_reservation` integer field (0/1) bound to `http://www.w3.org/ns/tdmrep#reservation`
- Added `tdm_policy` URI field bound to `http://www.w3.org/ns/tdmrep#policy`
- Changed embedded `tdm` wrapper to use JSON-LD `@nest` semantics (no intermediate blank node in RDF expansion)
- Added `iscc` field to standalone TDM schema for binding declarations to content by ISCC-CODE or ISCC-ID
- Embedded and standalone TDM objects now allow additional properties for backward compatibility with v0.5.0 payloads
- Fixed `empty_string_to_default` validator coercing integer 0 to None (now only exempts int, not bool/list/dict)
- Per-category fields deferred until IETF AIPREF vocabulary stabilizes (target August 2026)

### 0.5.0 - 2026-03-17
- Migrated documentation from mkdocs-material to zensical
- Added ISCC brand theming (header, footer, dark mode, logo)
- Added copy-page button for LLM-friendly markdown export
- Added ISCC-AI copilot widget integration
- Added llms.txt and per-page markdown generation for LLM consumption
- Added "For Coding Agents" reference page
- Added GitHub Pages deployment workflow
- Added navigation icons and short titles to all doc pages
- Added Open Graph and Twitter Card meta tags
- Added Plausible analytics via theme override
- Added `x-iscc-status` (stable/draft) to all fields across YAML schemas
- Rendered `x-iscc-status` in generated schema docs, vocabulary page, and terms includes
- Added `datasize` field for data processed size when ISCC is computed over sub-file data (e.g., bioimage planes)
- Added GenAI Service Metadata schema for generative AI disclosure signals (involvement, ai_system, digital_source_type)
- Added `genai` field to IsccMeta for embedding AI transparency signals in content metadata
- Moved `tdm` field from iscc-embeddable to iscc-extended (structured objects don't belong in media-embeddable metadata)
- Added `form` field for content-kind classification using Schema.org CreativeWork subtypes
- Pydantic models now emit versioned `$schema` and `@context` URLs (e.g., `http://purl.org/iscc/schema/0.5.0.json`)
- Standalone schema models (ISBN, ISRC, TDM) now emit versioned `@context` URLs
- Added versioning documentation page
- Embedded JSON-LD `@context` directly into JSON Schema files for self-contained validation and semantic mapping
- Added schema-specific `@context` to standalone schemas (isbn, isrc, tdm) with only their relevant terms
- Patched `@context` property in JSON Schemas to accept both URI string and inline object per JSON-LD spec
- Added `recover_context()` function for schema-driven JSON-LD context recovery from plain JSON data
- Added generated `contexts.py` module with bundled context data and type-to-schema mappings
- Reordered build pipeline so `buildcontext` runs before `buildschema`
- Added ISBN and ISRC Seed Metadata schemas for interoperable Meta-Code generation (IEP-0002)
- Added TDM Service Metadata schema for machine-readable TDM reservation signals (train, inference, derive, search, analyze)
- Added `tdm` field to IsccMeta for embedding TDM reservation metadata in content descriptions
- Reframed TDM schema as reservation policy signals aligned with EU DSM Directive Art. 4 opt-out
- Made TDM fields optional (omitted field = reservation status not determined)
- Added `additionalProperties: false` to TDM schema for strict validation
- Replaced legally loaded terminology in TDM field descriptions (e.g., "derivative works" → "content transformation")
- Introduced three-category schema framework: ISCC Metadata, Seed Metadata, Service Metadata
- Added per-schema documentation pages with JSON Schema links and field reference tables
- Added Seed and Service Metadata terms to JSON-LD context and vocabulary documentation
- Fixed misleading ISCC Metadata description (content vocabulary, not declaration schema)
- Added `x-iscc-standard` extension field to mark ISO 24138:2024 properties in YAML schemas
- Surfaced ISO 24138:2024 annotations in generated schema docs, vocabulary page, and terms includes
- Added `iscc_code` field as explicit alternative to the compact `iscc` field
- Added `nonce` field for cryptographic replay protection
- Added `signature` field to IsccMeta for iscc-crypto compatibility (EdDSA/JCS signing)
- Added `units` field for individual ISCC-UNITs that make up a composite ISCC-CODE
- Added `text` field for extracted plaintext of digital content
- Widened `parts` field to accept both strings and objects
- Added `minLength: 1` to `name` and `description` fields
- Fixed `keywords` description typo ("sting" → "string")
- Eliminated `iscc-collection.yaml` duplication; JSON Schema is now auto-generated from individual schema files
- Fixed JSON-LD identifier collision: `iscc_id` and `media_id` now have distinct ISCC term mappings
- Fixed URI-typed fields in JSON-LD context to use `@type: @id` for proper linked data processing
- Added missing `mode` field to JSON-LD context
- Fixed stale 0.3.2 version defaults in generator reference schema
- Fixed missing `x-iscc-status` and `x-iscc-context` annotations in JSON Schema output
- Exported `Signature` model from package
- Migrated from Poetry to uv with hatchling build backend
- Dropped Pydantic v1, migrated to native Pydantic v2 (closes #36)
- Require Python >=3.10,<3.15
- Added Python 3.13 and 3.14 to CI test matrix
- Switched CI to ubuntu-latest
- Suppressed datamodel-code-generator warnings and cleaned up build output
- Updated .gitignore to comprehensive Python template

### 0.4.1 - 2024-01-21
- Added `credentials`-field
- Updated dependencies
- Add pydantic v2 compatibility

### 0.4.0 - 2022-11-24
- Added test for error on extra fields
- Added typing information to IsccMeta.iscc_obj property
- Updated definition of `meta`-field
- Updated dependencies

### 0.3.9 - 2022-07-03
- Fixed identifier element to support stings and list of strings
- Add string/list support for creators and keywords fields
- Updated dependencies

### 0.3.8 - 2022-06-08
- Updated dependencies
- Refactor NFT reference to support CAIP-22 and CAIP-29 standards

### 0.3.7 - 2022-04-10
- Added new nft_chain, nft_contract, nft_token fields
- Moved changelog
- Updated examples

### 0.3.6 - 2022-03-19
- Use customized BaseModel for IsccMeta
- Convert empty strings to `None`
- Exclude `None` and unset in IsccMeta.dict() by default
- Exclude `None` and use by_alis in IsccMeta.json()
- Added IsccMeta.jcs() serialization
- Added IsccMEta.iscc_obj property
- Fixed JSON Schema code generation
- Moved thumbnail field to the bottom
- Added `media_id` vendor identifier
- Added `iscc_id` field
- Updated OpenAPI definitions.

### 0.3.5 - 2022-03-11
- Added custom field AnyUrl to support Data-URLs
- Fix typo in NftFrozen
- Change endpoint /freeze to /nft/freeze


### 0.3.4 - 2022-03-08
- Mark stable fields
- Change `iscc` field to not required
- Add schema.org context to `thumbnail` field
- Updated dependencies

### 0.3.3 - 2022-03-06
- Fixed typo in `acquire` field
- Renamed main schema class `ISCC` to `IsccMeta`
- Import schemas to package top-level
- Updated dependencies

### 0.3.2 - 2022-03-01
- Redesigned Generator API model
- Added `mode` element
- Added `thumbnail` element
- Added versioned context and schema URIs
- Added `$schema` element to context
- Renamed `verify` to `verifications`

### 0.3.1 - 2022-02-10
- Fixed packaging error

### 0.3.0 - 2022-02-10
- Added draft API for ISCC Generator Service
- Added new collection schema
- Updated dependencies
- Added new terms: verify, original, redirect

### 0.2.1 - 2022-01-19
- Tweak code generator
- Cleanup dependencies

### 0.2.0 - 2022-01-17
- Added generator field
- Changed properties field to support base64
- Changed iscc validation to support Semantic-Code

### 0.1.0 - 2022-01-05
- Initial release
