---
icon: lucide/microscope
title: STM Seed
description: Scientific/Technical/Medical seed metadata for DOI-identified scholarly works.
---

# STM Seed Metadata

STM (Scientific/Technical/Medical) Seed Metadata for interoperable Meta-Code generation. Minimal distinguishing metadata for scholarly works identified by a DOI, populatable from any DOI via Crossref/DataCite content negotiation (CSL-JSON). See [IEP-0002](https://github.com/iscc/iscc-ieps/blob/main/ieps/iep-0002.md) for details on Meta-Code generation.

**JSON Schema**: [`stm.json`](stm.json)

!!! example

    ```json
    {
      "$schema": "http://purl.org/iscc/schema/stm-0.7.0.json",
      "doi": "10.1016/j.jnt.2020.04.008",
      "resource_type": "JournalArticle",
      "title": "Twisting moduli for GL(2)",
      "publisher": "Elsevier Inc.",
      "pubyear": 2020,
      "version_type": "VoR",
      "container_title": "Journal of Number Theory",
      "issn": "0022-314X"
    }
    ```

**Required fields**: `$schema`, `doi`, `resource_type`, `title`, `publisher`, `pubyear`

## Field Reference

## **@context**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| @context | `string-uri` | http://purl.org/iscc/context | The JSON-LD Context URI for ISCC metadata.         |

## **@type**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| @type | `string` | STM | The type of seed metadata.         |

## **$schema**

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| $schema | `string-uri` | http://purl.org/iscc/schema/stm-0.7.0.json | The JSON Schema URI for STM seed metadata.         |

## **doi**
<http://purl.org/ontology/bibo/doi>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| doi | `string` | none | Digital Object Identifier of the work, lowercased, in bare prefix form (without the https://doi.org/ resolver prefix).<br><br>**Example**: `10.1016/j.jnt.2020.04.008`         |

## **resource_type**
<http://schema.org/additionalType>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| resource_type | `string` | none | The kind of research output as a readable token. Tokens follow the DataCite resource-type vocabulary and are populated from the Crossref/DataCite work type (for example, journal-article maps to JournalArticle). Each token is mapped to a resolvable schema.org or FaBiO class IRI in the JSON-LD context (see x-iscc-enum-context). This is the work-kind axis; version_type is the orthogonal version-stage axis.<br><br>**Example**: `JournalArticle`         |

## **title**
<http://schema.org/name>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| title | `string` | none | The primary title of the work.<br><br>**Example**: `Twisting moduli for GL(2)`         |

## **publisher**
<http://schema.org/publisher>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| publisher | `string` | none | Name of the publishing entity.<br><br>**Example**: `Elsevier Inc.`         |

## **pubyear**
<http://schema.org/datePublished>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| pubyear | `integer` | none | Year of publication. Crossref guarantees year-level precision only; using an integer avoids the false precision of a full date.<br><br>**Example**: `2020`         |

## **version_type**
<http://purl.org/iscc/terms/#version_type>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| version_type | `string` | none | Manifestation version using the NISO JAV (RP-8-2008) vocabulary. Publisher-specific version taxonomies are mapped into these values. Lets a Version-of-Record and an Accepted-Manuscript of the same work produce different Meta-Codes while a shared work-level `doi` links them.<br><br>**Example**: `VoR`         |

## **container_title**
<http://prismstandard.org/namespaces/basic/2.0/publicationName>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| container_title | `string` | none | Title of the serial or collection the work is part of (journal, proceedings, book). Not guaranteed for standalone works.<br><br>**Example**: `Journal of Number Theory`         |

## **issn**
<http://schema.org/issn>

| Name | Type | Default | Definition                     |
| ---- | ---- | --------|--------------------------------|
| issn | `string` | none | ISSN of the container serial. Only present for serial publications.<br><br>**Example**: `0022-314X`         |

