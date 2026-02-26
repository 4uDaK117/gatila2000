@echo off
REM Initialize git repository and create initial commit
if not exist .git (
    git init
    git add .
    git commit -m "Initial commit"
    echo Repository initialized and initial commit created.
) else (
    echo Git repository already initialized.
)
