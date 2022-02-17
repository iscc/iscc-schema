# Examples of ISCC Metadata

A collection of samples how you can use ISCC Metadata for different use cases.

## ISCC-NFT Metadata

ISCC metadata supports and extends the NFT metadata standards as defined by [ERC-721](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-721.md#specification) and [ERC-1155](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1155.md#metadata). The basic NFT metadata fields `name`, `description` and `image` are the same in ISCC metadata. ISCC metadata also specifically supports the `properties`-field and the commonly used fields `animation_url`, `external_url`  (See: https://schema.iscc.codes/schema/#iscc-nft).

### ISCC-NFT Examples

Basic NFT metadata extended with an ISCC:

```json
{
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



















