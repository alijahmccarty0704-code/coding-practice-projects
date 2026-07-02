# Java Knowledge Check 2: Help Desk Checklist CLI

This is a workplace-safe practice project using fake support scenarios only. Do not use real workplace tickets, customer names, internal system names, screenshots, or restricted details.

Create a command-line app from scratch named `HelpDeskChecklist.java`.

## Scenario

You are building a simple checklist helper for generic help-desk practice.

The user can:

- View fake support scenarios
- Choose a scenario
- Print a checklist for that scenario
- Exit the app

Scenarios:

- Password reset
- Network issue
- Printer issue

## Concepts Being Tested

- `Scanner`
- `String` input
- `Integer.parseInt()`
- `try` / `catch NumberFormatException`
- helper methods
- arrays and indexes
- `if` / `else if` / `else`
- `while` loops
- `for` loops
- method parameters and return values
- Git status, diff, staging, and commit workflow

## Build Checklist

### Checkpoint 1: Create The File, Compile, And Run

- [ ] Create `HelpDeskChecklist.java`.
- [ ] Add `import java.util.Scanner;`.
- [ ] Add `public class HelpDeskChecklist`.
- [ ] Add `public static void main(String[] args)`.
- [ ] Compile the file.
- [ ] Run the file.
- [ ] Confirm the menu appears.
- [ ] Choose exit.

Run:

```bash
cd java-hour/knowledge-checks/02-help-desk-checklist
javac HelpDeskChecklist.java
java HelpDeskChecklist
```

### Checkpoint 2: Menu Input Helper

Create:

```java
public static int getMenuChoice(Scanner scnr)
```

The helper should:

- Read input as a `String`.
- Return the parsed integer for valid whole-number input.
- Return `-1` for invalid input.

Stop and explain:

- Why does Java use `Integer.parseInt()` here?
- What does `-1` signal?

### Checkpoint 3: Scenario Labels

Use this array:

```java
String[] scenarios = {"Password reset", "Network issue", "Printer issue"};
```

- [ ] Print the scenarios with numbers.
- [ ] Use indexes correctly.
- [ ] Remember that menu option `1` maps to array index `0`.

Stop and explain:

- Why does `choice - 1` access the correct array item?

### Checkpoint 4: Checklist Output

Complete:

```java
public static void printChecklist(String scenario)
```

Rules:

- Password reset should print generic identity, reset, and follow-up steps.
- Network issue should print generic connection, restart, and escalation steps.
- Printer issue should print generic power, queue, and test-page steps.

Use fake/generic wording only.

### Checkpoint 5: Invalid Menu Input

- [ ] Invalid text should not crash the app.
- [ ] Out-of-range numbers should print an invalid option message.
- [ ] Exit option should end cleanly.

Manual test:

```text
pizza
4
1
4
```

Expected:

- `pizza` prints invalid input
- `4` exits if `4` is the exit option
- choosing `1` prints the password reset checklist

## Git Checkpoints

Use Git from the workspace root:

```bash
git status
git diff
git add java-hour/knowledge-checks/02-help-desk-checklist/README.md
git diff --staged
git commit -m "Add Java help desk checklist instructions"

# After you create HelpDeskChecklist.java:
git status
git diff
git add java-hour/knowledge-checks/02-help-desk-checklist/HelpDeskChecklist.java
git diff --staged
git commit -m "Add Java help desk checklist practice"
git log --oneline -3
```

Before committing, explain:

- What files are staged?
- What Java concepts did you practice?
- Why should `.class` files stay out of the commit?
