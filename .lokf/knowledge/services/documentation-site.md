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
  - id: hugo.toml
    resource: website/hugo.toml
    title: docsExclude
  - id: content.gotmpl
    resource: website/content/_content.gotmpl
    title: the redirects
  - id: prepare.sh
    resource: website/scripts/prepare.sh
    title: the schema's pages
  - id: website-readme.md
    resource: website/README.md
    title: what each page is built from
generated:
  by: process:ktl-librarian
  at: "2026-11-15T03:09:10Z"
status: draft
---

# Documentation site

`website/` holds a Hugo site. `website/site.toml` names the repository `lmodel/nist-sp-800-53`, the address `https://lmodel.github.io/nist-sp-800-53/` and the title `nist-sp-800-53`, and sets no logo, so the site shows the Knowledge Trust Ladder logo.[^site.toml] It shows the pages of `docs/` except `docs/templates-linkml/` and `docs/elements/`, which `website/hugo.toml` leaves out.[^hugo.toml] It redirects the addresses the retired mkdocs site gave its pages:

- each class and enum page of the retired schema under `/elements/` to the schema page of the class that renders the same element now, or to `/schema/` where none does;
- `/elements` to `/schema/`;
- the `/elements/<name>/` and `/schema/<name>/` addresses of every current schema page to that page, which sits under its kind's folder, such as `/schema/classes/Sp80053Catalog/`;
- `/about` to `/docs/about/`.

`website/site.toml` lists the retired pages, `/about` and the `/schema/<name>/` addresses. The site adds the `/elements` addresses of the current pages by itself, since the repository has a schema of its own.[^content.gotmpl]

`website/scripts/prepare.sh` runs LinkML's `gen-doc` on `src/nist_sp_800_53/schema/nist_sp_800_53.yaml` and writes the schema's pages into `website/generated/`, which is never committed.[^prepare.sh]

`website/README.md` says what each page is built from: the README becomes the home page, and the changelog a page per release. It also says that `scripts/build.sh` in `website/` writes `dist/` with the search index and then checks every link between its pages, and that Hugo and Pagefind come from PyPI, at the versions `pyproject.toml` names and the hashes `uv.lock` holds.[^website-readme.md] [Knowledge website](../workflows/knowledge-website.md) builds the site on each change to its sources and publishes it once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.

[^site.toml]: website/site.toml, the site's address, title and redirects
[^hugo.toml]: website/hugo.toml, docsExclude
[^content.gotmpl]: website/content/_content.gotmpl, the redirects
[^prepare.sh]: website/scripts/prepare.sh, the schema's pages
[^website-readme.md]: website/README.md, what each page is built from
