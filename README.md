# Retail Business Intelligence & Data Analytics

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live_Dashboard-FF4B4B?style=for-the-badge&logo=streamlit)](https://retail-business-intelligence-analytics-urhxcw74qyyvudplfiqgn5.streamlit.app/)

This repository contains my **Data Analytics & Business Intelligence Internship** project work at **RabTech Academy**.

👉 **Live Interactive Dashboard:** [Retail Business Intelligence & Analytics Dashboard](https://retail-business-intelligence-analytics-urhxcw74qyyvudplfiqgn5.streamlit.app/)

---

# Tasks Completed

## Task 02 — KPI Dictionary & Data Quality Contract

### Objective

The objective of Task 02 was to translate business requirements into measurable KPIs and define a testable framework for determining whether the retail data can be considered trustworthy.

### Work Performed

* Defined 10 business-oriented KPIs.
* Documented KPI formulas and calculation logic.
* Specified the appropriate data grain for each KPI.
* Added applicable filters and business conditions.
* Identified KPI ownership and refresh frequency.
* Profiled the dataset for completeness, uniqueness, validity, consistency, and freshness.
* Implemented executable data-quality checks using Python and Pandas.
* Checked for duplicate records and missing values.
* Validated dates, quantities, and discount values.
* Defined measurable quality thresholds.
* Documented failure handling and escalation procedures.

### Deliverables

```text
02_KPI_Data_Quality/
├── README.md
├── KPI_Dictionary_and_DQ_Contract.xlsx
├── Retail_Data_Profile.ipynb
├── Data_Quality_Contract.md
└── data/
    ├── retail-orders-raw.csv
    └── retail-data-dictionary.csv
```

---

# Task 03 — Data Cleaning & Preprocessing

### Objective

The objective of Task 03 was to prepare the retail dataset for reliable downstream analysis by identifying data inconsistencies, correcting invalid or incomplete values, and creating a cleaner analytical dataset.

### Work Performed

* Loaded and inspected the raw retail dataset.
* Reviewed data types and column structures.
* Identified missing and inconsistent values.
* Checked duplicate records.
* Standardized relevant date fields.
* Validated numerical columns such as Sales, Quantity, Discount, and Profit.
* Examined invalid or unexpected values.
* Applied appropriate data-cleaning transformations.
* Prepared the cleaned dataset for further analytical use.
* Documented the cleaning process and important observations.

### Deliverables

```text
03_Data_Cleaning/
├── README.md
├── Retail_Data_Cleaning.ipynb
├── cleaned_retail_data.csv
└── data/
    └── retail-orders-raw.csv
```

---

# Task 04 — Exploratory Data Analysis & Statistical Insights

### Objective

The objective of Task 04 was to perform comprehensive Exploratory Data Analysis on the retail dataset and identify important statistical and business patterns.

### Work Performed

* Calculated descriptive statistics including:

  * Mean
  * Median
  * Standard deviation
  * Minimum and maximum
  * Quartiles
* Analyzed distributions of Sales, Profit, Discount, and Quantity.
* Created histograms to understand variable distributions.
* Used box plots to identify potential outliers.
* Generated a correlation matrix and heatmap.
* Performed multivariate analysis using scatter plots.
* Compared sales and profitability across categories and regions.
* Formulated three business hypotheses.
* Applied Pearson correlation tests for numerical relationships.
* Applied one-way ANOVA for category-level profit comparison.
* Added Markdown commentary explaining statistical results.
* Summarized five major business-oriented findings.

### Hypotheses Tested

1. **Discount vs Profit**
   Examined whether discount levels are statistically associated with profit.

2. **Quantity vs Sales**
   Examined whether order quantity is statistically associated with sales.

3. **Category vs Profit**
   Examined whether average profit differs significantly across product categories.

### Deliverables

```text
04_Exploratory_Data_Analysis/
├── README.md
├── Retail_EDA_Statistical_Insights.ipynb
└── data/
    └── retail-orders-raw.csv
```

---

# Technology & Tools

The project uses the following technologies and tools:

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **SciPy**
* **Jupyter Notebook**
* **Microsoft Excel**
* **Markdown**
* **Git & GitHub**

---

# Analytics Workflow

The overall project follows a structured analytics workflow:

```text
Raw Retail Dataset
        │
        ▼
KPI Definition
        │
        ▼
Data Quality Profiling
        │
        ▼
Data Quality Contract
        │
        ▼
Data Cleaning & Preprocessing
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Statistical Analysis
        │
        ▼
Hypothesis Testing
        │
        ▼
Business Insights
```

---

# Repository Structure

```text
Retail-Data-Analytics/
│
├── README.md
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
├── 03_Data_Cleaning/
│   ├── README.md
│   ├── Retail_Data_Cleaning.ipynb
│   ├── cleaned_retail_data.csv
│   └── data/
│       └── retail-orders-raw.csv
│
└── 04_Exploratory_Data_Analysis/
    ├── README.md
    ├── Retail_EDA_Statistical_Insights.ipynb
    └── data/
        └── retail-orders-raw.csv
```

---

# Key Skills Demonstrated

This project demonstrates practical experience in:

* Data profiling
* Data quality assessment
* KPI development
* Data cleaning
* Data preprocessing
* Statistical analysis
* Exploratory Data Analysis
* Data visualization
* Correlation analysis
* Hypothesis testing
* Business interpretation
* Python-based analytics
* Pandas data manipulation
* Jupyter Notebook development
* Documentation and reporting

---
# Task 05 — Interactive Dashboard & KPI Visualizations

## Objective

Develop an interactive business dashboard using the cleaned retail transaction dataset to visualize key KPIs, trends, category performance and customer insights.

## Technologies Used

- Python
- Pandas
- Streamlit
- Plotly

## Dashboard Features

- Revenue KPI
- Total Transactions
- Total Customers
- Average Order Value (AOV)
- Total Quantity
- Date, Category, Payment Method and Discount filters
- Monthly Revenue Trend
- Category-wise Revenue Analysis
- Payment Method Analysis
- Discount Analysis
- Category × Monthly Revenue Heatmap
- Top 10 Items by Revenue
- Yearly Performance
- Customer Analysis
- Interactive Dataset Preview

## Dataset

The dashboard uses the cleaned dataset containing transaction, customer, category, item, pricing, quantity, payment, date and discount-related fields.

## KPI Calculation

- **Revenue:** Sum of `total_spent`
- **Transactions:** Unique `transaction_id`
- **Customers:** Unique `customer_id`
- **AOV:** Revenue ÷ Unique Transactions

## Dataset Limitations

The dataset does not contain dedicated fields for Customer Acquisition Cost (CAC), Churn Rate or geographic location. Therefore, these metrics were not artificially calculated.

## Run Locally

bash
pip install -r requirements.txt
streamlit run app.py


# Task 06 — Executive Decision Report & Capstone Presentation
## Objective
Synthesize Tasks 02–05 into an executive-ready Business Intelligence report for management decision-making.

## Deliverables
- `Executive_Decision_Report.pdf`
- `Final_Analytical_Notebook.ipynb`
- `ROI_Projection.xlsx`

---

## Executive KPIs
- **Revenue:** ₹16,36,956
- **Transactions:** 12,575
- **Customers:** 25
- **Average Order Value:** ₹130.18
- **Units Sold:** 69,828
- **Discount-applied transactions:** 33.6%

---

## Key Findings
- **Butchers** is the highest-revenue category.
- **2024** is the strongest full year in the supplied dataset.
- **Cash** is the largest payment channel by revenue.
- **Discount usage** is material and should be monitored through controlled experiments.
- The dataset does not contain profit, CAC, churn, or geographic fields, so these metrics are not fabricated.

---

## Strategic Recommendations
1. **Optimize category-level discounting.**
2. **Focus inventory and promotion** on strong revenue segments.
3. **Institutionalize recurring BI dashboard** and data-quality monitoring.

**Technology & ToolsLanguages & Core Libraries:**
Python, Pandas, NumPy, SciPyVisualization & Dashboards: Streamlit, Plotly, Matplotlib, SeabornTools & Platforms: Jupyter Notebook, Microsoft Excel, Git & GitHub, Streamlit Community CloudAnalytics 

**WorkflowPlaintext**

Raw Retail Dataset
       │
       ▼
KPI Definition & Data Profiling
       │
       ▼
Data Quality Contract & Validation
       │
       ▼
Data Cleaning & Preprocessing
       │
       ▼
Exploratory Data Analysis (EDA)
       │
       ▼
Statistical Analysis & Hypothesis Testing
       │
       ▼
Interactive Dashboard (Streamlit)
       │
       ▼
Executive Decision Report & ROI Projections
Repository StructurePlaintextRetail-Data-Analytics/
│
├── README.md
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
├── 03_Data_Cleaning/
│   ├── README.md
│   ├── Retail_Data_Cleaning.ipynb
│   ├── cleaned_retail_data.csv
│   └── data/
│       └── retail-orders-raw.csv
│
├── 04_Exploratory_Data_Analysis/
│   ├── README.md
│   ├── Retail_EDA_Statistical_Insights.ipynb
│   └── data/
│       └── retail-orders-raw.csv
│
├── 05_Interactive_Dashboard/
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   └── cleaned_retail_data.csv
│
└── 06_Executive_Decision_Report/
    ├── Executive_Decision_Report.pdf
    ├── Final_Analytical_Notebook.ipynb
    └── ROI_Projection.xlsx

# Key Skills Demonstrated

This project demonstrates practical experience in:

* Data profiling & data quality management
* KPI dictionary development & data contract design
* Data cleaning & preprocessing
* Exploratory Data Analysis (EDA) & data visualization
* Statistical analysis, correlation, & hypothesis testing
* Interactive dashboard development (Streamlit & Plotly)
* Executive reporting & management decision-making
* Business interpretation & strategic recommendations
* Python-based analytics & Pandas data manipulation
* Jupyter Notebook development & Git documentation

---

# Repository Status

| Task | Status |
| :--- | :--- |
| **Task 02 — KPI & Data Quality** | Completed |
| **Task 03 — Data Cleaning & Preprocessing** | Completed |
| **Task 04 — Exploratory Data Analysis** | Completed |
| **Task 05 — Interactive Dashboard** | Completed |
| **Task 06 — Executive Decision Report** | Completed |

**Project Status:** Completed 🎉

---

# Author

**Vaibhav Gupta**  
*B.Tech — Computer Science & Engineering*  

**Areas of Interest:**  
Data Analytics | Artificial Intelligence | Machine Learning | Python | Data Science
