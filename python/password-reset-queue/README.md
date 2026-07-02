# Password Reset Queue

A Python command-line application for managing a temporary queue of fake password-reset requests.

## Features

- Adds one or more fake reset requests.
- Displays pending requests with user-facing numbers.
- Marks a request complete by its displayed number.
- Removes completed requests from the pending queue.
- Handles invalid menu choices and out-of-range request numbers.
- Returns to the main menu after each action.

## Technical Highlights

- Python lists and dynamic appends
- Zero-based indexes mapped from user-facing numbers
- Nested `while` loops
- Helper functions that parse numeric input
- Empty-list and bounds validation
- `if` / `elif` / `else` control flow

## Run

From the repository root:

```bash
python3 python/password-reset-queue/passwordreset.py
```

## Example Workflow

```text
1. Add request
2. View pending requests
3. Mark as complete
4. Exit
```

A user can add a fictional request, view it as item `1`, then select item `1` to remove it from the pending queue.

## Current Scope

Requests are stored in memory and reset when the application exits. File or database persistence is a possible future improvement.

## Data Safety

All request labels and reasons should remain fictional. The project contains no real accounts, ticket numbers, or workplace information.
