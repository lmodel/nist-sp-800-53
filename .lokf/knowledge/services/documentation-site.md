---
type: Service
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: "The Hugo site in `website/`, for <https://lmodel.github.io/nist-sp-800-53>: the README as its home page, the pages of `docs/`, the schema's element pages, a page per concept of this bundle with its trust label, and the bundle's exports, built and published by Knowledge website."
resource: website
endpoint: https://lmodel.github.io/nist-sp-800-53
documentation: website/README.md
sources:
  - id: site.toml
    resource: website/site.toml
    title: the site's address, title and redirects
  - id: website-readme.md
    resource: website/README.md
    title: what each page is built from
generated:
  by: process:ktl-librarian
  at: "2026-11-15T02:57:28Z"
status: draft
---

# Documentation site

`website/` holds a Hugo site. `website/site.toml` names the repository `lmodel/nist-sp-800-53`, the site `https://lmodel.github.io` with the base path `/nist-sp-800-53`, and the title `nist-sp-800-53`.[^site.toml] It shows the pages of `docs/` except `docs/templates-linkml/`. It redirects the addresses the retired mkdocs site gave its pages:

- each class and enum page of the retired schema under `/elements/` to the schema page of the class that renders the same element now, or to `/schema/` where none does;
- `/elements` to `/schema/`;
- the old address of every current schema page to that page;
- `/about` to `/docs/about/`.

The other options take the site's defaults: the Knowledge Trust Ladder logo, the README as the home page, the changelog once it holds a release, and the schema's pages that `just gen-doc` writes.

`website/README.md` says what each page is built from, and that `npm run build` syncs the bundle, the README, the docs and the schema's pages before it builds and checks every link.[^website-readme.md] [Knowledge website](../workflows/knowledge-website.md) builds the site on each change to its sources and publishes it once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.

[^site.toml]: website/site.toml, the site's address, title and redirects
[^website-readme.md]: website/README.md, the build and its sources
