## Changelog

### [0.3.9] - Unreleased

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
