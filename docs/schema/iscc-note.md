---
icon: lucide/file-check
title: ISCC Note
description: Permanent ISCC Declaration log record for HUB timestamping and registration.
---

# IsccNote Protocol Schema

An ISCC Declaration record submitted to an ISCC-HUB for timestamping and registration. IsccNote is the permanent, self-describing log entry that binds an ISCC-CODE to its content hashes and a cryptographic signature. Stored in an append-only log, declarations are immutable once accepted, so the record is version-pinned and carries resolvable schema and context URLs.

**JSON Schema**: [`iscc-note.json`](iscc-note.json)

!!! example "Minimal declaration"

    ```json
    {
      "$schema": "http://purl.org/iscc/schema/iscc-note-0.8.0.json",
      "iscc_code": "ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY",
      "datahash": "1e20253d0f3460085c276f038de345c8e953a306f4a07f9fa77f5af8563c3d7274c5",
      "nonce": "0013a3c214c05796673503e6e549446d",
      "signature": {
        "version": "ISCC-SIG v1.0",
        "controller": "did:web:example.com",
        "pubkey": "z6MkmeDbeC5BecFmVnTHA5PWEBaVUrGLdB3weGE2KYnXfHso",
        "proof": "z5j9nrpPw3oYSAN4XbCvk2sUtkwrueTD6V2Y35gS1KFTode2ED2YQWokPmoXw6QBYtYEFxtAQfzBhdNyr8PMwP79G"
      }
    }
    ```

!!! example "Complete declaration (all fields)"

    ```json
    {
      "$schema": "http://purl.org/iscc/schema/iscc-note-0.8.0.json",
      "iscc_code": "ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY",
      "datahash": "1e20253d0f3460085c276f038de345c8e953a306f4a07f9fa77f5af8563c3d7274c5",
      "nonce": "0013a3c214c05796673503e6e549446d",
      "timestamp": "2025-08-12T14:30:00.123Z",
      "signature": {
        "version": "ISCC-SIG v1.0",
        "controller": "did:web:example.com",
        "keyid": "key-1",
        "pubkey": "z6MkmeDbeC5BecFmVnTHA5PWEBaVUrGLdB3weGE2KYnXfHso",
        "proof": "z5j9nrpPw3oYSAN4XbCvk2sUtkwrueTD6V2Y35gS1KFTode2ED2YQWokPmoXw6QBYtYEFxtAQfzBhdNyr8PMwP79G"
      },
      "units": [
        "ISCC:IADSKPIPGRQAQXBHN4BY3Y2FZDUVHIYG6SQH7H5HP5NPQVR4HVZHJRI",
        "ISCC:GADUCK27AIQUBLC3ALIINORUJ6JEC4GHRWXSXLIO5VLKRE65RM6A5RI",
        "ISCC:AADWN77F727NXSUSUVDFOUS64JFPMZ4GAR5NJ3O5P563LTMXWS5XNSQ"
      ],
      "metahash": "1e208bad08ad56b5517e09bc8bc5e2281b2d8f21d096939a310f539cf5007d443772",
      "gateway": "https://gateway.example.com/declaration/{iscc_id}"
    }
    ```

**Required fields**: `$schema`, `iscc_code`, `datahash`, `nonce`, `signature`

## Field Reference

## **@context**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| @context | `string-uri` | http://purl.org/iscc/context | The JSON-LD Context URI for ISCC metadata.         |

## **@type**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| @type | `string` | IsccNote | The type of protocol metadata.         |

## **$schema**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| $schema | `string-uri` | http://purl.org/iscc/schema/iscc-note-0.8.0.json | The JSON Schema URI for ISCC Declaration metadata.         |

## **iscc_code**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| iscc_code | `string` | none | The ISCC-CODE identifying the digital content being declared. Mapped to JSON-LD @id, making it the RDF subject of the declaration. Supports full-length 256-bit ISCC-CODEs.<br><br>**Example**: `ISCC:KACYPXW445FTYNJ3CYSXHAFJMA2HUWULUNRFE3BLHRSCXYH2M5AEGQY`         |

## **datahash**
<http://purl.org/iscc/terms/#datahash>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| datahash | `string` | none | A blake3 multihash of the digital content, hex-encoded with the `1e20` multihash prefix (blake3, 32-byte digest). Binds the declaration to the exact content bytes.<br><br>**Example**: `1e20253d0f3460085c276f038de345c8e953a306f4a07f9fa77f5af8563c3d7274c5`         |

## **nonce**
<http://purl.org/iscc/terms/#nonce>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| nonce | `string` | none | Cryptographic nonce for replay protection. A 128-bit random value encoded as lowercase hexadecimal.<br><br>**Example**: `0013a3c214c05796673503e6e549446d`         |

## **timestamp**
<http://purl.org/iscc/terms/#timestamp>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| timestamp | `string` | none | RFC 3339 timestamp of declaration creation in UTC with millisecond precision. Optional on submission - an ISCC-HUB assigns the authoritative timestamp on receipt.<br><br>**Example**: `2025-08-12T14:30:00.123Z`         |

## **signature**
<http://purl.org/iscc/terms/#signature>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| signature | `object` | none | Cryptographic signature over the IsccNote, conforming to the [iscc-crypto](https://github.com/iscc/iscc-crypto) signing protocol. Uses EdDSA (Ed25519) with JCS canonicalization.         |

## **units**
<http://purl.org/iscc/terms/#units>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| units | `array` | none | The individual full-length ISCC-UNITs that compose the declared ISCC-CODE, enabling similarity matching against the declaration. One to four 256-bit ISCC-UNITs.<br><br>**Example**: `['ISCC:IADSKPIPGRQAQXBHN4BY3Y2FZDUVHIYG6SQH7H5HP5NPQVR4HVZHJRI']`         |

## **metahash**
<http://purl.org/iscc/terms/#metahash>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| metahash | `string` | none | A blake3 multihash of the seed metadata, hex-encoded with the `1e20` multihash prefix (blake3, 32-byte digest). Same format as `datahash`.<br><br>**Example**: `1e208bad08ad56b5517e09bc8bc5e2281b2d8f21d096939a310f539cf5007d443772`         |

## **gateway**
<http://purl.org/iscc/terms/#gateway>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| gateway | `string` | none | An HTTP(S) URL or RFC 6570 URI template of a gateway that serves metadata for the declared ISCC. Used by ISCC resolvers to discover content metadata.<br><br>**Example**: `https://gateway.example.com/declaration/{iscc_id}`         |

