# LLM Wiki Workflow and Boundary Design

## Purpose

This repository will hold the shareable/public LLM Wiki output for AI-ready dissemination work. It is not the full private working memory of the agent.

## Recommended boundary

### Agent/private working area
Keep these outside the public wiki and preferably outside the repository or in ignored paths:
- Telegram document cache
- Google Drive raw pulls before review
- private scratch notes
- credentials, OAuth tokens, `.env`, client secrets
- name-specific internal project notes
- staging material that has not been sanitized yet

Recommended local-only directories:
- `workspace-private/ingest-staging/`
- `workspace-private/notes/`
- `workspace-private/tmp/`
- `llm-wiki-private/`

These are ignored by `.gitignore`.

### Shareable repo area
This is what can be mirrored to GitHub:
- `llm-wiki/`
- public docs explaining workflow and controls
- helper scripts that do not contain secrets

## Planned ingestion process later
1. receive source via Telegram or pull from Google Drive
2. store it in private staging first
3. inspect for names/secrets/private context
4. create a sanitized source artifact if needed
5. copy only the sanitized version into `llm-wiki/raw/`
6. synthesize wiki pages in `entities/`, `concepts/`, `comparisons/`, or `queries/`
7. run the sanitization check before commit/push

## Obsidian: how necessary is it?

Obsidian is not required.

### What works without Obsidian
- the wiki is just markdown files in folders
- Hermes can read, update, lint, and maintain the wiki directly
- GitHub versioning works fine without Obsidian
- headless/server use does not require a GUI at all

### What Obsidian improves
- faster human browsing of linked notes
- graph view for the knowledge network
- easy backlink navigation via `[[wikilinks]]`
- optional plugins such as Dataview for lightweight views over frontmatter

### Practical recommendation
- for agent-first automation: Obsidian is optional
- for human review/curation: Obsidian is very useful but not essential

## Hosting on another Proxmox LXC (or similar)

A workable agent-friendly setup:

1. create an LXC with:
   - git
   - python3
   - Hermes
   - optional Node.js if you want `obsidian-headless`
2. clone `jakobengdahl/ai-readiness-experiments`
3. keep the shareable wiki under the repo, e.g. `/srv/ai-readiness-experiments/llm-wiki`
4. keep private staging outside the repo, e.g. `/srv/ai-ready-private/`
5. let Hermes run on the same machine and use:
   - repo path for public wiki output
   - private path for staging and unsanitized material
6. optionally sync the repo via git push/pull
7. optionally run periodic lint/sanitization checks via cron

### With Obsidian on a headless/server box
If you want an Obsidian-compatible remote workflow:
- Hermes writes markdown into the repo's `llm-wiki/`
- optionally use `obsidian-headless` plus Obsidian Sync on a server
- your desktop Obsidian vault points at the same synced folder or a local clone

That said, for this project I would start simpler:
- use git + markdown first
- add Obsidian later only if you want better human navigation

## Resulting structure

### Agent total working structure (conceptual)
```text
/root/
  ai-readiness-experiments/          # git-tracked repo
    llm-wiki/                        # shareable/public wiki area
    docs/                            # public workflow docs
    bin/                             # repo helper scripts
  workspace-private/                 # ignored local staging
    ingest-staging/                  # raw Telegram/Drive drops before review
    notes/                           # private scratch notes
    tmp/                             # temporary processing artifacts
  .hermes/                           # Hermes config, tokens, sessions, skills
```

### Shareable wiki structure inside the repo
```text
llm-wiki/
  README.md
  SCHEMA.md
  index.md
  log.md
  raw/
    articles/
    papers/
    transcripts/
    assets/
  entities/
  concepts/
  comparisons/
  queries/
  _meta/
    README.md
    SANITIZATION_POLICY.md
    RELEASE_CHECKLIST.md
    redaction-denylist.example.txt
  templates/
    page-template.md
  tools/
    sanitize_check.py
```

## Operating rule
The agent can use both the private area and the repo, but only the `llm-wiki/` area is intended to be broadly shareable. Treat everything else as private unless explicitly promoted.
