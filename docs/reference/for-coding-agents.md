---
icon: lucide/bot
description: Prescriptive reference for AI coding agents — architecture, constraints, decision rules, task recipes, and change playbooks.
---

# For Coding Agents

Dense, prescriptive reference for AI coding agents working on or integrating with **iscc-schema**.

## Architecture Map

### File Layout

| Path | Contents | Editable? |
|------|----------|-----------|
| `iscc_schema/__init__.py` | Public API exports: `IsccMeta`, `Signature`, `ISBN`, `ISRC`, `TDM`, `GenAI`, `recover_context` | Yes |
| `iscc_schema/base.py` | Custom `BaseModel` — serialization (`dict`, `json`, `jcs`), empty-string-to-None coercion | Yes |
| `iscc_schema/fields.py` | RFC 3986-compliant `AnyUrl` type with regex validation | Yes |
| `iscc_schema/recovery.py` | `recover_context()` — reconstruct `@context` from `$schema` or `@type` | Yes |
| `iscc_schema/aliases.json` | Maps `@context`→`context_`, `@type`→`type_`, `$schema`→`schema_` | Yes |
| `iscc_schema/schema.py` | **Generated** — main `IsccMeta` Pydantic v2 model | No |
| `iscc_schema/generator.py` | **Generated** — OpenAPI models for ISCC Generator API | No |
| `iscc_schema/seed_isbn.py` | **Generated** — `ISBN` model | No |
| `iscc_schema/seed_isrc.py` | **Generated** — `ISRC` model | No |
| `iscc_schema/service_tdm.py` | **Generated** — `TDM` model | No |
| `iscc_schema/service_genai.py` | **Generated** — `GenAI` model | No |
| `iscc_schema/contexts.py` | **Generated** — JSON-LD context mappings + `TYPE_SCHEMAS` dispatch | No |
| `iscc_schema/models/*.yaml` | **Source of truth** — OpenAPI 3.1.0 schema definitions | Yes |
| `iscc_schema/models/iscc-all.yaml` | Composition manifest (`allOf` + `$ref` to individual schemas) | Yes |
| `tools/build_code.py` | Code generation: YAML → datamodel-code-generator → Pydantic + post-processing | Yes |
| `tools/build_json_schema.py` | Flatten individual YAML schemas into merged `iscc.json` | Yes |
| `tools/build_json_ld_context.py` | Generate JSON-LD context files from model metadata | Yes |
| `tools/build_terms.py` | Generate vocabulary markdown from `x-iscc-context` fields | Yes |
| `tools/build_docs.py` | Generate documentation pages from YAML schemas + README/CHANGELOG | Yes |
| `tools/format_yaml.py` | Reformat YAML (2-space indent, 88 width, LF) | Yes |

### Schema Composition

```
IsccMeta (iscc-all.yaml composes via allOf + $ref):
  ├── iscc-jsonld.yaml      → @context, @type, $schema
  ├── iscc-minimal.yaml     → iscc
  ├── iscc-basic.yaml       → name, description, meta
  ├── iscc-embeddable.yaml  → creator, license, credit, rights, acquire
  ├── iscc-extended.yaml    → media_id, iscc_id, image, keywords, form, version, tdm, genai
  ├── iscc-technical.yaml   → mode, filename, filesize, datasize, mediatype, duration, fps, width, height, created
  ├── iscc-crypto.yaml      → tophash, metahash, datahash, nonce, signature
  ├── iscc-nft.yaml         → external_url, animation_url, properties, attributes, nft
  └── iscc-declaration.yaml → original, redirect, chain, wallet, credentials, verifications

Standalone (NOT in IsccMeta):
  ├── isbn.yaml  → ISBN (seed metadata)
  ├── isrc.yaml  → ISRC (seed metadata)
  ├── tdm.yaml   → TDM  (service metadata; also inline in IsccMeta.tdm)
  └── genai.yaml → GenAI (service metadata; also inline in IsccMeta.genai)
```

### Import Dependency Flow

```
iscc_schema.__init__
  → iscc_schema.schema (generated) → iscc_schema.base → pydantic.BaseModel
                                    → iscc_schema.fields (AnyUrl)
  → iscc_schema.seed_isbn (generated) → iscc_schema.base
  → iscc_schema.seed_isrc (generated) → iscc_schema.base
  → iscc_schema.service_tdm (generated) → iscc_schema.base
  → iscc_schema.service_genai (generated) → iscc_schema.base
  → iscc_schema.recovery → iscc_schema.contexts (generated)
```

### Public API Exports

```python
from iscc_schema import IsccMeta      # Main metadata model (all fields)
from iscc_schema import Signature     # Cryptographic signature (nested)
from iscc_schema import ISBN          # Seed metadata
from iscc_schema import ISRC          # Seed metadata
from iscc_schema import TDM           # Service metadata
from iscc_schema import GenAI         # Service metadata
from iscc_schema import recover_context  # JSON-LD context recovery
```

## Decision Dispatch

### Which model to use?

| Use case | Model | Source YAML |
|----------|-------|-------------|
| General ISCC metadata | `IsccMeta` | `iscc-all.yaml` (composed) |
| ISBN-based Meta-Code generation | `ISBN` | `isbn.yaml` |
| ISRC-based Meta-Code generation | `ISRC` | `isrc.yaml` |
| TDM reservation signals | `TDM` | `tdm.yaml` |
| GenAI disclosure signals | `GenAI` | `genai.yaml` |
| API request/response models | `generator.py` models | `iscc-generator.yaml` |

### Which serialization method?

| Need | Method | Behavior |
|------|--------|----------|
| JSON-LD output | `meta.json()` | `by_alias=True` → `@context`, `@type`, `$schema` |
| Dict for processing | `meta.dict()` | `exclude_none=True`, `exclude_unset=True`, `by_alias=True` |
| Canonical bytes for signing | `meta.jcs()` | JCS-canonicalized JSON bytes |
| Pydantic v2 native | `meta.model_dump()` / `meta.model_dump_json()` | Used internally by `dict()` / `json()` |

### Which build command?

| Changed | Run |
|---------|-----|
| Any YAML schema | `uv run poe all` (full pipeline) |
| Only Python code (base.py, fields.py) | `uv run pytest` |
| Only build tool scripts | `uv run poe all` |
| Quick code regen only | `uv run poe buildcode` |
| Quick JSON Schema only | `uv run poe buildschema` |

## Constraints and Invariants

### Model Configuration

All models inherit from `iscc_schema.base.BaseModel` with:

- `extra="forbid"` — unknown fields raise `ValidationError`
- `validate_assignment=True` — assignment validates at runtime
- `use_enum_values=True` — enums serialize to string values
- `populate_by_name=True` — accept both `context_` and `@context`

### Empty String Coercion

The `@model_validator(mode="before")` in `base.py` converts empty strings to `None` for all fields. Combined with `exclude_none=True` in serialization, empty strings are silently dropped.

### URL Validation

`AnyUrl` in `fields.py` validates against RFC 3986. Accepts any scheme (http, https, ipfs, data, urn). Empty string → `None` via the empty-string coercion.

### Field Aliases

Three fields use aliases because `@` and `$` are invalid in Python identifiers:

| JSON property | Python field | Alias |
|---------------|-------------|-------|
| `@context` | `context_` | `@context` |
| `@type` | `type_` | `@type` |
| `$schema` | `schema_` | `$schema` |

### Extension Fields

| Extension | Values | Purpose |
|-----------|--------|---------|
| `x-iscc-context` | IRI string | JSON-LD context mapping for the property |
| `x-iscc-status` | `stable` / `draft` | Field maturity indicator |
| `x-iscc-standard` | Standard name | ISO/IPTC standard reference |
| `x-iscc-schema-doc` | Text | Original schema.org definition |
| `x-iscc-embed` | Text | Media embedding guidance |

### Generated File Post-Processing

`build_code.py` applies two patches after code generation:

1. **Import swap**: `pydantic.BaseModel` → `iscc_schema.base.BaseModel`, `pydantic.AnyUrl` → `iscc_schema.fields.AnyUrl`
2. **URL versioning**: `http://purl.org/iscc/context` → `http://purl.org/iscc/context/{version}.jsonld`, `http://purl.org/iscc/schema` → `http://purl.org/iscc/schema/{version}.json`

## Side Effects Catalog

| Method / Function | Effect |
|-------------------|--------|
| `IsccMeta(...)` | Validates all fields, coerces empty strings to None |
| `meta.dict()` | Pure — returns new dict, no mutation |
| `meta.json()` | Pure — returns JSON string, no mutation |
| `meta.jcs()` | Pure — returns canonical bytes, no mutation |
| `recover_context(data)` | Mutates input dict — adds `@context` key |
| `poe buildcode` | Overwrites `schema.py`, `generator.py`, seed/service modules |
| `poe buildschema` | Overwrites `docs/schema/*.json`, `iscc_schema/contexts.py` |
| `poe buildcontext` | Overwrites `docs/context/*.jsonld` |
| `poe buildterms` | Overwrites `docs/includes/terms-*.md` |
| `poe builddocs` | Overwrites `docs/index.md`, `docs/changelog.md`, `docs/schema/*.md`, `docs/context/index.md` |

## Task Recipes

### Add a new field to IsccMeta

1. Choose the appropriate YAML schema file in `iscc_schema/models/` based on the field's category
2. Add the property with type, description, and `x-iscc-*` extension fields
3. Add the field name to the `priority` list in `tools/build_json_schema.py` for property ordering
4. Run `uv run poe all` to regenerate everything and run tests
5. Verify the field appears in `schema.py`, `docs/schema/iscc.json`, and vocabulary docs

### Add a new standalone schema (seed or service)

1. Create `iscc_schema/models/{name}.yaml` with title, type, properties
2. Add to `SEED_SCHEMAS` or `SERVICE_SCHEMAS` dict in `tools/build_code.py`
3. Add to `SEED_SCHEMAS` or `SERVICE_SCHEMAS` lists in `tools/build_json_schema.py`
4. Add to the corresponding lists in `tools/build_json_ld_context.py`
5. Add to the corresponding lists in `tools/build_terms.py`
6. Add to the corresponding lists in `tools/build_docs.py`
7. Export the new model from `iscc_schema/__init__.py`
8. Run `uv run poe all`

### Recover JSON-LD context from plain JSON

```python
from iscc_schema import recover_context

data = {"iscc": "ISCC:KACYPXW445FTYNJ3", "name": "Example"}
data_with_context = recover_context(data)
# Adds @context from SCHEMA_CONTEXTS[SCHEMA_ISCC]
```

### Bypass validation (downstream pattern)

```python
meta = IsccMeta.model_construct(iscc="ISCC:...", name="...")
# No validation, no coercion — use only for trusted internal data
```

## Change Playbook

### If modifying a YAML schema property

- Run `uv run poe all` — regenerates code, JSON Schema, context, docs, runs tests
- Check generated `schema.py` for correct field type and alias
- Check `docs/schema/iscc.json` for correct property definition
- If property has `x-iscc-context`: check `docs/context/iscc.jsonld` and `contexts.py`

### If modifying base.py

- Run `uv run pytest` — tests cover serialization, coercion, JCS
- Check that `dict()`, `json()`, `jcs()` defaults still match expectations
- Downstream impact: iscc-sdk subclasses `IsccMeta` and uses `.construct()` extensively

### If modifying fields.py (AnyUrl)

- Run `uv run pytest` — tests cover URL validation patterns
- Check that valid URIs (http, ipfs, data, urn) still accepted
- Check that empty string → None coercion still works

### If modifying build_code.py

- Run `uv run poe buildcode && uv run pytest`
- Verify post-processing patches applied correctly in generated files
- Check import statements in `schema.py` reference `iscc_schema.base.BaseModel`

### If modifying build_json_schema.py

- Run `uv run poe buildschema`
- Verify `docs/schema/iscc.json` property order matches `priority` list
- Verify `contexts.py` regenerated with correct mappings
- Verify `@context` property accepts both URI string and inline object

### If adding a new x-iscc-* extension field

- Update all `tools/build_*.py` scripts that inspect extension fields
- Update `tools/build_docs.py` to render the new extension in documentation
- Run `uv run poe all`

## Common Mistakes

NEVER edit `schema.py`, `generator.py`, `seed_*.py`, `service_*.py`, or `contexts.py` directly — they are overwritten by `poe buildcode` / `poe buildschema`. ALWAYS edit the source YAML schemas and run the build pipeline.

---

NEVER add a new YAML schema field without adding it to the `priority` list in `tools/build_json_schema.py`. Fields missing from this list end up unsorted at the bottom of the generated JSON Schema.

---

NEVER use `pydantic.BaseModel` or `pydantic.AnyUrl` in hand-written code that extends iscc-schema. ALWAYS use `iscc_schema.base.BaseModel` and `iscc_schema.fields.AnyUrl` — they provide JSON-LD serialization, empty-string coercion, and RFC 3986 validation.

---

NEVER assume fields are present in serialized output. `exclude_none=True` and `exclude_unset=True` mean only explicitly set, non-None fields appear. ALWAYS check for key existence when consuming IsccMeta dicts.

---

NEVER pass `by_alias=False` to `dict()` or `json()` unless you specifically need Python field names (`context_`, `type_`, `schema_`). The default `by_alias=True` produces JSON-LD compatible output with `@context`, `@type`, `$schema`.

---

NEVER add a standalone schema without updating ALL five build scripts (`build_code.py`, `build_json_schema.py`, `build_json_ld_context.py`, `build_terms.py`, `build_docs.py`). Missing any one causes incomplete output.
