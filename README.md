# Retail Business Intelligence & Data Analytics

This repository contains my **Data Analytics & Business Intelligence Internship** project work at **RabTech Academy**.

## Current Task

Task 02 — KPI Dictionary & Data Quality Contract

Objective:
Translate business requirements into measurable KPIs and establish a structured data-quality framework.

Key Work
Defined 10 business KPIs with:
KPI name
Formula
Data grain
Filters
Business owner
Refresh cadence
Profiled the retail dataset for:
Completeness
Uniqueness
Validity
Consistency
Freshness
Implemented executable data-quality checks using Python and Pandas.
Identified issues such as missing values, duplicate records, invalid dates, invalid quantities, and invalid discount values.
Defined measurable quality thresholds and failure-handling procedures.
Created a KPI dictionary and Data Quality Contract.
Deliverables
02_KPI_Data_Quality/
├── README.md
├── KPI_Dictionary_and_DQ_Contract.xlsx
├── Retail_Data_Profile.ipynb
├── Data_Quality_Contract.md
└── data/
    ├── retail-orders-raw.csv
    └── retail-data-dictionary.csv
Task 03 — Data Ingestion, Cleaning & Preprocessing with Pandas

Objective:
Clean and standardize a large retail transaction dataset containing real-world data-quality issues and prepare it for further analysis.

Key Work
Loaded and inspected a 12,575-row retail sales dataset.
Performed initial data-quality profiling.
Identified and handled missing values.
Checked and removed duplicate records where applicable.
Standardized column names and text values.
Corrected inconsistent data types.
Converted transaction dates into datetime format.
Standardized discount-related values.
Imputed missing numerical values.
Recalculated missing transaction totals where appropriate.
Detected and handled numerical outliers using the IQR method.
Performed feature engineering.
Validated the cleaned dataset.
Exported the final analysis-ready dataset.
Feature Engineering

The following features were created:

year
month
month_name
average_transaction_value
discount_status

A profit margin was not calculated because the source dataset does not contain a separate cost/COGS field required for a valid profit calculation.

Final Dataset

The cleaned dataset contains:

12,575 records
15 columns
0 missing values
0 duplicate rows
Deliverables
03_Data_Ingestion_Cleaning/
├── README.md
├── Data_Cleaning_Preprocessing.ipynb
├── clean_dataset.csv
└── data/
    └── retail_store_sales.csv
Technologies Used
Python
Pandas
NumPy
Matplotlib
Jupyter Notebook
Microsoft Excel
Markdown
Repository Structure
RabTech-Data-Analytics-Internship/
│
├── 02_KPI_Data_Quality/
│   ├── README.md
│   ├── KPI_Dictionary_and_DQ_Contract.xlsx
│   ├── Retail_Data_Profile.ipynb
│   ├── Data_Quality_Contract.md
│   └── data/
│       ├── retail-orders-raw.csv
│       └── retail-data-dictionary.csv
│
├── 03_Data_Ingestion_Cleaning/
│   ├── README.md
│   ├── Data_Cleaning_Preprocessing.ipynb
│   ├── clean_dataset.csv
│   └── data/
│       └── retail_store_sales.csv
│
└── README.md
Key Skills Demonstrated

Through these tasks, I demonstrated practical experience in:

Data ingestion
Data profiling
Data cleaning
Data preprocessing
Data-quality validation
KPI definition
Business metric design
Missing-value handling
Duplicate detection
Data-type conversion
Outlier detection
Feature engineering
Pandas-based data analysis
Data documentation
Business-oriented data interpretation
Internship Progress
Task	Status
Task 01	⏳ Pending
Task 02 — KPI & Data Quality	✅ Completed
Task 03 — Data Cleaning & Preprocessing	✅ Completed
Task 04	⏳ Pending
Task 05	⏳ Pending
Task 06	⏳ Pending
About

This repository documents my practical learning and implementation work during the RabTech Academy Data Analytics & Business Intelligence Internship, with a focus on building reliable data workflows and preparing business data for analysis and decision-making.
