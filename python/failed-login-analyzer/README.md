# Failed Login Analyzer

## Goal

Build a small Python CLI that analyzes fake failed-login events and flags basic risk patterns.

Use fake data only. Do not use real workplace usernames, IP addresses, logs, device names, customer names, or internal systems.

## Scenario

A help desk analyst wants a simple tool for reviewing fake failed-login attempts. The tool should let the user add fake failed-login records, view all records, count failures for a username, and flag usernames with repeated failures.

## Concepts Practiced

- `while` menu loop
- `if` / `elif` / `else`
- lists
- strings
- helper functions
- user input
- numeric validation
- counting items
- Git status/diff/add/commit/log loop

## Build Checklist

- [x] Create a menu with these options:
  - `1. Add failed login`
  - `2. View failed logins`
  - `3. Count failures for username`
  - `4. Show high-risk usernames`
  - `5. Exit`
- [x] Store fake failed-login records in a list.
- [x] Each record should include:
  - fake username
  - fake IP address
  - fake reason
- [x] Add input validation for menu choices.
- [x] Print a clear message when the list is empty.
- [x] Count how many records match a username entered by the user.
- [x] Mark a username as high-risk if it has 3 or more failed logins.
- [x] Exit cleanly.

## Suggested Fake Test Data

Use examples like these:

- username: `alex.demo`
  - IP: `10.0.0.15`
  - reason: `bad password`
- username: `sam.test`
  - IP: `10.0.0.22`
  - reason: `locked account`
- username: `alex.demo`
  - IP: `10.0.0.18`
  - reason: `bad password`
- username: `alex.demo`
  - IP: `10.0.0.19`
  - reason: `bad password`

## Manual Tests

- Invalid menu input reprompts or shows an error.
- Viewing records before adding any records shows an empty-list message.
- Adding one failed login makes it appear in the list.
- Counting `alex.demo` after adding three matching records prints `3`.
- High-risk usernames shows `alex.demo` when it has 3 or more failed logins.
- Exit option ends the program cleanly.

## Git Checkpoints

Use Git yourself as you work:

1. `git status`
2. `git diff`
3. `git add lifeloom-python-setup/python-hour/knowledge-checks/05-failed-login-analyzer/README.md lifeloom-python-setup/python-hour/knowledge-checks/05-failed-login-analyzer/failed_login_analyzer.py`
4. `git diff --staged`
5. Commit only when the program works and you understand the staged changes.

Suggested commit message:

```bash
git commit -m "Add failed login analyzer practice"
```

## Stretch Goals

- Show unique usernames.
- Show total failed-login count.
- Allow deleting one fake record by number.
- Save fake records to a text file.
