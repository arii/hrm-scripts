#!/usr/bin/env bash
set -euo pipefail

# If PR numbers provided as arguments, use those
# Otherwise, fetch all open PRs
if [ "$#" -gt 0 ]; then
  PR_NUMBERS=("$@")
else
  echo "[INFO] No PR numbers provided, fetching open PRs..."
  mapfile -t PR_NUMBERS < <(gh pr list --repo arii/hrm --state open --json number --jq '.[].number')
  
  if [ "${#PR_NUMBERS[@]}" -eq 0 ]; then
    echo "[INFO] No open PRs found."
    exit 0
  fi
  
  echo "[INFO] Found ${#PR_NUMBERS[@]} open PR(s): ${PR_NUMBERS[*]}"
fi

# Process each PR
for PR_NUMBER in "${PR_NUMBERS[@]}"; do
  echo ""
  echo "=========================================="
  echo "[INFO] Processing PR #${PR_NUMBER}..."
  echo "=========================================="
  python github-ops/process_pr.py "${PR_NUMBER}"
  echo "[DONE] PR #${PR_NUMBER} processing complete."
done

echo ""
echo "[DONE] All PRs processed."
