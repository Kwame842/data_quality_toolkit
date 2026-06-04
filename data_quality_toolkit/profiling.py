import pandas as pd


def find_duplicates(df: pd.DataFrame, subset=None):
    """
    Find duplicate rows.
    """

    duplicates = df[df.duplicated(subset=subset)]

    return {
        "count": len(duplicates),
        "rows": duplicates
    }


def profile_dataframe(df: pd.DataFrame):
    """
    Generate column profiling statistics.
    """

    profile = {}

    total_rows = len(df)

    for col in df.columns:

        profile[col] = {
            "dtype": str(df[col].dtype),
            "nulls": int(df[col].isnull().sum()),
            "null_pct": round(
                (df[col].isnull().sum() / total_rows) * 100,
                2
            ),
            "unique": int(df[col].nunique())
        }

        if pd.api.types.is_numeric_dtype(df[col]):

            profile[col]["min"] = float(df[col].min())
            profile[col]["max"] = float(df[col].max())
            profile[col]["mean"] = round(
                float(df[col].mean()),
                2
            )
            profile[col]["median"] = round(
                float(df[col].median()),
                2
            )

    return profile