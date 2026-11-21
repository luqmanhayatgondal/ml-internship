import pandas as pd


def clean_sales(raw: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw sales data and return a cleaned DataFrame.

    The original DataFrame is not modified.
    """

    # Create a separate working copy
    df = raw.copy()

    # Remove exact duplicate rows
    df = df.drop_duplicates()

    # Standardize region and status names
    df["region"] = df["region"].str.strip().str.title()
    df["status"] = df["status"].str.strip().str.title()

    # Convert the three date formats
    date_format_1 = pd.to_datetime(df["order_date"], format="%Y-%m-%d", errors="coerce")
    date_format_2 = pd.to_datetime(df["order_date"], format="%d/%m/%Y", errors="coerce")
    date_format_3 = pd.to_datetime(
        df["order_date"], format="%b %d, %Y", errors="coerce"
    )

    df["order_date"] = date_format_1.fillna(date_format_2).fillna(date_format_3)

    # Clean unit prices
    df["unit_price"] = (
        df["unit_price"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    # Convert quantity to numeric and remove invalid rows
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

    invalid_quantity = (df["quantity"] <= 0) | (df["quantity"] > 1000)

    df["quantity"] = df["quantity"].mask(invalid_quantity)
    df = df.dropna(subset=["quantity"])
    df["quantity"] = df["quantity"].astype(int)

    # Fill missing customer and discount values
    df["customer"] = df["customer"].fillna("Unknown")
    df["discount"] = df["discount"].fillna(0.0)

    # Calculate revenue after discount
    df["revenue"] = (df["quantity"] * df["unit_price"] * (1 - df["discount"])).round(2)

    return df
