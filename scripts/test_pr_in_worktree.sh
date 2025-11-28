#!/bin/bash

set -e

# Check if a PR number is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <pr_number>"
    exit 1
fi

PR_NUMBER=$1
WORKSPACE_ROOT=$(dirname $(dirname $(realpath $0)))
HRM_DIR=$WORKSPACE_ROOT/hrm
WORKTREES_BASE=$WORKSPACE_ROOT/worktrees

# Get the branch name from the PR number
echo "Fetching details for PR #$PR_NUMBER..."
BRANCH_NAME=$(gh pr view $PR_NUMBER --json headRefName --jq '.headRefName' --repo arii/hrm)

if [ -z "$BRANCH_NAME" ]; then
    echo "Could not get branch name for PR #$PR_NUMBER"
    exit 1
fi

echo "Branch name is $BRANCH_NAME"

WORKTREE_PATH=$WORKTREES_BASE/$BRANCH_NAME

# Prune worktrees before creating a new one
echo "Pruning worktrees..."
git -C $HRM_DIR worktree prune

# Create a new worktree
echo "Creating worktree for branch $BRANCH_NAME at $WORKTREE_PATH..."
if [ -d "$WORKTREE_PATH" ]; then
    echo "Worktree path $WORKTREE_PATH already exists. Removing it."
    rm -rf "$WORKTREE_PATH"
fi

git -C $HRM_DIR worktree add --force $WORKTREE_PATH $BRANCH_NAME

# Navigate into the worktree
cd $WORKTREE_PATH

echo "Rebasing onto origin/leader..."
git rebase origin/leader

echo "Installing dependencies..."
npm install

echo "Building the project..."
npm run build

echo "Running visual tests..."
TEST_OUTPUT_FILE=$(mktemp)
if npm run test:visual > $TEST_OUTPUT_FILE 2>&1; then
    TEST_STATUS="✅ Passed"
else
    TEST_STATUS="❌ Failed"
fi

# Create a comment body
COMMENT_BODY="### Local Test Results
**Status:** $TEST_STATUS

<details>
<summary>Test Output</summary>

\`\`\`
$(cat $TEST_OUTPUT_FILE)
\`\`\`

</details>
"

# Post the comment to the PR
echo "Posting comment to PR #$PR_NUMBER..."
gh pr comment $PR_NUMBER -b "$COMMENT_BODY" --repo arii/hrm

# Clean up the temp file
rm $TEST_OUTPUT_FILE


echo "Cleaning up worktree..."
cd $WORKSPACE_ROOT
rm -rf $WORKTREE_PATH
git -C $HRM_DIR worktree prune

echo "Done."
