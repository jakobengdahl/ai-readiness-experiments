# Sanitization Policy

This wiki is intended to be mirrored to GitHub and shared. Treat it as public by default.

## Never commit these here
- secrets, API keys, bearer tokens, cookies, passwords, OAuth refresh/access tokens
- downloaded credential files such as `client_secret*.json`
- `.env` contents
- private internal meeting notes copied verbatim without review
- personal names that are not clearly intended for public dissemination
- direct exports from private chats unless rewritten/sanitized
- internal-only URLs, hostnames, IPs, ports, or infrastructure maps unless explicitly approved

## Required workflow boundary
1. ingest raw material into a private staging area outside the shareable wiki
2. inspect it manually/agentically for sensitivity
3. create a sanitized derivative if needed
4. only then copy the sanitized version into `llm-wiki/raw/`
5. run `tools/sanitize_check.py llm-wiki`
6. only after review should material be committed/pushed

## Redaction guidance
- replace names with roles where possible, e.g. `[project lead]`
- replace exact secrets with placeholders, e.g. `[redacted-secret]`
- rewrite private notes into generalized lessons rather than publishing originals
- if uncertain whether something is sensitive, keep it out
