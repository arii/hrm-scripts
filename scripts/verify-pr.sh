#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <pr_number>"
  exit 1
fi

PR_NUMBER="$1"

echo "[INFO] Processing PR #${PR_NUMBER}..."
python github-ops/process_pr.py "${PR_NUMBER}"

echo ""
echo "[INFO] Opening PR in browser..."
gh pr view "${PR_NUMBER}" --web --repo arii/hrm
