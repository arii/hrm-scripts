# TODO

This markdown tracks actionable next steps for the workspace.

## Next Actions

- Expand analyzer rules (route naming conventions, component structure, required env files).
- Improve README onboarding with "Getting Started" and environment setup tips.

## Completed

- Minimal CI layout enforcement only.
- `process_pr.py` defaults to local `npm run verify` and includes analyzer results.
- Submodule-based layout, devcontainer init, and local validation script in place.
- Added analyzer summary to PR comment header (PASS/FAIL).
- Created `scripts/check-workspace.sh` for quick local validation + analyzer.
- Improved PR comment formatting and truncation.
- Added `scripts/verify-pr.sh` wrapper to process PR and open in browser.
