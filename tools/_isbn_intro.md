## Recommended Format

For Meta-Code generation ([IEP-0002](https://github.com/iscc/iscc-ieps/blob/main/ieps/iep-0002.md)),
use compact JSON with a `$schema` reference. The `@context` and `@type` fields are not required -
they can be recovered from the schema on demand via
[Schema-Driven Context Recovery](../guide.md#schema-driven-context-recovery).

This is fully conformant with IEP-0002, which accepts both `application/json` and
`application/ld+json` as meta element formats. The compact form keeps data lean while remaining
self-describing through the `$schema` link.
