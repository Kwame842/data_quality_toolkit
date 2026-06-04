import json
from pathlib import Path
from datetime import datetime

from .profiling import (
    find_duplicates,
    profile_dataframe
)


def generate_quality_report(
        df,
        output_file=None
):
    """
    Generate complete quality report.
    """

    report = {
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "duplicate_rows": find_duplicates(df)["count"],
        "columns_with_nulls": int(
            (df.isnull().sum() > 0).sum()
        ),
        "profile": profile_dataframe(df)
    }

    # Auto-generate file path if none supplied
    if output_file is None:

        reports_dir = Path.cwd() / "reports"
        reports_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        output_file = (
            reports_dir /
            f"quality_report_{timestamp}.json"
        )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            report,
            f,
            indent=4
        )

    return report