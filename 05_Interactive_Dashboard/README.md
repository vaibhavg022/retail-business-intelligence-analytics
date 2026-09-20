# Task 05 — Interactive Dashboard & KPI Visualizations

## Project: Retail Business Performance Dashboard

This task focuses on developing an interactive business intelligence dashboard using the Retail Orders dataset used throughout the previous analytics tasks.

The dashboard provides a visual overview of business performance through KPI cards, trend analysis, category and regional comparisons, temporal drill-downs, interactive filters, and product-level analysis.

## Objectives

* Build an interactive business dashboard using Streamlit and Plotly.
* Present important business KPIs in a clear executive-friendly format.
* Analyze revenue, profit, orders, customers, and average order value.
* Provide interactive filtering by date, region, category, and customer segment.
* Visualize revenue trends over time.
* Compare category and regional performance.
* Provide temporal drill-down from yearly to quarterly and monthly views.
* Analyze product and sub-category performance.
* Maintain a clear visual hierarchy for dashboard usability.

## Dashboard Features

### Executive KPI Cards

The dashboard includes:

* Revenue
* Customer Acquisition Cost (when acquisition-cost data is available)
* Churn Rate (when customer-retention data is available)
* Average Order Value

Additional supporting KPIs include:

* Total Orders
* Total Customers
* Total Profit
* Profit Margin

CAC and Churn Rate are not artificially estimated when the Retail Orders dataset does not contain the required acquisition or customer-retention information.

## Interactive Filters

Users can filter the dashboard using:

* Order Date
* Region
* Category
* Customer Segment

All applicable KPI cards and visualizations update according to the selected filters.

## Visualizations

The dashboard contains:

* Monthly Revenue Trend
* Revenue vs Profit Trend
* Revenue by Category
* Revenue by Region
* Geographic/Regional Performance View
* Top Sub-Categories
* Profit by Discount Level
* Temporal Drill-Down
* Top Products Table

## Technology Stack

* Python
* Streamlit
* Pandas
* NumPy
* Plotly

## Project Structure

```text
05_Interactive_Dashboard/
│
├── README.md
├── app.py
├── requirements.txt
├── Dashboard.pdf
│
├── data/
│   └── retail-orders-clean.csv
│
└── screenshots/
    ├── dashboard_overview.png
    ├── revenue_analysis.png
    └── regional_analysis.png
```

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the Streamlit application

```bash
streamlit run app.py
```

### 3. Open the dashboard

Streamlit will provide a local URL, normally:

```text
http://localhost:8501
```

## Expected Output

The completed dashboard should provide an interactive interface where users can:

1. Select a date range.
2. Filter business regions.
3. Filter product categories.
4. Filter customer segments.
5. Review updated KPI values.
6. Analyze revenue and profit trends.
7. Compare regional and category performance.
8. Perform temporal drill-down.
9. Review top-performing products and sub-categories.

## Data Note

The Retail Orders dataset primarily provides transactional information. Metrics such as Customer Acquisition Cost and Churn Rate require additional marketing and customer-lifecycle information.

Therefore, the application checks whether the required fields exist before calculating these KPIs. If the required information is unavailable, the dashboard displays `N/A` instead of generating an unsupported estimate.

## Expected Proof

The task submission can include:

* `app.py`
* `requirements.txt`
* `README.md`
* Dashboard PDF export
* Dashboard screenshots
* Streamlit deployment link, if deployed

## Conclusion

This dashboard converts the Retail Orders dataset into an interactive business analysis interface, allowing users to explore performance across time, products, categories, customer segments, and regions through dynamically updated visualizations.
