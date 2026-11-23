

# AI/ML Internship — Week 1 and Week 2

## Student Information

- **Name:** Luqman Hayat Gondal
- **Program:** AI/ML Internship
- **Weeks Completed:** Week 1 and Week 2
- **Python Version:** 3.13.17

## Project Description

This repository contains my Week 1 and Week 2 learning tasks for the AI/ML internship.

Week 1 focused on Python fundamentals, reusable modules, file handling, Git, and automated testing.

Week 2 focused on NumPy, Pandas, data inspection, data cleaning, vectorisation, business data analysis, and writing reusable data-cleaning functions with automated tests.

## Development Environment

- Python 3.13.17
- Visual Studio Code
- Git and GitHub
- Jupyter Notebook
- Virtual Environment (`.venv`)

## Project Setup

### 1. Create a virtual environment

```powershell
python -m venv .venv
```

### 2. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Upgrade pip

```powershell
python -m pip install --upgrade pip
```
### 4. Install required packages

```powershell
python -m pip install -r requirements.txt
```

## Project Structure

- `notebooks/` — Jupyter notebooks for learning and practice.
- `week01/` — Week 1 Python exercises, toolkit modules, tests, and project files.
- `week02/` — Week 2 NumPy, Pandas, sales data analysis, and cleaning project.
- `week02/data/raw/` — Original sales and product datasets.
- `week02/data/processed/` — Cleaned sales dataset.
- `week02/docs/` — Week 2 data dictionary and documentation.
- `requirements.txt` — Required Python packages.
- `README.md` — Project documentation.

## Tools I use

- Python 3.13.17
- Visual Studio Code
- Git
- GitHub
- Jupyter Notebook
- pytest
- black

## Running the Project

### Run automated tests

```powershell
python -m pytest -v
```
### Run the log report

```powershell
python .\week01\run_log_report.py
```

## Toolkit Modules

- `stats.py` — Provides reusable statistical functions such as `mean`, `median`, `mode`, `count_by`, and `top_n`.
- `loader.py` — Provides the `DataLoader` class to load CSV, JSON, and text files.
- `log_parser.py` — Provides the `LogEvent` dataclass, `parse_line()` to parse one log line, and `read_events()` to read valid log events while skipping corrupted lines.
- `run_log_report.py` — Runs the log analysis report and displays total, valid, and corrupted log lines.

### Example Usage

#### 1. Statistics

```python
from week01.toolkit.stats import mean

numbers = [10, 20, 30]
print(mean(numbers))
```

#### 2. Data Loader

```python
from pathlib import Path
from week01.toolkit.loader import DataLoader

loader = DataLoader(Path("week01/data"))
records = loader.load_csv("sample.csv")
print(records)
```

#### 3. Log Parser

```python
from pathlib import Path
from week01.toolkit.log_parser import read_events

events = list(read_events(Path("week01/data/auth_practice.log")))
print(events)
```

#### 4. Log Report

```powershell
python .\week01\run_log_report.py week01\data\auth.log
```

## Wednesday Learning Finding

The IP address range 203.0.113.0/24 is reserved for documentation and examples. These addresses are not meant to represent real public internet devices.

## Week 1 Learning Outcomes

- Learned Python basics, including variables, data types, lists, tuples, sets, and dictionaries.
- Practiced Git commands, branching, merging, and resolving merge conflicts.
- Completed Python exercises and practiced debugging errors.
- Created reusable Python modules for statistics, data loading, and log parsing.
- Learned how to write automated tests using pytest.
- Used Black to format Python code.
- Practiced creating branches, commits, and pull requests using GitHub.

## What I Found Hard

- Understanding Python concepts as a beginner.
- Debugging errors and understanding error messages.
- Learning Git branching, merging, and resolving conflicts.
- Understanding how Python modules and automated tests work.

## Daily Learning Log

My daily learning progress, completed tasks, difficulties, and debugging notes for Monday to Friday are recorded in `docs/learning-log.md`.


## Week 2 Development Environment

- Python: 3.13.17
- NumPy: 2.5.4
- Pandas: 3.1.1

All required Python packages are installed in the project's virtual environment (`.venv`).

To install the required packages, run:

```powershell
python -m pip install -r requirements.txt

```

## Week 2 — NumPy, Pandas and Sales Data Analysis

### Week 2 Notebooks

- [Monday: NumPy Exercises](week02/01_numpy_exercises.ipynb)
- [Monday: Vectorisation](week02/02_vectorisation.ipynb)
- [Tuesday: Sales Data Inspection](week02/03_inspect_sales.ipynb)
- [Wednesday: Sales Data Cleaning](week02/04_clean_sales.ipynb)
- [Thursday: Sales Data Analysis — 15 Questions](week02/05_analysis.ipynb)

The Thursday analysis notebook contains answers to all 15 business questions, including revenue analysis, regional performance, product profitability, customer orders, discounts, and order trends.

- [Friday: Final Cleaning Report](week02/06_final_report.ipynb)


### Week 2 Daily Work Summary

#### Monday — NumPy and Vectorisation

- Practiced NumPy arrays, array creation, indexing, slicing, filtering and broadcasting.
- Completed 10 NumPy exercises.
- Created five Python loop functions and their NumPy vectorised versions.
- Compared Python and NumPy results to verify correctness.
- Measured execution times and calculated speed-ups for all five functions.
- Successfully ran both Monday notebooks.

#### Tuesday — Pandas and Data Inspection

- Studied Pandas fundamentals and completed the assigned Kaggle lessons 1–3.
- Loaded and inspected the raw sales dataset using Pandas.
- Examined the dataset's shape, columns, data types and missing values.
- Identified 40 duplicate rows.
- Investigated missing customer names, quantities and discounts.
- Identified inconsistent region and order-status labels.
- Documented the initial data quality issues in the inspection notebook.

#### Wednesday — Sales Data Cleaning

- Removed 40 duplicate rows from the raw sales dataset.
- Standardized region and order-status labels.
- Parsed multiple date formats into a consistent date format.
- Removed dollar signs and commas from prices and converted them into numeric values.
- Identified and removed 43 rows with missing or invalid quantities.
- Filled missing customer names with `Unknown` and missing discounts with `0.0`.
- Calculated revenue after applying discounts.
- Saved the cleaned dataset with 957 rows and 11 columns.
- Verified that the cleaned dataset had no missing values or duplicate rows.

#### Thursday — Business Data Analysis

- Answered all 15 assigned business questions using Pandas.
- Practiced `groupby`, dataset merging and pivot tables.
- Analyzed revenue by region, product, category and month.
- Identified top products and customers using sales data.
- Examined cancelled orders, order statuses and discount patterns.
- Analyzed product profitability by merging sales and product datasets.
- Documented findings and interpretations in the analysis notebook.

#### Friday — Reusable Cleaning Function, Testing and Final Report

- Created the reusable `clean_sales()` function in `sales_cleaning.py`.
- Wrote automated tests for duplicate removal, label standardization, date parsing, price conversion, quantity validation, missing values and revenue calculation.
- Verified that the original DataFrame remains unchanged.
- Successfully ran all 8 automated tests.
- Created a data dictionary documenting all 11 cleaned dataset columns.
- Prepared the final report notebook and successfully executed its cells.
- Checked Python code formatting using Black; both Python files passed the check.


### Reusable Cleaning Function and Tests

The reusable sales cleaning function is available in `week02/sales_cleaning.py`.

To run the automated tests, open the VS Code PowerShell terminal and run:

```powershell
cd week02
python -m pytest -v
```

To format Python files using Black:

```powershell
cd week02
python -m black --check .
```

### Data Dictionary

The cleaned dataset's columns, meanings, data types, allowed values and cleaning rules are documented in [the data dictionary](week02/docs/data_dictionary.md).

### Cleaning Summary

- Original raw dataset: 1,040 rows and 10 columns.
- Final cleaned dataset: 957 rows and 11 columns.
- Exact duplicate rows were removed.
- Invalid and missing quantities were excluded.
- Missing customer names and discounts were handled.
- Dates and prices were converted into appropriate formats.
- Revenue was calculated after applying discounts.

### Wednesday Data Cleaning Log

| Cleaning Step | Action Taken | Result |
|---|---|---|
| Duplicate rows | Removed exact duplicate rows | 40 rows removed |
| Region and status | Removed extra spaces and standardized capitalization | 4 regions and 3 statuses |
| Order dates | Parsed three different date formats | No missing dates |
| Unit prices | Removed dollar signs and commas, converted to float | Numeric prices |
| Quantity | Converted to numeric, marked invalid values as missing, and removed them | 43 rows removed |
| Customer names | Filled missing values with "Unknown" | No missing customer names |
| Discounts | Filled missing values with 0.0 | No missing discounts |
| Revenue | Calculated quantity × unit price × (1 − discount) | Total revenue: 4,162,140.15 |

### Three Surprising Data Observations

1. The raw dataset contained inconsistent region and status labels because of different capitalization and extra spaces.
2. The order dates appeared in multiple formats, so they needed to be standardized before analysis.
3. The quantity column contained negative, zero and unusually large values, which could affect sales analysis if left untreated.

### Monday Vectorisation Timing Results


| Function | Python Loop (seconds) | NumPy (seconds) | Speed-up |
|---|---:|---:|---:|
| Sum of squares | 0.192559 | 0.009248 | 20.82x |
| Z-score | 0.523407 | 0.024992 | 20.94x |
| Count above threshold | 0.148642 | 0.004476 | 33.21x |
| Moving average | 1.155653 | 0.038969 | 29.66x |
| Pairwise distances | 0.661566 | 0.054974 | 12.03x |


### Week 2 Learning Log

Daily learning progress, completed tasks and difficulties are recorded in `docs/learning-log.md`.
