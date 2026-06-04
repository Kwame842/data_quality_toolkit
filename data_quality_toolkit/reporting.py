import json

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
        "duplicate_rows":
            find_duplicates(df)["count"],
        "columns_with_nulls":
            int((df.isnull().sum() > 0).sum()),
        "profile":
            profile_dataframe(df)
    }

    if output_file:

        with open(
            output_file,
            "w"
        ) as f:

            json.dump(
                report,
                f,
                indent=4
            )

    return report