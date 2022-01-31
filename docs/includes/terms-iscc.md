### **metadata**

!!! term "<small><http://purl.org/iscc/terms/#metadata></small>"

    Descriptive, industry-sector or use-case specific metadata. **Used as input for ISCC Meta-Code generation**. Can be any object that is JSON/JCS serializable. If `metadata` is provided it is used as an input for Meta-Code generation and as the sole input for the cryptographic `metahash` calculation. If `metadata` is set to a string it is assumed that it is base64 encoded binary file metadata.

### **redirect**

!!! term "<small><http://purl.org/iscc/terms/#redirect></small>"

    URL to which a resolver should redirect an ISCC-ID that has been minted from a declartion that includes the IPFS-hash of this metadata instance. **Supports URI template `{iscc-id}`**.

### **previous**

!!! term "<small><http://purl.org/iscc/terms/#previous></small>"

    ISCC of the preceding version of this item.

### **filename**

!!! term "<small><http://purl.org/iscc/terms/#filename></small>"

    Filename of the referenced **digital content** (automatically used as fallback if the `name` field was not specified for ISCC processing)

### **fps**

!!! term "<small><http://purl.org/iscc/terms/#fps></small>"

    Frames per second of video assets.

### **width**

!!! term "<small><http://purl.org/iscc/terms/#width></small>"

    Width of visual media in number of pixels.

### **height**

!!! term "<small><http://purl.org/iscc/terms/#height></small>"

    Height of visual media in number of pixels.

### **characters**

!!! term "<small><http://purl.org/iscc/terms/#characters></small>"

    Number of text characters (code points after Unicode normalization)

### **parts**

!!! term "<small><http://purl.org/iscc/terms/#parts></small>"

    Indicates items that are part of this item via Content-Codes (inverse-property belongs).

### **part_of**

!!! term "<small><http://purl.org/iscc/terms/#part_of></small>"

    Indicates that this item is part of other items via their Content-Code.

### **features**

!!! term "<small><http://purl.org/iscc/terms/#features></small>"

    Granular features of the *digital content*.

### **generator**

!!! term "<small><http://purl.org/iscc/terms/#generator></small>"

    Name and version of the software that generated the ISCC

### **external_url**

!!! term "<small><http://purl.org/iscc/terms/#external_url></small>"

    This is the URL that will appear below the asset's image on some NFT Marketplaces and will allow users to leave the site and view the item on your site.

### **animation_url**

!!! term "<small><http://purl.org/iscc/terms/#animation_url></small>"

    A URL to a multi-media attachment for the item.

### **properties**

!!! term "<small><http://purl.org/iscc/terms/#properties></small>"

    Arbitrary properties. Values may be strings, numbers, object or arrays. Properties defined here may show up on NFT marketplaces. See [ERC-1155](https://eips.ethereum.org/EIPS/eip-1155#metadata)

### **tophash**

!!! term "<small><http://purl.org/iscc/terms/#tophash></small>"

    A [Multihash](https://multiformats.io/multihash/) of the concatenation (binding) of metahash and datahash (default blake3).

### **metahash**

!!! term "<small><http://purl.org/iscc/terms/#metahash></small>"

    A [Multihash](https://multiformats.io/multihash/) of the supplied metadata (default blake3). The hash is created from `name` and `description` fields or `properties` if supplied. For deterministic results [JSC RFC5452](https://datatracker.ietf.org/doc/html/rfc8785) canonicalization is applied to `properties` before hashing if it is a JSON object.

### **datahash**

!!! term "<small><http://purl.org/iscc/terms/#datahash></small>"

    A [Multihash](https://multiformats.io/multihash/) of the *digital content* (default blake3).

