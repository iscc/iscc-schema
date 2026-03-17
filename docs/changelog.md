## Changelog

### [0.5.0] - 2026-03-17
- Added ISBN and ISRC Seed Metadata schemas for interoperable Meta-Code generation (IEP-0002)
- Added TDM Service Metadata schema for AI content usage rights (train, inference, derive, search, analyze)
- Added `tdm` field to IsccMeta for embedding TDM reservation metadata in content descriptions
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

### [0.4.1] - 2024-01-21
- Added `credentials`-field
- Updated dependencies
- Add pydantic v2 compatibility

### [0.4.0] - 2022-11-24
- Added test for error on extra fields
- Added typing information to IsccMeta.iscc_obj property
- Updated definition of `meta`-field
- Updated dependencies

### [0.3.9] - 2022-07-03
- Fixed identifier element to support stings and list of strings
- Add string/list support for creators and keywords fields
- Updated dependencies

### [0.3.8] - 2022-06-08
- Updated dependencies
- Refactor NFT reference to support CAIP-22 and CAIP-29 standards

### [0.3.7] - 2022-04-10
- Added new nft_chain, nft_contract, nft_token fields
- Moved changelog
- Updated examples

### [0.3.6] - 2022-03-19
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

### [0.3.5] - 2022-03-11
- Added custom field AnyUrl to support Data-URLs
- Fix typo in NftFrozen
- Change endpoint /freeze to /nft/freeze


### [0.3.4] - 2022-03-08
- Mark stable fields
- Change `iscc` field to not required
- Add schema.org context to `thumbnail` field
- Updated dependencies

### [0.3.3] - 2022-03-06
- Fixed typo in `acquire` field
- Renamed main schema class `ISCC` to `IsccMeta`
- Import schemas to package top-level
- Updated dependencies

### [0.3.2] - 2022-03-01
- Redesigned Generator API model
- Added `mode` element
- Added `thumbnail` element
- Added versioned context and schema URIs
- Added `$schema` element to context
- Renamed `verify` to `verifications`

### [0.3.1] - 2022-02-10
- Fixed packaging error

### [0.3.0] - 2022-02-10
- Added draft API for ISCC Generator Service
- Added new collection schema
- Updated dependencies
- Added new terms: verify, original, redirect

### [0.2.1] - 2022-01-19
- Tweak code generator
- Cleanup dependencies

### [0.2.0] - 2022-01-17
- Added generator field
- Changed properties field to support base64
- Changed iscc validation to support Semantic-Code

### [0.1.0] - 2022-01-05
- Initial release
