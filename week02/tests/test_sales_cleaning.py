import pandas as pd
from pandas.testing import assert_frame_equal

from sales_cleaning import clean_sales


def sample_data():
    """Create a small handmade sales dataset for testing."""
    return pd.DataFrame(
        {
            "order_id": [1, 1, 2, 3, 4, 5, 6],
            "order_date": [
                "2026-01-01",
                "2026-01-01",
                "02/01/2026",
                "Jan 03, 2026",
                "2026-01-04",
                "2026-01-05",
                "2026-01-06",
            ],
            "customer": ["Ali", "Ali", None, "Sara", "Ahmed", "Usman", "Ayesha"],
            "region": [" north ", " north ", "SOUTH", "east", "west", "North", "East"],
            "product": ["A", "A", "B", "C", "D", "E", "F"],
            "category": ["X", "X", "Y", "X", "Y", "X", "Y"],
            "quantity": [2, 2, 3, 4, 0, 5, 6],
            "unit_price": [
                "$10.00",
                "$10.00",
                "$20.00",
                "$5.00",
                "$8.00",
                "$2.00",
                "$3.00",
            ],
            "discount": [0.1, 0.1, None, 0.0, 0.0, 0.2, 0.0],
            "status": [
                " shipped ",
                " shipped ",
                "PENDING",
                "cancelled",
                "Shipped",
                "pending",
                "SHIPPED",
            ],
        }
    )


def test_duplicates_removed():
    result = clean_sales(sample_data())
    assert len(result) == 5


def test_region_and_status_standardized():
    result = clean_sales(sample_data())
    assert set(result["region"]) == {"North", "South", "East"}
    assert set(result["status"]) == {"Shipped", "Pending", "Cancelled"}


def test_three_date_formats_parsed():
    result = clean_sales(sample_data())
    assert result["order_date"].notna().all()
    assert pd.api.types.is_datetime64_any_dtype(result["order_date"])


def test_price_text_converted():
    result = clean_sales(sample_data())
    assert pd.api.types.is_float_dtype(result["unit_price"])
    assert result.loc[result["order_id"] == 1, "unit_price"].iloc[0] == 10.0


def test_invalid_quantity_rows_removed():
    result = clean_sales(sample_data())
    assert (result["quantity"] > 0).all()
    assert (result["quantity"] <= 1000).all()


def test_missing_customer_and_discount_filled():
    result = clean_sales(sample_data())
    assert result["customer"].isna().sum() == 0
    assert result["discount"].isna().sum() == 0
    assert "Unknown" in result["customer"].values
    assert 0.0 in result["discount"].values


def test_revenue_calculated_correctly():
    result = clean_sales(sample_data())
    # Hand calculation: 3 * 20 * (1 - 0) = 60
    assert result.loc[result["order_id"] == 2, "revenue"].iloc[0] == 60.0


def test_original_dataframe_not_modified():
    original = sample_data()
    original_copy = original.copy(deep=True)

    clean_sales(original)

    assert_frame_equal(original, original_copy)
