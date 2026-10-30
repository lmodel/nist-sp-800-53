---
type: Service
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/workflows/knowledge-website
genre: reference
title: Knowledge website (knowledge-website.yaml)
description: "The Knowledge website workflow, `.github/workflows/knowledge-website.yaml`: on pushes and pull requests that touch the site's sources, every Monday at 05:23 UTC and by hand, its build job builds `website/` and checks its links read-only, and its deploy job publishes the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is true."
resource: .github/workflows/knowledge-website.yaml
sources:
  - id: knowledge-website.yaml
    resource: .github/workflows/knowledge-website.yaml
    title: the header comment, the on key and the two jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:28:23Z"
status: draft
---

# Knowledge website (knowledge-website.yaml)

`.github/workflows/knowledge-website.yaml` is a copy of the ktl-website template at Knowledge Trust Ladder v0.59.0. It runs on pushes and pull requests that touch the site's sources, every Monday at 05:23 UTC and by hand. Its `build` job runs with `contents: read` and no secret. It:

- checks the repository out with its full history;
- installs the sidecar's toolkit with `uv sync --locked` in `.lokf/`, and the site's packages with `npm ci --ignore-scripts`;
- runs `npm run build`, which syncs the bundle, the README, the docs and the schema's pages, then builds and checks every link;
- uploads `website/dist` as the Pages artifact.

Its `deploy` job holds `pages: write` and `id-token: write`, runs only from the default branch in the `github-pages` Environment, and only once the repository variable `KNOWLEDGE_WEBSITE_ENABLED` is `true`. [Documentation site](../services/documentation-site.md) describes what it publishes.[^knowledge-website.yaml]

[^knowledge-website.yaml]: .github/workflows/knowledge-website.yaml, the header comment, the on key and the two jobs
