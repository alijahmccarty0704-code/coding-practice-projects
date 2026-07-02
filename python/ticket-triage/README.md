# Ticket Triage CLI

A Python command-line application that categorizes fake help-desk requests using simple keyword matching.

## Features

- Displays a guide for supported ticket categories.
- Accepts a short, fake support request from the user.
- Normalizes input to lowercase before matching keywords.
- Categorizes requests as `password`, `network`, `hardware`, `software`, or `general`.
- Handles invalid menu input without exiting unexpectedly.

## Technical Highlights

- Python functions and return values
- `while` loop menu flow
- String normalization with `.lower()`
- `if` / `elif` / `else` branching
- Keyword searches with the `in` operator
- `if __name__ == "__main__"` entry-point guard

## Run

From the repository root:

```bash
python3 python/ticket-triage/ticket_triage.py
```

## Example

```text
Please enter your ticket info: wifi connection is down
network
```

## Category Keywords

| Category | Example keywords |
| --- | --- |
| Password | password, login, reset, locked |
| Network | wifi, VPN, internet, connection |
| Hardware | laptop, keyboard, monitor, printer |
| Software | app, install, update, error |
| General | anything without a known keyword |

## Current Scope

The project uses deterministic keyword matching and keeps no saved ticket history. It is intentionally small so the control flow and categorization logic remain easy to inspect.

## Data Safety

All examples are fictional. The project contains no employer, customer, or internal system data.
