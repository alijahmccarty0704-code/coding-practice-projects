# Python Knowledge Check 3: Fake Ticket Triage CLI

This is a workplace-safe practice project using fake support requests only. Do not use real workplace tickets, customer names, internal system names, screenshots, or restricted details.

Create a command-line app from scratch named `ticket_triage.py`.

## Scenario

You are building a tiny helper that categorizes fake help-desk ticket text.

The user can:

- Categorize a fake ticket
- View a category guide
- Exit the app

Categories:

- `password`
- `network`
- `hardware`
- `software`
- `general`

## Concepts Being Tested

- `input()`
- strings and `.lower()`
- `if` / `elif` / `else`
- helper functions
- return values
- `while` loops
- `continue`
- simple keyword matching
- Git status, diff, staging, and commit workflow

## Build Checklist

### Checkpoint 1: Create The File, Start, And Exit

- [ ] Create `ticket_triage.py`.
- [ ] Add a short welcome message.
- [ ] Add a `main()` function.
- [ ] Add the `if __name__ == "__main__": main()` guard.
- [ ] Build a main menu loop.
- [ ] Confirm the menu appears.
- [ ] Choose exit.
- [ ] Confirm the app prints a goodbye message.

Run:

```bash
cd lifeloom-python-setup/python-hour/knowledge-checks/03-ticket-triage
python3 ticket_triage.py
```

### Checkpoint 2: Category Guide

- [ ] Select the guide option.
- [ ] Print each category with example fake keywords.
- [ ] Return to the main menu after the guide prints.

Example guide content:

```text
password: password, login, reset, locked
network: wifi, internet, vpn, connection
hardware: laptop, keyboard, monitor, printer
software: app, install, update, error
general: anything unclear
```

### Checkpoint 3: Triage Helper

Create:

```python
categorize_ticket(ticket_text)
```

Rules:

- Password words map to `password`.
- Network words map to `network`.
- Hardware words map to `hardware`.
- Software words map to `software`.
- Anything else maps to `general`.

Stop and explain:

- Why should the helper return a category instead of printing the final answer itself?
- Why should the ticket text be converted to lowercase before checking keywords?

### Checkpoint 4: Categorize Fake Ticket

- [ ] Ask for fake ticket text.
- [ ] Use `categorize_ticket()`.
- [ ] Print the category.
- [ ] Return to the menu.

Manual tests:

```text
forgot password
```

Expected category:

```text
password
```

```text
wifi down
```

Expected category:

```text
network
```

```text
blue screen on laptop
```

Expected category:

```text
hardware
```

```text
calendar app error
```

Expected category:

```text
software
```

```text
need assistance
```

Expected category:

```text
general
```

### Checkpoint 5: Invalid Menu Input

- [ ] If the user types anything besides `1`, `2`, or `3`, print an invalid option message.
- [ ] The app should keep running.

Manual test:

```text
pizza
3
```

Expected:

- invalid option message
- goodbye message

## Git Checkpoints

Use Git from the workspace root:

```bash
git status
git diff
git add lifeloom-python-setup/python-hour/knowledge-checks/03-ticket-triage/README.md
git diff --staged
git commit -m "Add Python ticket triage instructions"

# After you create ticket_triage.py:
git status
git diff
git add lifeloom-python-setup/python-hour/knowledge-checks/03-ticket-triage/ticket_triage.py
git diff --staged
git commit -m "Add Python ticket triage practice"
git log --oneline -3
```

Before committing, explain:

- What files are staged?
- What behavior did you practice?
- Why is this safe for a portfolio or work-practice folder?
