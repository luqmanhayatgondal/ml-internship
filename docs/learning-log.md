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

### GitHub Pull Request and Merge Conflict

- Created and pushed the `feature/readme-tools` branch.
- Added the "Tools I use" section to README.
- Created Pull Request #2 on GitHub and successfully merged it into `main`.
- Practiced a deliberate Git merge conflict.
- Resolved the conflict by selecting the correct changes, removing conflict markers, and committing the resolved file.
- Cleaned up the practice branch and temporary demo file.


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

# Week 2 — Learning Log

## Monday — NumPy and Vectorisation

### What I Learned
- Learned to create NumPy arrays using `arange` and `reshape`.
- Practiced array indexing, slicing, filtering and conditional replacement.
- Learned row sums, column means and broadcasting.
- Understood the difference between array views and copies.
- Learned vectorisation and compared Python loops with NumPy operations.

### What I Built
- Created `01_numpy_exercises.ipynb` with 10 NumPy exercises.
- Created `02_vectorisation.ipynb` with five Python loop functions and their NumPy versions.
- Compared Python and NumPy results.
- Measured execution times and calculated speed-ups.
- Added a performance comparison table and conclusion.
- Updated `requirements.txt` with NumPy 2.5.4 and Pandas 3.1.1.
- Updated README with environment versions.

### What I Found Difficult
- Understanding NumPy broadcasting.
- Understanding views and copies.
- Understanding vectorisation and performance comparisons.

### Progress
- Successfully executed both Monday notebooks.
- Verified that all five NumPy functions produced matching results with their Python loop versions.
- Restarted the kernel and ran all cells successfully.
## Tuesday 10 November 2026 – pandas Basics and Data Inspection

### What I Learned
- Learned the difference between pandas Series and DataFrames.
- Practiced reading CSV files and inspecting data using head(), info(), describe() and value_counts().
- Learned to select and filter data using brackets, loc and iloc.

### What I Built
- Created 03_inspect_sales.ipynb.
- Inspected the original sales dataset containing 1,040 rows and 10 columns.
- Identified 40 duplicate rows and missing values in customer, quantity and discount.
- Examined inconsistent region and status labels, quantity values and date formats.

### What Blocked Me and How I Got Past It
- Understanding the different data types and inspection results was difficult.
- Practiced the pandas inspection methods step by step.

### Questions for My Mentor
- How should I decide whether a missing value should be filled or its row removed?

### Tomorrow's Plan
- Clean the sales dataset and document each cleaning decision.

## Wednesday 11 November 2026 – Data Cleaning

### What I Learned
- Learned how to remove duplicates and standardize text values.
- Practiced converting price strings into numeric values.
- Learned to parse multiple date formats explicitly.
- Understood when to drop invalid rows and when to fill missing values.

### What I Built
- Created 04_clean_sales.ipynb.
- Removed 40 duplicate rows.
- Standardized region and status values.
- Converted dates and unit prices into appropriate data types.
- Removed 43 rows with invalid or missing quantities.
- Filled missing customer and discount values.
- Calculated revenue and saved the cleaned dataset.

### What Blocked Me and How I Got Past It
- Handling different date formats and deciding what to do with invalid quantities required extra practice.
- Used explicit date formats and checked the results after each cleaning step.

### Questions for My Mentor
- In which situations is filling a missing quantity better than dropping its row?

### Tomorrow's Plan
- Analyze the cleaned sales data using groupby, merge and pivot tables.

## Thursday 12 November 2026 – Sales Data Analysis

### What I Learned
- Learned the split-apply-combine approach using groupby.
- Practiced merging tables using matching columns.
- Learned to create pivot tables and analyze dates using pandas.
- Understood how to summarize business data.

### What I Built
- Created 05_analysis.ipynb.
- Worked through 15 business questions about sales.
- Analyzed revenue, regions, products, customers, discounts, profit and order status.
- Used groupby, merge, pivot_table and date operations.

### What Blocked Me and How I Got Past It
- Understanding how different pandas operations produce summary tables was challenging.
- Practiced the operations using the sales dataset and checked the results.

### Questions for My Mentor
- How can I check that a merge has not unexpectedly increased the number of rows?

### Tomorrow's Plan
- Convert the cleaning notebook logic into a reusable Python function and test it.

## Friday 13 November 2026 – Consolidation, Testing and Documentation

### What I Learned
- Learned why reusable functions make data cleaning easier to maintain.
- Practiced writing automated tests with pytest.
- Understood how to document dataset columns in a data dictionary.
- Learned to check Python formatting with Black.

### What I Built
- Created sales_cleaning.py with the clean_sales() function.
- Created tests/test_sales_cleaning.py with eight tests.
- Created 06_final_report.ipynb.
- Created the data dictionary describing all 11 cleaned dataset columns.
- Updated the project README and requirements documentation.
- Verified that all eight pytest tests passed in a fresh virtual environment.
- Ran all cells in 06_final_report.ipynb successfully without errors.

### What Blocked Me and How I Got Past It
- Understanding how to test each cleaning rule independently was challenging.
- Used small test DataFrames and assertions to check the expected results.

### Questions for My Mentor
- What improvements should I make to my cleaning function and tests before using them in a larger project?

### Tomorrow's Plan
- Review the week's work, revise the pandas and NumPy concepts, and prepare for the mentor review.

