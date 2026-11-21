

# ML Internship — Week 1

## Student Information

- **Name:** Luqman Hayat Gondal
- **Program:** AI/ML Internship
- **Week:** 01
- **Python Version:** 3.13.17

## Project Description

This repository contains my Week 1 learning tasks and Python practice for the AI/ML internship.

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

- `notebooks/` — Jupyter notebooks.
- `week01/` — Week 1 Python exercises and project code.
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
- [Friday: Final Cleaning Report](week02/06_final_report.ipynb)

### Reusable Cleaning Function and Tests

The reusable sales cleaning function is available in `week02/sales_cleaning.py`.

To run the automated tests, open the VS Code PowerShell terminal and run:

```powershell
cd week02
python -m pytest -v
```

To format Python files using Black:

```powershell
python -m black ..
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

### Three Surprising Data Observations

1. The raw dataset contained inconsistent region and status labels because of different capitalization and extra spaces.
2. The order dates appeared in multiple formats, so they needed to be standardized before analysis.
3. The quantity column contained negative, zero and unusually large values, which could affect sales analysis if left untreated.

### Monday Vectorisation Timing Results

| Operation | Python Loop (seconds) | NumPy (seconds) | Speedup |
|---|---:|---:|---:|
| Sum of squares | 0.223392 | 0.034877 | 6.41x |
| Z-score | 2.098556 | 0.108647 | 19.32x |
| Count above threshold | 0.190069 | 0.006695 | 28.39x |
| Moving average | 2.384449 | 0.039255 | 60.74x |
| Pairwise distances | 1.153573 | 0.192637 | 5.99x |

### Week 2 Learning Log

Daily learning progress, completed tasks and difficulties are recorded in `docs/learning-log.md`.
