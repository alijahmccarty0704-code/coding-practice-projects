# Help Desk Checklist CLI

A Java command-line application that prints troubleshooting checklists for three fake support scenarios.

## Features

- Offers password-reset, network, and printer scenarios.
- Maps numbered menu choices to scenario labels stored in an array.
- Prints a scenario-specific troubleshooting checklist.
- Handles nonnumeric and out-of-range menu input.
- Repeats until the user selects Exit.

## Technical Highlights

- `Scanner` input
- `Integer.parseInt()` with `NumberFormatException` handling
- Static helper methods with parameters and return values
- Arrays and `choice - 1` index mapping
- String comparison with `.equals()`
- Repeating menu flow with `while`

## Compile And Run

From the repository root:

```bash
cd java/help-desk-checklist
javac HelpDeskChecklist.java
java HelpDeskChecklist
```

## Supported Scenarios

| Option | Scenario | Checklist focus |
| --- | --- | --- |
| 1 | Password reset | Account identification, reset, verification |
| 2 | Network issue | Connection scope, restart, outage, escalation |
| 3 | Printer issue | Power, paper, queue, test print, escalation |
| 4 | Exit | Ends the application |

## Current Scope

The scenarios and checklist text are fixed in the source code. The project focuses on Java methods, array indexing, validation, and predictable CLI behavior.

## Data Safety

Every scenario is generic and fictional. The project contains no real tickets, accounts, customer names, or internal procedures.
