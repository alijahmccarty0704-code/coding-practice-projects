# Failed Login Analyzer

A Python command-line application that reviews fake failed-login records and identifies repeated failures by username.

## Features

- Adds fake login records containing a username, IP address, and failure reason.
- Displays all current records with readable labels.
- Counts failures for a username selected by the user.
- Flags usernames with three or more failed attempts.
- Prevents duplicate usernames in the high-risk report.
- Handles invalid menu input and empty lists.

## Technical Highlights

- Nested lists used as structured records
- Record-field access through indexes
- Counters and conditional matching
- Nested loops for aggregate analysis
- Duplicate prevention with `not in`
- Menu validation and clean exit behavior

## Run

From the repository root:

```bash
python3 python/failed-login-analyzer/failed_login_analyzer.py
```

## Example Analysis

After three records are added for `alex.demo`:

```text
Enter the username you would like to view the logs for: alex.demo
alex.demo 3

High Risk:
['alex.demo']
```

## Current Scope

Records exist only for the current session. The analyzer uses lists and nested loops rather than persistent storage or external log files.

## Data Safety

All usernames, addresses, and failure reasons are fictional. No real authentication logs or internal system details are included.
