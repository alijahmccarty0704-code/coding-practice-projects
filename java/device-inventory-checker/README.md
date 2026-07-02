# Java Knowledge Check 3: Device Inventory Checker

Build this from scratch. Use fake practice data only. Do not use real workplace devices, asset tags, usernames, internal systems, screenshots, or restricted details.

## Scenario

Create a small CLI app for reviewing fake device inventory.

## Required Features

- Show a main menu.
- Display a numbered list of fake devices.
- Let the user choose a device by number.
- Print a generic status/checklist for the selected device.
- Handle invalid text input.
- Handle out-of-range numbers.
- Exit the app cleanly.

## Rules

- Use arrays for device names and statuses.
- Use menu numbers that map correctly to array indexes.
- Use at least one helper method.
- Use at least one `for` loop.
- Do not crash on invalid input.
- Keep all device data fake and generic.

## Concepts To Practice

- `Scanner`
- `String` input
- `Integer.parseInt()`
- `try` / `catch NumberFormatException`
- arrays
- indexes
- `choice - 1`
- helper methods
- `while` loops
- `for` loops
- `if` / `else if` / `else`
- Git status, diff, staging, and commits

## Manual Tests

Test these flows:

```text
show device list
choose device 1
choose device 2
enter text instead of a number
enter a number that is too high
exit
```

Expected behavior:

- Device choices print the matching fake status/checklist.
- Text input prints an invalid input message.
- Out-of-range numbers print an invalid option message.
- Exit ends cleanly.
- The app compiles with `javac` and runs with `java`.

## Git Checkpoints

From the workspace root:

```bash
git status
git diff
git add java-hour/knowledge-checks/03-device-inventory-checker/README.md
git diff --staged
git commit -m "Add Java device inventory checker instructions"
```

After you create the app file:

```bash
git status
git diff
javac java-hour/knowledge-checks/03-device-inventory-checker/DeviceInventoryChecker.java
git status --ignored --short java-hour/knowledge-checks/03-device-inventory-checker
git add java-hour/knowledge-checks/03-device-inventory-checker
git diff --staged
git commit -m "Add Java device inventory checker practice"
git log --oneline -3
```

Before committing, explain what changed and why generated `.class` files should stay out of the commit.
