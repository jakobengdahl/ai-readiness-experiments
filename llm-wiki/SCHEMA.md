# Wiki Schema

## Domain
This wiki covers AI-ready dissemination experiments, MCP patterns, statistical data access workflows, and related operational/design notes that are safe to share publicly.

## Shareability boundary
This wiki is a public/shareable area. It must not contain:
- API keys, tokens, passwords, OAuth credentials, client secrets, or internal URLs with embedded credentials
- raw private documents copied in without review
- personal names tied to sensitive internal project context unless explicitly approved
- operational notes that reveal private infrastructure details not meant for publication

Private staging happens outside the wiki, in ignored local-only directories described in `docs/llm-wiki-workflow.md`.

## Conventions
- File names: lowercase, hyphens, no spaces
- Every wiki page starts with YAML frontmatter
- Use `[[wikilinks]]` for internal references
- Every page should link to at least 2 other wiki pages when possible
- Every change that materially affects the wiki should be logged in `log.md`
- New tags must be added here before use
- Before content is copied into `raw/`, run the sanitization checklist

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [mcp, dissemination]
sources: [raw/articles/example-source.md]
sensitivity: public
---
```

## Tag Taxonomy
- dissemination
- official-statistics
- mcp
- pxweb
- data-access
- ai-agent
- llm-wiki
- evaluation
- workflow
- governance
- security
- sanitization
- comparison
- implementation
- research-note

## Directory roles
- `raw/` — sanitized source material safe to retain in the repo
- `entities/` — notable entities (orgs, tools, platforms, projects)
- `concepts/` — reusable concepts and themes
- `comparisons/` — side-by-side analyses
- `queries/` — durable answers worth preserving
- `_meta/` — policy, release controls, maintenance docs
- `templates/` — page templates
- `tools/` — local helper scripts safe to commit

## Page thresholds
- Create a page when something is central to one ingested source or recurs across multiple sources
- Do not create pages for incidental mentions
- Split pages around 200 lines

## Update policy
When new information conflicts with existing content:
1. keep both claims if needed
2. cite dates/sources
3. note the contradiction explicitly
4. flag it in `log.md` if it needs review
