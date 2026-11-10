# Week 1 — Learning Log

## Monday – Environment Setup

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

## Learn Git Branching

### Introduction Sequence

- **Introduction to Git Commits:** Learned how Git records snapshots of tracked files and maintains project history.
- **Introduction to Git Branching:** Learned how to create new branches and switch between them.
- **Introduction to Git Merging:** Learned how to combine changes from different branches.
- **Introduction to Git Rebase:** Learned how Git moves commits onto another base commit.

### Ramping Up

- **Detach yo HEAD:** Learned how to move HEAD directly to a specific commit instead of pointing to a branch.
- **Relative Refs:** Learned how to navigate through commit history using relative references.
- **Relative Refs #2:** Practiced moving HEAD to specific commits using relative references.
- **Reversing Changes:** Learned how to undo changes in Git.


## Tuesday Self-Check

1. The staging area lets me choose specific changes for the next commit instead of committing all modified files.

2. Branches let us work on new features separately without affecting the main branch. Changes can be reviewed before merging.

3. I read the last line of a traceback first because it shows the error type and message.

4. A merge conflict happens when Git cannot automatically combine competing changes. I fixed mine by choosing the correct version, removing conflict markers, and committing the resolved file.

## Wednesday – Python Data Structures and Exercises

### What I learned
- Practiced Python functions and docstrings.
- Learned lists, tuples, sets, and dictionaries.
- Used Counter to count word frequencies.
- Practiced list and dictionary comprehensions.
- Worked with CSV and JSON files.
- Learned exception handling using try and except.
- Practiced generators and defaultdict.
- Used assertions to test my functions.

### What I found difficult
- Understanding dictionary comprehension.
- Understanding Counter and generators.
- Writing correct assertions.
### Progress
- Completed Exercises 1–14 successfully.
- Completed Exercise 15 (Log Analyser) using the authentication log file.
- Successfully analysed 403 total lines, 400 valid events and 3 corrupted lines.
- Displayed event counts by IP address and event type.
- Identified the top IP addresses with failed logins.
- Identified users with more than 5 failed logins from one IP.
- Identified that 203.0.113.x belongs to the TEST-NET-3 range, reserved for documentation and examples, not evidence of real suspicious activity.

## Thursday – Reusable Toolkit Package

### What I Learned
- Learned how to organize Python code into reusable modules.
- Understood the purpose of `__init__.py`.
- Practiced importing functions and classes from different modules.
- Learned how to use `pathlib` to work with file paths.

### What I Built
- Created a `toolkit` package inside the `week01` folder.
- Created reusable modules: `stats.py`, `loader.py`, and `log_parser.py`.
- Created `run_log_report.py` to run the log report.
- Tested the toolkit modules.

### What I Found Difficult
- Understanding Python imports.
- Organizing files into packages.
- Understanding how modules work together.

### Progress
- Created and tested the reusable toolkit package.
- Added the toolkit work to GitHub.

## Friday – Automated Testing and Code Formatting

### What I Learned
- Learned the basics of automated testing with pytest.
- Practiced writing test functions.
- Understood how assertions check expected results.
- Learned how to format Python code using Black.
- Practiced checking code quality.

### What I Built
- Created automated tests for the toolkit modules.
- Added test files inside the `tests` folder.
- Installed and used pytest.
- Used Black to check Python code formatting.

### What I Found Difficult
- Understanding how to write test cases.
- Finding and fixing errors in tests.
- Understanding code formatting rules.

### Progress
- Successfully ran all 14 automated tests; all tests passed.
- Black formatting check passed for all Python files.
- `pip check` completed with no broken requirements.
- Verified the log report output: 403 total lines, 400 valid events and 3 corrupted lines.
- Installed project dependencies in a clean virtual environment and verified the project setup.
- Pushed the completed work to GitHub.