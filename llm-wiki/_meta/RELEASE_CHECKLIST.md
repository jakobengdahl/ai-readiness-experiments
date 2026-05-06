# Release Checklist

Before pushing wiki changes or sharing this directory:

- [ ] No secrets or credentials present
- [ ] No personal names that should remain private
- [ ] No raw private source documents copied over by mistake
- [ ] Sanitized files in `raw/` are actually safe to publish
- [ ] `python3 llm-wiki/tools/sanitize_check.py llm-wiki` runs clean
- [ ] `index.md` and `log.md` reflect the current state
- [ ] Any new tags used are declared in `SCHEMA.md`
- [ ] Repo diff only contains intended public/shareable files
