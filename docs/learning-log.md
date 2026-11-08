# Week 1 — Learning Log

## Environment Setup

**Completion Date:** 6 November 2026

### What I Learned
- Basic Python environment setup.
- How to create and activate a virtual environment.
- How to install Python packages using pip.
- Basic use of VS Code, Git and GitHub.
- How to use Jupyter Notebook.

### What I Built
- Created the ML Internship project.
- Created and activated `.venv`.
- Installed pytest, black and ipykernel.
- Created `requirements.txt`.
- Created an environment-check notebook.
- Updated the project README.

### Blockers and How I Solved Them
- Faced some issues while creating project folders.
- Learned to create folders separately using PowerShell.
- Checked the README file using UTF-8 encoding.

### Questions for Mentor
- I would appreciate guidance on the next steps and priorities for the upcoming tasks.

### Tomorrow's Plan
- Review the concepts covered during Week 1.
- Practice Python programming.
- Continue working on the remaining internship tasks.

## Tuesday – Debugging Practice (Task C)

### Snippet 1 – NameError
- Error: `NameError: name 'totl' is not defined. Did you mean: 'total'?`
- Cause: Variable ka naam galat likha gaya tha.
- Fix: `totl` ko `total` se replace kiya.

### Snippet 2 – TypeError
- Error: `TypeError: can only concatenate str (not "int") to str`
- Cause: String aur integer ko `+` se directly combine kiya gaya.
- Fix: `print("Total:", 5)` use kiya.

### Snippet 3 – IndexError
- Error: `IndexError: list index out of range`
- Cause: List mein index 3 available nahi tha.
- Fix: `items[3]` ko `items[2]` kiya.

### Snippet 4 – KeyError
- Error: `KeyError: 'port'`
- Cause: Dictionary mein `port` naam ki key maujood nahi thi.
- Fix: Existing key `host` use ki.

### Snippet 5 – ValueError
- Error: `ValueError: invalid literal for int() with base 10: 'forty-two'`
- Cause: `int()` word "forty-two" ko integer mein convert nahi kar sakta.
- Fix: `int("42")` use kiya.

### Snippet 6 – ModuleNotFoundError
- Error: `ModuleNotFoundError: No module named 'matplotlibb'`
- Cause: Matplotlib module ka naam galat type kiya gaya tha.
- Fix: `matplotlibb` ko `matplotlib` kiya aur missing library install ki.

### Snippet 7 – Mutable Default Argument
- Error: No traceback; unexpected output was produced.
- Cause: Default empty list dono function calls mein reuse ho rahi thi.
- Fix: Default argument `None` rakha aur function ke andar new list banayi.
- Correct output: `['a']` and `['b']`.

### VS Code Debugger Practice
- Used VS Code Debugger to debug Snippet 1 and Snippet 2.
- Set breakpoints on the code lines.
- Used F5 to start debugging and F10 to execute code step by step.
- Observed the yellow highlight to understand which line was executing.
- Successfully checked the output of both snippets.
