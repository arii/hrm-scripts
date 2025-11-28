# TODO

This markdown tracks actionable next steps for the workspace.

## Next Actions

- Integrate analyzer summary into PR comments header (short pass/fail + link to details).
- Add quick workspace check script `scripts/check-workspace.sh` to run layout validation + analyzer locally.
- Harden `github-ops/process_pr.py` error parsing for `npm run verify` and improve PR comment truncation/formatting.
- Expand analyzer rules (route naming conventions, component structure, required env files).
- Improve README onboarding with “Getting Started” and environment setup tips.
- Optional convenience: `scripts/verify-pr.sh <pr>` wrapper to fetch PR, run local verify, and surface logs.

## Completed

- Minimal CI layout enforcement only.
- `process_pr.py` defaults to local `npm run verify` and includes analyzer results.
- Submodule-based layout, devcontainer init, and local validation script in place.
