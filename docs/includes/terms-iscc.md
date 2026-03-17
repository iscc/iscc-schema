### **iscc**

!!! term "<small><http://purl.org/iscc/terms/#iscc></small>"

    An **ISCC-CODE** in canonical representation. A valid ISCC Metadata object should include at least one of the `iscc`, `iscc_id`, or `iscc_code` fields.

    **Standard**:  ISO 24138:2024

### **meta**

!!! term "<small><http://purl.org/iscc/terms/#meta></small>"

    Subject, industry, or use-case specific metadata encoded as Data-URL.

    **Standard**:  ISO 24138:2024

### **media_id**

!!! term "<small><http://purl.org/iscc/terms/#media_id></small>"

    Vendor specific (internal) identifier for the source media file.

### **iscc_id**

!!! term "<small><http://purl.org/iscc/terms/#iscc_id></small>"

    The **ISCC-ID** of the digital content in canonical representation. A valid ISCC Metadata object should include at least one of the `iscc`, `iscc_id`, or `iscc_code` fields.

### **iscc_code**

!!! term "<small><http://purl.org/iscc/terms/#iscc></small>"

    A composite **ISCC-CODE** in canonical representation. Explicit alternative to the more compact `iscc` field. A valid ISCC Metadata object should include at least one of the `iscc`, `iscc_id`, or `iscc_code` fields.

### **previous**

!!! term "<small><http://purl.org/iscc/terms/#previous></small>"

    ISCC of the preceding version of this item.

### **tdm**

!!! term "<small><http://purl.org/iscc/terms/#tdm></small>"

    Machine-readable TDM reservation signals for AI-related content usage categories. Omitted fields indicate that the reservation status has not been determined.

### **genai**

!!! term "<small><http://purl.org/iscc/terms/#genai></small>"

    Machine-readable generative AI disclosure signals for content transparency. Omitted fields indicate that the disclosure status has not been determined.

### **mode**

!!! term "<small><http://purl.org/iscc/terms/#mode></small>"

    The perceptual mode used to create the ISCC-CODE.

### **filename**

!!! term "<small><http://purl.org/iscc/terms/#filename></small>"

    Filename of the referenced **digital content** (automatically used as fallback if the `name` field was not specified for ISCC processing)

    **Standard**:  ISO 24138:2024

### **fps**

!!! term "<small><http://purl.org/iscc/terms/#fps></small>"

    Frames per second of video assets.

    **Standard**:  ISO 24138:2024

### **width**

!!! term "<small><http://purl.org/iscc/terms/#width></small>"

    Width of visual media in number of pixels.

    **Standard**:  ISO 24138:2024

### **height**

!!! term "<small><http://purl.org/iscc/terms/#height></small>"

    Height of visual media in number of pixels.

    **Standard**:  ISO 24138:2024

### **characters**

!!! term "<small><http://purl.org/iscc/terms/#characters></small>"

    Number of text characters (code points after Unicode normalization)

    **Standard**:  ISO 24138:2024

### **parts**

!!! term "<small><http://purl.org/iscc/terms/#parts></small>"

    Indicates items that are part of this item via Content-Codes (inverse-property belongs).

### **part_of**

!!! term "<small><http://purl.org/iscc/terms/#part_of></small>"

    Indicates that this item is part of other items via their Content-Code.

### **features**

!!! term "<small><http://purl.org/iscc/terms/#features></small>"

    Granular features of the *digital content*.

### **units**

!!! term "<small><http://purl.org/iscc/terms/#units></small>"

    Individual ISCC-UNITs that make up a composite ISCC-CODE.

### **generator**

!!! term "<small><http://purl.org/iscc/terms/#generator></small>"

    Name and version of the software that generated the ISCC

### **text**

!!! term "<small><http://purl.org/iscc/terms/#text></small>"

    Extracted plaintext of the *digital content*.

### **external_url**

!!! term "<small><http://purl.org/iscc/terms/#external_url></small>"

    This is the URL that will appear below the asset's image on some NFT Marketplaces and will allow users to leave the site and view the item on your site. **Supports URI template `(iscc-id)`**.

### **animation_url**

!!! term "<small><http://purl.org/iscc/terms/#animation_url></small>"

    A URL to a multi-media attachment for the item.

### **properties**

!!! term "<small><http://purl.org/iscc/terms/#properties></small>"

    Arbitrary properties. Values may be strings, numbers, object or arrays. Properties defined here may show up on NFT marketplaces. See [ERC-1155](https://eips.ethereum.org/EIPS/eip-1155#metadata)

### **attributes**

!!! term "<small><http://purl.org/iscc/terms/#attributes></small>"

    Similar to `properties` but as an array of objects. These attributes will show up on some NFT marketplaces.

### **nft**

!!! term "<small><http://purl.org/iscc/terms/#nft></small>"

    A unique URI for a non-fungible token of the identified content. The URI must contain references to the blockchain, smart-contract and token. The recommended schemes are [CAIP-22](https://github.com/ChainAgnostic/CAIPs/blob/master/CAIPs/caip-22.md) and [CAIP-29](https://github.com/ChainAgnostic/CAIPs/blob/master/CAIPs/caip-29.md).

### **tophash**

!!! term "<small><http://purl.org/iscc/terms/#tophash></small>"

    A [Multihash](https://multiformats.io/multihash/) of the concatenation (binding) of metahash and datahash (default blake3).

    **Standard**:  ISO 24138:2024

### **metahash**

!!! term "<small><http://purl.org/iscc/terms/#metahash></small>"

    A [Multiformats](https://multiformats.io) multihash or IPFS CIDv1 of the supplied metadata. The hash is created from `name` and `description` fields or `meta` if supplied.

    **Standard**:  ISO 24138:2024

### **datahash**

!!! term "<small><http://purl.org/iscc/terms/#datahash></small>"

    A [Multihash](https://multiformats.io/multihash/) of the *digital content* (default blake3).

    **Standard**:  ISO 24138:2024

### **nonce**

!!! term "<small><http://purl.org/iscc/terms/#nonce></small>"

    Cryptographic nonce for replay protection. A 128-bit random value encoded as lowercase hexadecimal.

### **signature**

!!! term "<small><http://purl.org/iscc/terms/#signature></small>"

    Cryptographic signature over ISCC metadata, conforming to the [iscc-crypto](https://github.com/iscc/iscc-crypto) signing protocol. Uses EdDSA (Ed25519) with JCS canonicalization.

### **original**

!!! term "<small><http://purl.org/iscc/terms/#original></small>"

    The signee of the declaring transaction claims to be the original creator of the work manifested by the identified digital content.

### **redirect**

!!! term "<small><http://purl.org/iscc/terms/#redirect></small>"

    URL to which an ISCC resolver should redirect the ISCC-ID. **Supports URI template `(iscc-id)`**

### **chain**

!!! term "<small><http://purl.org/iscc/terms/#chain></small>"

    The blockchain on which an ISCC-CODE is declared.

### **wallet**

!!! term "<small><http://purl.org/iscc/terms/#wallet></small>"

    The wallet-address that signs an ISCC declaration.

### **verifications**

!!! term "<small><http://purl.org/iscc/terms/#verifications></small>"

    A list of self-verifications. Self-verifications are public URLs under the account/authority of the signee. The verification URL must respond to a GET request with text that contains a multihash of the ISCC declaration signees wallet address in the format of `verify:<multihash-of-wallet-address>:verify`.

