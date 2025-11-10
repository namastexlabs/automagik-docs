# Onboarding Issues Discovered

**Date**: 2025-11-09
**Reviewer**: Claude Code (AI assistant)
**Context**: Creating CLAUDE.md file for the automagik-docs repository

## Issues Found During Onboarding

### 1. No Clear Repository Type Indicator

**Issue**: It's not immediately obvious that this is a documentation-only repository.

**Impact**: New contributors might look for source code or try to run application commands.

**Recommendation**:
- Add a clear callout in `README.md` stating "This is a documentation-only repository"
- Consider adding badges: `[Documentation](badge)` `[Mintlify](badge)`

**Current State**: `README.md` contains only "# Automagik Docs"

---

### 2. Missing Development Dependencies Documentation

**Issue**: No `package.json` or clear dependency listing in the repository.

**Impact**: Contributors don't know what needs to be installed before running `mint dev`.

**Recommendation**:
- Add a "Prerequisites" section to `README.md`:
  ```markdown
  ## Prerequisites

  - Node.js v19+
  - Mintlify CLI: `npm i -g mint`
  ```

**Current State**: Prerequisites only documented in `development.mdx` (buried in docs).

---

### 3. README.md is Nearly Empty

**Issue**: The `README.md` file contains only a single line: "# Automagik Docs"

**Impact**:
- No quick start instructions
- No link to published documentation
- No contribution guidelines
- GitHub visitors get zero context

**Recommendation**: Add essential information:
```markdown
# Automagik Docs

Official documentation for the Automagik Suite.

**📖 View Live Docs**: [https://docs.automagik.ai](URL)

## Quick Start

```bash
npm i -g mint
mint dev
```

## Repository Structure

This is a **documentation-only** repository using Mintlify...
```

---

### 4. Planning Files Scattered in Root

**Issue**: Multiple planning files in root directory:
- `.doc-generation-plan.md`
- `.spark-documentation-plan.md`
- `.spark-execution-plan.md`
- `.spark-final-audit.md`

**Impact**:
- Clutters root directory
- Confusing for new contributors (are these published docs?)
- Not clear these are internal-only

**Recommendation**:
- Move to `.planning/` or `.internal/` directory
- OR add clear comments at the top: `<!-- INTERNAL: Not published -->`
- OR document their purpose in `CLAUDE.md` (already done)

---

### 5. Python Scripts with Hardcoded Paths

**Issue**: `generate-forge-docs.py` contains:
```python
base_path = Path("/home/cezar/automagik/docs/forge")
```

**Impact**: Script won't work for other contributors without modification.

**Recommendation**:
- Use relative paths or environment variables
- Add command-line argument support
- OR clearly mark as "reference only" in comments

---

### 6. No Contribution Guidelines

**Issue**: No `CONTRIBUTING.md` file.

**Impact**: Contributors don't know:
- How to structure commits
- The documentation philosophy ("Linus-approved", grounded reality)
- Quality standards before submitting PRs
- The 4-phase documentation pattern

**Recommendation**: Create `CONTRIBUTING.md` covering:
- Documentation philosophy
- How to add new pages (update docs.json!)
- Quality checklist
- Local testing requirements

---

### 7. Unclear Initial Command

**Issue**: When starting work, the instruction "study this doc" had no doc specified.

**Impact**: Ambiguous starting point for AI assistants or new contributors.

**Recommendation**:
- The `/init` command worked well but isn't discoverable
- Consider adding a `.github/` workflow or template that guides setup

**Note**: This is more of a workflow issue than a documentation issue.

---

### 8. No Link Validation in CI/CD

**Issue**: While `mint broken-links` exists, there's no evidence of it running in CI/CD.

**Impact**: Broken links could be committed and deployed.

**Recommendation**:
- Add GitHub Actions workflow to run `mint broken-links` on PRs
- Block merges if broken links detected

**Current State**: No `.github/workflows/` directory found.

---

### 9. API Base URL Hardcoded to localhost

**Issue**: In `docs.json`:
```json
"api": {
  "baseUrl": "http://localhost:8887"
}
```

**Impact**: API examples in production docs point to localhost.

**Recommendation**:
- Use environment-based configuration
- OR document that this is intentional (development-focused docs)
- OR provide a way to toggle between localhost/production

---

### 10. No Visual Preview of Documentation Structure

**Issue**: To understand the full documentation structure, you must read through the entire `docs.json` file (534 lines).

**Impact**: Hard to get a bird's-eye view of what's documented and what's missing.

**Recommendation**:
- Add a visual sitemap or tree structure to `README.md` or `CONTRIBUTING.md`
- Consider generating it programmatically from `docs.json`

---

## Positive Observations

Things that worked well:

✅ **Clear directory structure** - Each tool has its own directory
✅ **Consistent naming** - `.mdx` extensions, lowercase with hyphens
✅ **docs.json as source of truth** - Centralized configuration
✅ **Planning files show thought process** - Good internal documentation
✅ **Philosophy documented** - "Linus-approved", grounded reality approach
✅ **Automation scripts** - `convert_api_examples.py` shows automation mindset

---

## Priority Recommendations

**High Priority** (Do first):
1. Populate `README.md` with essential information
2. Document prerequisites clearly
3. Add contribution guidelines

**Medium Priority**:
4. Move planning files to dedicated directory
5. Fix hardcoded paths in Python scripts
6. Add link validation to CI/CD

**Low Priority** (Nice to have):
7. Generate visual sitemap
8. Add environment-based API URL configuration
9. Create issue templates for doc contributions

---

## Notes for Future Claude Instances

When working in this repository:
1. **Always update `docs.json`** when adding new pages
2. **Run `mint dev`** to test changes locally
3. **Follow the "grounded reality" philosophy** - no vaporware
4. **Use the 4-phase pattern** for new tool documentation
5. **Check `CLAUDE.md`** for detailed guidance

The biggest gotcha: **Adding a new page without updating `docs.json` will make it invisible in the navigation.**
