# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running files

```
python day1\hello.py
python day1\datatypes.py
python todo-app\concepts.py
python todo-app\todo.py
```

No build step, package manager, or dependencies — plain Python scripts, run directly.

## Project structure

This is a beginner Python learning course. Each folder represents a day or topic:

- **`day1/`** — variables, data types, string concatenation, `print()`, `str()` conversion
- **`todo-app/`** — lists, loops, `if/elif/else`, `input()`, and a complete interactive CLI app

## Code style

- String concatenation with `+` (not f-strings) — intentional for beginner clarity
- No functions or classes yet — all code is top-level procedural
- `todo-app/todo.py` is the most complete file: it uses a `while True` loop with `break`, `.strip().lower()` on input, and `.isdigit()` for safe integer validation
