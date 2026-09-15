# Task 02 — KPI Dictionary & Data Quality Contract

## Objective
Translate a retail business requirement into measurable KPIs and a testable agreement about what trustworthy data means.

## Decision Owner
**Head of Commerce / Operations Manager**

## Dataset
Retail Orders dataset supplied by RabTech Academy.

Expected grain: **one row per unique `order_id`**

## Deliverables
- `KPI_Dictionary_and_DQ_Contract.xlsx` — KPI definitions, DQ rules, source dictionary and contract
- `Retail_Data_Profile.ipynb` — executable data-quality profiling notebook
- `Data_Quality_Contract.md` — human-readable quality agreement
- `data/retail-orders-raw.csv` — original raw dataset
- `data/retail-data-dictionary.csv` — supplied column definitions

## KPIs
10 KPIs are defined:
1. Gross Sales
2. Discount Amount
3. Net Sales
4. Orders
5. Units Sold
6. Average Order Value (AOV)
7. Paid Order Rate
8. Refund Rate
9. Average Discount %
10. Units per Order

## Data Quality Dimensions
- Completeness
- Uniqueness
- Validity
- Consistency
- Freshness

## How to Run
1. Open `Retail_Data_Profile.ipynb` in Jupyter Notebook or Google Colab.
2. Keep the `data` folder beside the notebook.
3. Run all cells.
4. Review the quality-check results and final contract decision.

## Contract Decision
Critical data-quality failures block KPI publication until the affected records are corrected or quarantined and the profile passes again.
