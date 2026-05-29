### **datahash**

!!! term "<small><http://purl.org/iscc/terms/#datahash></small>"

    A blake3 multihash of the digital content, hex-encoded with the `1e20` multihash prefix (blake3, 32-byte digest). Binds the declaration to the exact content bytes.

### **nonce**

!!! term "<small><http://purl.org/iscc/terms/#nonce></small>"

    Cryptographic nonce for replay protection. A 128-bit random value encoded as lowercase hexadecimal.

### **timestamp**

!!! term "<small><http://purl.org/iscc/terms/#timestamp></small>"

    RFC 3339 timestamp of declaration creation in UTC with millisecond precision. Optional on submission - an ISCC-HUB assigns the authoritative timestamp on receipt.

### **signature**

!!! term "<small><http://purl.org/iscc/terms/#signature></small>"

    Cryptographic signature over the IsccNote, conforming to the [iscc-crypto](https://github.com/iscc/iscc-crypto) signing protocol. Uses EdDSA (Ed25519) with JCS canonicalization.

### **units**

!!! term "<small><http://purl.org/iscc/terms/#units></small>"

    The individual full-length ISCC-UNITs that compose the declared ISCC-CODE, enabling similarity matching against the declaration. One to four 256-bit ISCC-UNITs.

### **metahash**

!!! term "<small><http://purl.org/iscc/terms/#metahash></small>"

    A blake3 multihash of the seed metadata, hex-encoded with the `1e20` multihash prefix (blake3, 32-byte digest). Same format as `datahash`.

### **gateway**

!!! term "<small><http://purl.org/iscc/terms/#gateway></small>"

    An HTTP(S) URL or RFC 6570 URI template of a gateway that serves metadata for the declared ISCC. Used by ISCC resolvers to discover content metadata.

