# Data Quality Toolkit

A reusable Python package for data quality assessments on tabular datasets using Pandas.

---

## Installation

```bash
pip install git+https://github.com/Kwame842/data_quality_toolkit.git
```

Or clone and install locally:

```bash
git clone https://github.com/Kwame842/data_quality_toolkit.git

cd data_quality_toolkit

pip install -e .
```

---

## Quick Start

```python
import pandas as pd
from data_quality_toolkit.profiling import profile_dataframe, find_duplicates
from data_quality_toolkit.reporting import generate_quality_report

df = pd.read_csv("your_data.csv")

# Profile your data
profile = profile_dataframe(df)

# Check for duplicates
duplicates = find_duplicates(df)
print(f"Duplicate rows: {duplicates['count']}")

# Generate a full quality report
report = generate_quality_report(df, output_file="report/quality_report.json")
```

---

## Usage

### Profile a DataFrame

Returns column-level statistics — dtype, null counts, unique values, min/max/mean/median.

```python
from data_quality_toolkit.profiling import profile_dataframe

profile = profile_dataframe(df)
print(profile)
```

```json
{
  "customer_id": {
    "dtype": "int64",
    "nulls": 0,
    "null_pct": 0.0,
    "unique": 1000,
    "min": 1,
    "max": 1000,
    "mean": 500.5,
    "median": 500.5
  }
}
```

### Find Duplicates

```python
from data_quality_toolkit.profiling import find_duplicates

duplicates = find_duplicates(df)
print(duplicates["count"])   # number of duplicate rows
print(duplicates["rows"])    # the duplicate records
```

### Generate a Quality Report

Produces a full summary — row/column counts, duplicates, null columns, and the complete profile — saved as JSON.

```python
from data_quality_toolkit.reporting import generate_quality_report
from pathlib import Path

report_dir = Path("report")
report_dir.mkdir(exist_ok=True)

report = generate_quality_report(df, output_file=report_dir / "quality_report.json")
```

```json
{
  "total_rows": 1000,
  "total_columns": 12,
  "duplicate_rows": 5,
  "columns_with_nulls": 3,
  "profile": { "..." }
}
```

---

## Dependencies

- `pandas`
- `numpy`

---

## License

MIT - see [LICENSE](LICENSE) for details.
