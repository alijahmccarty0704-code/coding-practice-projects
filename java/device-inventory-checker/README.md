# Device Inventory Checker

A Java command-line application that displays fictional device inventory totals from parallel arrays.

## Features

- Displays Laptop, Desktop, VM, and Exit menu options.
- Prints the matching fictional inventory total for a selected device type.
- Converts user-facing menu numbers to zero-based array indexes.
- Handles text and out-of-range numeric input without crashing.
- Repeats until the user selects Exit.

## Technical Highlights

- `Scanner` input and numeric parsing
- `try` / `catch NumberFormatException`
- Parallel arrays
- `for` loop menu display
- `while` loop application lifecycle
- Range validation with `&&`
- `menuSelection - 1` index mapping

## Compile And Run

From the repository root:

```bash
cd java/device-inventory-checker
javac DeviceInventoryChecker.java
java DeviceInventoryChecker
```

## Example

```text
1. Laptop Inventory
2. Desktop Inventory
3. VM Inventory
4. Exit

Selection: 2
Desktops: 100
```

## Current Scope

Inventory totals are fixed, fictional values stored in memory. A future class-based version could represent each device type as an object and load inventory from a file.

## Data Safety

All inventory values are fictional. No real devices, asset tags, users, or workplace systems are represented.
