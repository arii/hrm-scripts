# Workspace Plan

This document tracks next steps for restructuring and enforcement.

## Active TODOs

- Tighten CI failure conditions: keep CI minimal, fail only on layout validation. [Completed]
- Integrate `npm run verify` into `github-ops/process_pr.py` for local-first checks and PR commenting. [Completed]
- Document local-first workflow in `README.md` (submodule init + run `npm run verify`). [Completed]
- Optional: expand analyzer rules for structural checks (kept local by default). [Completed]

## Notes

- `hrm` lives as a Git submodule under `hrm/`.
- Dev Container initializes submodules and installs app dependencies.
- Layout validation runs via `local-dev/validate_hrm_layout.py` and in minimal CI.
- PR processing defaults to `npm run verify` and includes structure analyzer results in PR comments.
