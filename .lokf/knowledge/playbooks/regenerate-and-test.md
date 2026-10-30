---
type: Playbook
id: https://w3id.org/lmodel/nist-sp-800-53/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test after a schema change
description: "How to change the schema and check it: `uv sync --group dev`, edit `src/nist_sp_800_53/schema/nist_sp_800_53.yaml`, then `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and the pre-commit hooks before a pull request."
resource: CONTRIBUTING.md
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Development setup and Before opening a pull request
  - id: justfile
    resource: justfile
    title: the lint, gen-project, gen-doc and test recipes
  - id: claude.md
    resource: .claude/CLAUDE.md
    title: the Commands section
generated:
  by: process:ktl-librarian
  at: "2026-10-30T08:34:38Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T09:09:14Z"
---

# Regenerate and test after a schema change

1. Install with `uv sync --group dev`. You need Python 3.10 or later, uv and just.[^contributing.md]
2. Edit `src/nist_sp_800_53/schema/nist_sp_800_53.yaml`, rendering what SP 800-53, SP 800-53A or SP 800-53B defines in your own words, and name the section or table in the pull request.
3. Run `just lint`, which runs linkml-lint with errors only under `.linkmllint.yaml`.[^justfile]
4. Run `just gen-project`, `just gen-doc` and `just lokf-adapt`, and commit their output. `project/`, `src/nist_sp_800_53/datamodel/`, `docs/schema/` and `.lokf/nist-sp-800-53.yaml` are generated.
5. Add a valid example and a counter-example per new constraint under `tests/data/`, named `ClassName-suffix.yaml`, each counter-example starting `# Fails at: <JSON pointer>`, and run `just test`.
6. Run the pre-commit hooks on what you staged with `uvx pre-commit run`, and add a changelog entry under `## [Unreleased]` when the change alters behaviour.

`.claude/CLAUDE.md` lists the same commands for a coding agent, and says to edit only the schema and never a generated file.[^claude.md]

[^contributing.md]: CONTRIBUTING.md, Development setup and Before opening a pull request
[^justfile]: justfile, lint, gen-project, gen-doc and test
[^claude.md]: .claude/CLAUDE.md, Commands and Schema-Driven Generation
