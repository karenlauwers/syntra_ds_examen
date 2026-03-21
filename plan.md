# Plan: Belgian Births 2019 — Exam Assignment

## Context
Karen needs to complete a Syntra data science exam analyzing simulated Belgian birth data for 2019. The assignment is in notebooks/opgave.ipynb (read-only reference with expected outputs). We'll work in notebooks/opgave_copy.ipynb step by step.
Working Notebook
notebooks/opgave_copy.ipynb — all code goes here.

## Steps (in order)
### Stap 1: Data Inlezen (1 pt)
•	First: populate config.py with DATA_DIR, column names, and other stable variables
•	Discover all CSV files in data/ matching 2019-M-D.csv pattern
•	Validate dates (skip invalid like 2019-2-29), log loaded/skipped files
•	Build df_births with columns: gemeente, naam, geslacht, verwachte_datum (renamed from verwachte datum), geboortedatum (datetime from filename), dag_van_het_jaar (1-365)
•	Show checks: row count, min/max geboortedatum, min/max dag_van_het_jaar, no invalid dates

### Stap 2: EDA
•	Q1 (1pt): Plot births per day with horizontal red dashed mean line
•	Q2.1 (1pt): Find outliers using a defensible rule: 
    We will use 2 methods to define outliers, method=IQR (Interquartile range) 
    Rules to apply: 
    the birth count on a day is an outlier if it lies outside Q1 – 1.5·IQR or Q3 + 1.5·IQR.
•	Q2.2 (1pt): Remediate 2 outlier days, store bad rows in df_wrong, remake Q1 plot with df_births_clean
•	Q2.3 (1pt): Identify 8 most extreme days in H2 of 2019
•	Q3.1 (2pt): Smoothed plot — average births per week (rolling 7-day by weekday)
•	Q3.2 (2pt): Average births per weekday (bar chart)
•	Q3.3 (3pt): Monthly births with 95% CI (pointplot/barplot or boxplot with error bars)
•	Q3.4 (4pt): Weekday effect by season (boxplot, different plots in a figure)

### Stap 3: Research Questions
•	Onderzoek 1 — Unisex names:
o	Q1.1 (3pt): df_name_gender table, find names in both genders, top 3 per category
o	Q1.2 (2pt): "Real unisex" filter (x <= 1.5y and y <= 1.5x), df_real_unisex
o	Q1.3 (1pt): Compare % men vs % women with unisex name
o	Q1.4 (2pt): Visualization of real unisex names by gender
•	Onderzoek 2 — Expected vs actual birth date:
o	Q2.1 (3pt): Overlay actual vs expected births per day
o	Q2.2 (1pt): Explain edge effects at start/end of year (comment)
o	Q2.3 (3pt): Histogram of days-early distribution with median & P90
o	Q2.4 (4pt): Scatter per top-8 gemeente with reference line
•	Onderzoek 3 — Names vs babies:
o	Q3.1: Investigate relationship between # babies and # unique names
o	Random sampling analysis, frequency as derived variable
o	Linear regression on n_births > 10,000
o	Log transformation for full-range fit
o	Validation plots

## Approach
We work one step at a time. For each step:
1.	I write the code cells directly in notebooks/opgave.ipynb or Karen has written code and I review the code - Karen specifies in each step whether to write or to review/improve. 
2.	Karen reviews, analysis the steps taken, asks for clarification if needed, checks understanding, and runs them
3.	We verify output matches expected results
4.	Move to next step

## Project Structure Conventions
•	src/syntradsexamen/config.py — All filepaths and stable variables go here (DATA_DIR, column names, etc.)
•	src/syntradsexamen/styling.py — Karen will add the teacher's styling first, then I review for completeness/correctness
•	Shared code lives in the package; notebooks import from it

## Column Naming Conventions
•	Rename CSV column verwachte datum (with space) → verwachte_datum
•	Birth date from filename → geboortedatum (datetime)
•	Day of year → dag_van_het_jaar (integer 1-365, where 2019-01-01 = 1, 2019-01-02 = 2, etc.)

## Key Data Notes
•	Gender values: Mannelijk, Vrouwelijk (Dutch)
•	Expected date format in CSV: US format MM/DD/YYYY
•	Outlier days from reference output: 2019-01-01 and 2019-07-01
•	8 extreme H2 days include holidays: Jul 21, Aug 15, Nov 1-2, Nov 11, Dec 24-26

## Verification
•	Compare outputs cell-by-cell against opgave.ipynb reference
•	Check row counts, specific values shown in expected outputs
