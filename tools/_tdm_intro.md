## Overview

Under EU copyright law
([DSM Directive, Article 4](https://eur-lex.europa.eu/eli/dir/2019/790/oj)),
text and data mining of lawfully accessed content is permitted by default - including for
commercial AI training. Rightsholders who do not expressly reserve their rights in a
machine-readable manner have no legal basis to prevent such use.
The [AI Act, Article 53](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) reinforces this by
requiring GPAI providers to identify and comply with TDM reservations.

The [W3C TDMRep](https://www.w3.org/community/reports/tdmrep/CG-FINAL-tdmrep-20240510/) protocol
defines two properties for this purpose - `tdm-reservation` (integer 0/1) and `tdm-policy` (URL) -
deliverable via well-known files, HTTP headers, HTML meta tags, EPUB metadata, and PDF XMP.

This schema carries the same TDMRep signals through a sixth channel: **content-addressed
lookup** using [ISCC](https://iscc.io) (ISO 24138:2024). A consumer can compute an ISCC
fingerprint from any file and query an ISCC registry for its TDM status - even when the file has
been redistributed, reformatted, or stripped of embedded metadata.

### W3C TDMRep Conformance

The schema fields map directly to the
[W3C TDMRep namespace](https://www.w3.org/ns/tdmrep) (`http://www.w3.org/ns/tdmrep#`):

| ISCC field | TDMRep property | Namespace IRI |
|---|---|---|
| `tdm_reservation` | `tdm-reservation` | `http://www.w3.org/ns/tdmrep#reservation` |
| `tdm_policy` | `tdm-policy` | `http://www.w3.org/ns/tdmrep#policy` |

JSON-LD expansion of an ISCC TDM declaration produces the same RDF predicates as TDMRep signals
embedded in EPUB or PDF content. The `tdm_policy` field links to standard
[TDMRep ODRL policy](https://www.w3.org/community/reports/tdmrep/CG-FINAL-tdmrep-20240510/#sec-tdm-policy)
documents - existing publisher policies work without modification.

### Embedded and Standalone Forms

TDM signals appear in two forms within the ISCC ecosystem:

- **Standalone** (`@type: TDM`) - Served by ISCC registries as independent JSON-LD documents, bound
  to content via the `iscc` field which becomes the RDF subject (`@id`)
- **Embedded** - Nested inside ISCC Metadata declarations under a `tdm` wrapper key, using JSON-LD
  [`@nest`](https://www.w3.org/TR/json-ld11/#nested-properties) semantics (nested properties
  promote to the parent subject - no intermediate blank node)

Both forms share one JSON-LD context and expand to identical RDF triples on the two TDMRep
predicates.
