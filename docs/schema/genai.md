# GenAI Service Metadata

Machine-readable generative AI disclosure signals for content transparency. Designed for AI providers to declare the level of AI involvement in content creation, supporting compliance with transparency regulations (e.g., EU AI Act Art. 50) and enabling end users to verify AI-generated content. These signals are designed for use within content identification and discovery protocols that provide additional identity, provenance, and trust context.

**JSON Schema**: [`genai.json`](genai.json)

!!! example

    ```json
    {
      "@context": "http://purl.org/iscc/context",
      "@type": "GenAI",
      "$schema": "http://purl.org/iscc/schema/genai.json",
      "involvement": "ai_generated",
      "ai_system": "DALL-E 3",
      "digital_source_type": "http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia"
    }
    ```

## **@context**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| @context | `string-uri` | http://purl.org/iscc/context | The JSON-LD Context URI for ISCC metadata.         |

## **@type**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| @type | `string` | GenAI | The type of service metadata.         |

## **$schema**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| $schema | `string-uri` | http://purl.org/iscc/schema/genai.json | The JSON Schema URI for GenAI service metadata.         |

## **involvement**
<http://purl.org/iscc/terms/#involvement>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| involvement | `string` | none | Level of generative AI involvement in content creation. 'human' indicates content created purely by human effort without generative AI. 'ai_assisted' indicates content created by human effort with support from generative AI. 'human_supervised' indicates content created by generative AI but supervised or reviewed by humans. 'ai_generated' indicates content created by generative AI without human supervision.<br><br>**Example**: `ai_generated`         |

## **ai_system**
<http://purl.org/iscc/terms/#ai_system>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| ai_system | `string` | none | Name or identifier of the generative AI system used for content creation. Aligns with IPTC Photo Metadata 2025.1 'AI System Used' property.<br><br>**Example**: `DALL-E 3`         |

## **digital_source_type**
<http://purl.org/iscc/terms/#digital_source_type>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| digital_source_type | `string-uri` | none | IPTC Digital Source Type URI for granular content source classification. This optional field bridges to the IPTC controlled vocabulary, an external evolving standard that offers finer-grained source type distinctions than the 'involvement' field. Also used by C2PA Content Credentials. See https://cv.iptc.org/newscodes/digitalsourcetype/<br><br>**Example**: `http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia`         |

