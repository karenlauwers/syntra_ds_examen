## Context & assumptions
This is an data analysis assignment about analyzing births in 2019 in Belgium. The data are represented in csv-files in /data. The filename represents the real or effective day of birth, xxxx-x-x or xxxx-xx-xx, year-month-day. The column names are in Dutch. The columns in each csv-file are gemeente (place of birth), naam (name), geslacht (gender), verwachte_datum (expected day of birth). We will read the csv-files into a dataframe. 

- Files live under /data, one CSV per calendar day in 2019, named YYYY-M-D.csv or YYYY-MM-DD.csv.
- Only valid calendar dates are allowed; e.g., 2019-2-29.csv must be skipped (2019 isn’t a leap year).
- CSV columns (Dutch): gemeente (place of birth), naam (name), geslacht (gender), verwachte_datum (expected date of birth).
- One row ≙ one baby.
- No external data is required; all signals come from filenames + CSV content.
  
## Goals & scope
Goal: Build a single, clean pandas DataFrame for all valid dates in 2019, with two added columns:
- date_of_birth — parsed from the filename, dtype datetime (date precision).
- source — the filename each row came from.

We will use this DataFrame to answer different kinds of data analysis questions like (among others): 
- Mean number of births per day (2019)
- Outlier days (unusually high/low counts)
- Relationships between days/weeks/months and daily births; weekday pattern
- Relationship between actual birth date and expected birth date
- Names that appear in both female and male groups; counts and examples
- Number of unique names and number of births (overall and by gender)
- A simple linear regression to explain births and frequency of names

Non‑goals: individual‑level prediction or external demographic/holiday datasets.

## Data contracts & schema
### Input CSV schema (per file)
Columns:
- gemeente → string
- naam → string
- geslacht → string (expected values like M, V, X, m, v, x, or Dutch words; normalize later)
- verwachte_datum → date (parseable; may be missing)

Encoding: utf-8 or utf-8-sig (auto‑handle BOM).

Delimiter: , (comma). If ambiguous, allow auto‑detection with Python engine fallback.

### Output master DataFrame schema
- gemeente → string (trimmed)
- naam → string (trimmed; original case preserved; keep a normalized copy for analysis)
- geslacht → category with levels: F, M, X, Unknown
- verwachte_datum → datetime64[ns] (NaT allowed)
- Added: date_of_birth → datetime64[ns], derived from filename (date only)
- Added: number of day 1 - 365, 1 for 1/1/2019, 2 for 1/2/2019 etc

### Constraints:
- date_of_birth must be not null for all rows.
- Only include rows from valid calendar filenames in 2019.
- Do not inferverwachte_datum from filename; only from CSV.

## File discovery & validation rules
### List candidates: all files under /data matching regex:
^2019-\d{1,2}-\d{1,2}\.csv$ (basename).
Validate date part:
- Split on - → (YYYY, M, D).
- Construct datetime.date(YYYY, M, D) in a try/except; if it fails → skip file.
- Enforce year == 2019.

### Logging: Keep two lists:
- loaded_files: valid files ingested.
- skipped_files: invalid filenames (e.g., 2019-2-29.csv, malformed, wrong year).

## Quality, logging, and tests
### Quality checks
Assert:
All date_of_birth are in 2019.
Number of unique date_of_birth ≤ 365.
No rows from invalid filenames (use skipped_files log).
births_per_day.births.sum() == len(df).

### Nulls:
Count nulls per column; verwachte_datum may be NaT; others should be near‑zero null after string cleaning.