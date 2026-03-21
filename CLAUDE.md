# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Data analysis exam project analyzing simulated Belgian birth data for 2019. The analysis is done in Jupyter notebooks using pandas, with visualizations in matplotlib/seaborn and modeling via scikit-learn.

## Setup

```bash
conda env create -f environment.yml
conda activate syntra_ds_examen
pip install -e .
```

## Architecture

- **`data/`** — One CSV per calendar day in 2019, named `YYYY-M-D.csv` (e.g., `2019-1-1.csv`). Each row is one birth with columns: `gemeente`, `naam`, `geslacht`, `verwachte datum`. Gitignored.
- **`notebooks/opgave.ipynb`** — The main assignment notebook (read-only reference with questions and expected outputs).
- **`notebooks/opgave_copy.ipynb`** — Working copy for solutions.
- **`src/syntradsexamen/`** — Installable package (`pip install -e .`) for shared utilities (config, styling). Currently mostly empty stubs.
- **`specs.md`** — Detailed data contracts, validation rules, and schema definitions.

## Data Conventions

- CSV filenames encode the actual birth date; column `verwachte datum` is the expected date (US date format `MM/DD/YYYY`).
- Gender values are Dutch: `Mannelijk` (male), `Vrouwelijk` (female). Normalize to `M`, `F`, `X`, `Unknown` per specs.
- Invalid dates like `2019-2-29` (not a leap year) must be skipped during file discovery.
- The master DataFrame should add `date` (datetime from filename) and `dag_van_jaar` (1-365) columns.

## Key Dependencies

Python 3.11, pandas 2.2, numpy 1.26, scikit-learn 1.5, matplotlib 3.9, seaborn 0.13, scipy, tqdm.
