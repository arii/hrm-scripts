# TODO

This markdown tracks actionable next steps for the workspace.

## Next Actions

- **Performance Optimization**: Add caching for frequent GitHub/Jules API calls to reduce latency
- **Monitoring Dashboard**: Create web interface for workspace status and session health
- **Automated Session Health Checks**: Implement periodic cleanup of stalled or orphaned sessions

## Recently Completed ✅

### Unified Script Architecture (2025-12-01)
- ✅ **Common Configuration**: Created `common_config.py` for centralized path management and logging
- ✅ **Unified Jules Client**: Implemented `jules_client.py` with robust error handling and timeouts
- ✅ **Data Management**: Consolidated all exports into `data/` directory
- ✅ **Script Updates**: Updated all scripts (`jules_ops.py`, session management, github-ops, session-ops) to use unified architecture
- ✅ **Documentation**: Created comprehensive `scripts_README.md`
- ✅ **Code Cleanup**: Removed stale CSV files and duplicate client implementations

### Previous Milestones
- ✅ Expand analyzer rules (route naming conventions, component structure, required env files)
- ✅ Improve README onboarding with "Getting Started" and environment setup tips
- ✅ Minimal CI layout enforcement only
- ✅ `process_pr.py` defaults to local `npm run verify` and includes analyzer results
- ✅ Submodule-based layout, devcontainer init, and local validation script in place
- ✅ Added analyzer summary to PR comment header (PASS/FAIL)
- ✅ Created `scripts/check-workspace.sh` for quick local validation + analyzer
- ✅ Improved PR comment formatting and truncation
- ✅ Added `scripts/verify-pr.sh` wrapper to process PR and open in browser
