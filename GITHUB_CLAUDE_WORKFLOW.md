# GitHub and Claude Workflow

This workspace is set up so the main OpenClaw agent can orchestrate both GitHub operations and Claude Code runs for repository work.

## Current setup

- Main orchestration stays in OpenClaw on Codex.
- Claude Code is used as a controlled coding sub-agent when helpful.
- GitHub access currently works through HTTPS with a PAT-backed remote/API flow.
- External-facing repository text, commit messages, branch names, PR titles, and PR bodies should be written in English.
- Conversation with Jakob in this chat can remain in Swedish.

## Claude execution pattern

Claude Code is invoked through:

- `/root/.openclaw/workspace/bin/claude-openclaw`

This wrapper:

- reads the token from `~/.claude/openclaw-oauth-token`
- exports `CLAUDE_CODE_OAUTH_TOKEN`
- runs `claude` with the provided arguments

Use this when Claude should perform bounded repo work and return results, not full internal conversation transcripts.

## GitHub execution pattern

Current GitHub workflow supports:

- creating branches
- committing changes
- pushing branches
- creating pull requests
- updating repo settings through the GitHub API when needed

Because `gh` is not currently installed in this environment, GitHub operations are handled through:

- `git` for local branch/commit/push work
- GitHub REST API for PR creation and repo metadata operations

## Repository conventions for this project

Repository:
- `jakobengdahl/ai-readiness-experiments`

Preferred base branch:
- `main`

Working pattern:
1. start from `main`
2. create a focused branch
3. make a bounded change
4. push the branch
5. open a PR against `main`
6. merge when approved or requested

## Short command patterns Jakob can use

Examples of short requests that should now be enough:

- "Create a branch and draft a PR for this change."
- "Let Claude handle this repo task."
- "Use Claude for the implementation, then open a PR."
- "Make the change directly on a branch and prepare the PR text."
- "Merge the current PR if checks are fine."
- "Update the README and push it on a new branch."

## Important notes

- Keep external/project-facing text in English by default.
- Prefer concise, scoped Claude tasks instead of sending whole conversations through Claude.
- Return summaries, results, errors, and links here, not raw Claude interaction logs.
- The current PAT was shared in chat and should be rotated after setup is stabilized.
- A future improvement is to install `gh` and move to a cleaner GitHub CLI auth flow.
