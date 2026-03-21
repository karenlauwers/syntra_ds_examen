from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
SCRIPTS_DIR = PROJECT_ROOT / "scripts"

# ── Data constants ─────────────────────────────────────────────────────
YEAR = 2019

# Original CSV column names (as they appear in the files)
CSV_COLUMNS = ["gemeente", "naam", "geslacht", "verwachte datum"]

# Renamed / added columns in the master DataFrame
COL_GEMEENTE = "gemeente"
COL_NAAM = "naam"
COL_GESLACHT = "geslacht"
COL_VERWACHTE_DATUM = "verwachte_datum"      # renamed from "verwachte datum"
COL_GEBOORTEDATUM = "geboortedatum"          # datetime parsed from filename
COL_DAG_VAN_HET_JAAR = "dag_van_jaar"    # 1-365

# Gender mapping (Dutch → short code)
GENDER_MAP = {
    "Mannelijk": "M",
    "Vrouwelijk": "V",
}
