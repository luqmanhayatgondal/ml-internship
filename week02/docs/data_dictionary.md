# Sales Dataset Data Dictionary

This document describes the 11 columns in the cleaned sales dataset.

| Column | Type | Meaning | Allowed values or range | Cleaning rule |
|---|---|---|---|---|
| order_id | Integer | Unique identifier for each order | Unique order IDs | Exact duplicate rows removed |
| order_date | Datetime | Date when the order was placed | Valid calendar dates | Three date formats converted into datetime |
| customer | String | Name of the customer | Customer name or Unknown | Missing values replaced with Unknown |
| region | String | Sales region | East, North, South, West | Spaces removed and capitalization standardized |
| product | String | Product name | Existing product names | Original values retained |
| category | String | Product category | Existing category names | Original values retained |
| quantity | Integer | Number of units sold | 1 to 1000 | Invalid and missing quantities removed |
| unit_price | Float | Price per unit | Numeric price | Dollar signs and commas removed |
| discount | Float | Discount applied to the order | Numeric discount fraction | Missing values replaced with 0.0 |
| status | String | Current order status | Cancelled, Pending, Shipped | Spaces removed and capitalization standardized |
| revenue | Float | Revenue after discount | Numeric amount rounded to 2 decimal places | Calculated using quantity × unit_price × (1 - discount) |

## Revenue Calculation

Revenue is calculated using this formula:

`revenue = quantity * unit_price * (1 - discount)`

The calculated revenue is rounded to two decimal places.