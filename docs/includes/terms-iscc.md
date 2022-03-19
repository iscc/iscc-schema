### **meta**

!!! term "<small><http://purl.org/iscc/terms/#meta></small>"

    Subject, industry, or use-case specific metadata, encoded as JSON string or Data-URL (used as sole input for Meta-Code and `metahash` generation if supplied).

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

### **attributes**

!!! term "<small><http://purl.org/iscc/terms/#attributes></small>"

    Similar to `properties` but as an array of objects. These attributes will show up on some NFT marketplaces.

### **tophash**

!!! term "<small><http://purl.org/iscc/terms/#tophash></small>"

    A [Multihash](https://multiformats.io/multihash/) of the concatenation (binding) of metahash and datahash (default blake3).

### **metahash**

!!! term "<small><http://purl.org/iscc/terms/#metahash></small>"

    A [Multiformats](https://multiformats.io) multihash or IPFS CIDv1 of the supplied metadata. The hash is created from `name` and `description` fields or `meta` if supplied.

### **datahash**

!!! term "<small><http://purl.org/iscc/terms/#datahash></small>"

    A [Multihash](https://multiformats.io/multihash/) of the *digital content* (default blake3).

### **original**

!!! term "<small><http://purl.org/iscc/terms/#original></small>"

    The signee of the declaring transaction claims to be the original creator of the work manifested by the identified digital content.

### **redirect**

!!! term "<small><http://purl.org/iscc/terms/#redirect></small>"

    URL to which a resolver should redirect an ISCC-ID that has been minted from a declartion that includes the IPFS-hash of this metadata instance.

### **chain**

!!! term "<small><http://purl.org/iscc/terms/#chain></small>"

    The blockchain on which an ISCC-CODE is declared.

### **wallet**

!!! term "<small><http://purl.org/iscc/terms/#wallet></small>"

    The wallet-address that signs an ISCC declaration.

### **verifications**

!!! term "<small><http://purl.org/iscc/terms/#verifications></small>"

    A list of self-verifications. Self-verifications are public URLs under the account/authority of the signee. The verification URL must respond to a GET request with text that contains a multihash of the ISCC declaration signees wallet address in the format of `verify:<multihash-of-wallet-address>:verify`.

