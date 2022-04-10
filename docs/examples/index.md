# Examples of ISCC Metadata

A collection of samples how you can use ISCC Metadata for different use cases.

## ISCC-NFT Metadata

ISCC metadata is a superset of NFT metadata as defined
by [ERC-721](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-721.md#specification)
and [ERC-1155](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1155.md#metadata). The  NFT
metadata fields `name`, `description` and `image`, `properties` are the same in the ISCC metadata
schema.  ISCC metadata also specifically supports the commonly used fields like `attributes`,
`animation_url`, and `external_url`  (See: https://schema.iscc.codes/schema/#iscc-nft).

### ISCC-NFT Examples

Basic NFT metadata extended with an ISCC:

``` json linenums="1"
{
    "@context": "http://purl.org/iscc/context/0.3.6.jsonld",
    "$schema": "http://purl.org/iscc/schema/0.3.6.json",
    "@type": "ImageObject",
    "iscc": "ISCC:KMD5MO6ZVATK7EOBJY2ED5CVIEZ4IW2ATWZ6SX2VQLROZORS5W5TR6A",
    "name": "LIQUID SILVER",
    "description": "Liquid Metal by TRIPLE SIX. Holders will have exclusive access to events, giveaways and more.",
    "image": "ipfs://QmWguwGk5DvfuY9a7eVrkgjYgu66eCLsku2NPtbKhddz2C/1.mp4",
    "attributes": [
        {
            "trait_type": "METAL",
            "value": "SILVER"
        },
        {
            "display_type": "number",
            "trait_type": "GENERATION",
            "value": 1
        }
    ]
}
```



















