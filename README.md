# Retail Business Intelligence & Data Analytics

This repository contains my **Data Analytics & Business Intelligence Internship** project work at **RabTech Academy**.

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

# Expected Outcomes

The completed tasks provide a structured approach for moving from raw retail data to business-oriented analytical insights.

The project establishes data-quality expectations first, prepares the dataset for analysis, and then applies statistical and visual techniques to identify meaningful patterns.

---

# Conclusion

Tasks 02, 03, and 04 collectively demonstrate an end-to-end approach to retail data analysis.

The workflow begins with defining measurable business metrics and data-quality requirements, continues through data cleaning and preparation, and concludes with exploratory and statistical analysis.

The resulting notebooks, documentation, and supporting files provide reproducible evidence of the analytical process and its findings.

---

## Author

**Vaibhav Gupta**

B.Tech — Computer Science & Engineering

### Areas of Interest

* Data Analytics
* Artificial Intelligence
* Machine Learning
* Python
* Data Science

---

## Repository Status

| Task                                | Status    |
| ----------------------------------- | --------- |
| Task 02 — KPI & Data Quality        | Completed |
| Task 03 — Data Cleaning             | Completed |
| Task 04 — Exploratory Data Analysis | Completed |

**Project Status: Completed**
