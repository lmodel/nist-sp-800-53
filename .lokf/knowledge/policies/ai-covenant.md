---
type: Policy
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/policies/ai-covenant
genre: reference
title: AI covenant
description: "The repository's rules for work done with artificial intelligence (AI): you own what you submit, an element under the schema renders SP 800-53, SP 800-53A or SP 800-53B in the project's own words and cites it, NIST's catalog and baseline copies are never edited, and the scheduled librarian proposes changes only through reviewed pull requests."
resource: AI_COVENANT.md
sources:
  - id: ai_covenant.md
    resource: AI_COVENANT.md
    title: the core principle, the project note and the agent automation section
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:28:23Z"
status: draft
---

# AI covenant

`AI_COVENANT.md` says that everything you contribute is yours, whatever tools helped create it: you understand, verify and defend what you submit. Its note for this project says the repository models someone else's catalog, so an element under `src/nist_sp_800_53/schema/` says what SP 800-53, SP 800-53A or SP 800-53B says, in the project's own words, with the section or table cited in the pull request; the copies under `src/nist_sp_800_53/schema/oscal-content/` are NIST's text, never edited and replaced only from one release of usnistgov/oscal-content; and the namespace `nist_sp_800_53:` is the project's own, with the catalog's identifiers appearing only as values.[^ai_covenant.md]

For the scheduled librarian, the covenant says the agent commits under a bot identity or the maintainer who invoked it, never both, opens every change as a pull request a person approves, runs with no write credential and hands its change to a separate job that runs no agent, and records a person's verdict only as that person gave it. AI review comments are suggestions, AI systems must not post in issues or discussions, and co-authorship trailers are discouraged.[^ai_covenant.md]

[^ai_covenant.md]: AI_COVENANT.md, Core Principle, A note specific to this project and Repository-Owned Agent Automation
