# Python Knowledge Check 4: Fake Password Reset Queue

Build this from scratch. Use fake practice data only. Do not use real workplace accounts, usernames, ticket numbers, customer names, internal systems, screenshots, or restricted details.

## Scenario

Create a small CLI app for managing fake password reset requests.

## Required Features

- Show a main menu.
- Add a fake reset request.
- View all pending requests.
- Mark a request complete by number.
- Exit the app.

## Rules

- Store requests in a list.
- Each request should include a fake name or label and a short fake reason.
- Do not crash on invalid menu input.
- Do not crash if the user tries to complete a request number that does not exist.
- After each action, return to the main menu.

## Concepts To Practice

- `input()`
- strings
- lists
- indexes
- helper functions
- `while` loops
- `if` / `elif` / `else`
- numeric input validation
- Git status, diff, staging, and commits

## Manual Tests

Test these flows:

```text
view when list is empty
add one request
view list
complete request 1
view list again
invalid menu input
invalid complete number
exit
```

Expected behavior:

- Empty list prints a clear message.
- Added requests appear in the pending list.
- Completing a request removes it or marks it complete.
- Invalid inputs print a helpful message and keep the app running.
- Exit ends cleanly.

## Git Checkpoints

From the workspace root:

```bash
git status
git diff
git add lifeloom-python-setup/python-hour/knowledge-checks/04-password-reset-queue/README.md
git diff --staged
git commit -m "Add Python password reset queue instructions"
```

After you create the app file:

```bash
git status
git diff
git add lifeloom-python-setup/python-hour/knowledge-checks/04-password-reset-queue
git diff --staged
git commit -m "Add Python password reset queue practice"
git log --oneline -3
```

Before committing, explain what changed and why it is safe to save.
