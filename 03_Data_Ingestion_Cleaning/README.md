# Task 03 — Data Ingestion, Cleaning & Preprocessing with Pandas

## Overview

This project focuses on ingesting, cleaning, standardizing, and preprocessing a retail sales dataset using Python and Pandas.

The raw dataset contains more than 10,000 transaction records with missing values, inconsistent data types, and data-quality issues. The objective is to transform the raw data into a clean and analysis-ready dataset through a structured data-cleaning workflow.

## Dataset

**Dataset:** Retail Store Sales Dataset

* Records: 12,575
* Original columns: 11
* Domain: Retail / Sales Transactions
* Format: CSV

The raw dataset is stored in:

```text
data/retail_store_sales.csv
```

## Objectives

* Load the raw retail dataset using Pandas.
* Inspect the structure and quality of the dataset.
* Identify missing values and duplicate records.
* Correct inconsistent data types.
* Standardize text and categorical values.
* Handle missing and invalid numerical values.
* Detect and handle numerical outliers.
* Convert transaction dates into a standardized datetime format.
* Perform feature engineering for analysis.
* Validate the cleaned dataset.
* Export the final cleaned dataset as a CSV file.

## Data Cleaning Process

The following preprocessing steps were performed:

1. Loaded the raw CSV dataset into Pandas.
2. Inspected rows, columns, data types, and statistical information.
3. Identified missing values across the dataset.
4. Checked for duplicate transaction records.
5. Standardized column names and text formatting.
6. Converted price, quantity, and total-spent fields to numeric types.
7. Converted transaction dates to datetime format.
8. Standardized the `Discount Applied` field.
9. Handled missing categorical values using an `Unknown` category where appropriate.
10. Imputed missing numerical values using category-based and median-based approaches.
11. Recalculated missing `Total Spent` values using price and quantity.
12. Detected extreme numerical values using the IQR method.
13. Capped extreme price and quantity values to reduce the impact of outliers.
14. Performed final data-quality validation.

## Feature Engineering

Additional analytical features were created from the cleaned dataset:

* `year` — transaction year
* `month` — transaction month
* `month_name` — transaction month name
* `average_transaction_value` — total spent divided by quantity
* `discount_status` — descriptive discount indicator

A profit margin was not calculated because the original dataset does not contain a separate cost or cost-of-goods-sold field.

## Before vs After

The cleaning process includes a comparison of the dataset before and after preprocessing, covering:

* Dataset dimensions
* Missing values
* Duplicate records
* Data types
* Numerical data quality

The final dataset contains:

* **12,575 records**
* **15 standardized columns**
* **0 missing values**
* **0 duplicate rows**

## Project Structure

```text
03_Data_Ingestion_Cleaning/
│
├── README.md
├── Data_Cleaning_Preprocessing.ipynb
├── clean_dataset.csv
│
└── data/
    └── retail_store_sales.csv
```

## Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook

## Output

The final cleaned and standardized dataset is available as:

```text
clean_dataset.csv
```

This file is ready for further exploratory data analysis, visualization, reporting, and business intelligence workflows.
