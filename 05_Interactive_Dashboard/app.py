import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Retail Business Performance Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>
        .main {
            padding-top: 1rem;
        }

        .dashboard-title {
            font-size: 2.2rem;
            font-weight: 700;
            margin-bottom: 0.2rem;
        }

        .dashboard-subtitle {
            color: #666;
            font-size: 1rem;
            margin-bottom: 1.5rem;
        }

        .kpi-card {
            padding: 1rem;
            border-radius: 12px;
            border: 1px solid #e5e7eb;
            background-color: #ffffff;
            min-height: 120px;
        }

        .kpi-title {
            font-size: 0.9rem;
            color: #6b7280;
            margin-bottom: 0.5rem;
        }

        .kpi-value {
            font-size: 1.8rem;
            font-weight: 700;
        }

        .kpi-note {
            font-size: 0.75rem;
            color: #6b7280;
            margin-top: 0.35rem;
        }

        .section-title {
            font-size: 1.25rem;
            font-weight: 650;
            margin-top: 1rem;
            margin-bottom: 0.5rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# DATA LOCATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_CANDIDATES = [
    BASE_DIR / "data" / "retail-orders-clean.csv",
    BASE_DIR / "data" / "retail-orders-raw.csv",
    BASE_DIR / "data" / "retail_orders.csv",
    BASE_DIR / "retail-orders-clean.csv",
    BASE_DIR / "retail-orders-raw.csv",
]


# ============================================================
# COLUMN NORMALIZATION
# ============================================================

def normalize_column_name(column):
    """
    Converts column names into a consistent snake_case format.
    """
    column = str(column).strip().lower()

    replacements = {
        " ": "_",
        "-": "_",
        "/": "_",
        ".": "_",
        "(": "",
        ")": "",
        "%": "percent"
    }

    for old, new in replacements.items():
        column = column.replace(old, new)

    while "__" in column:
        column = column.replace("__", "_")

    return column.strip("_")


def normalize_columns(df):
    """
    Normalize all dataframe column names.
    """
    df = df.copy()
    df.columns = [normalize_column_name(col) for col in df.columns]
    return df


# ============================================================
# COLUMN ALIASES
# ============================================================

ALIASES = {
    "order_id": [
        "order_id",
        "orderid"
    ],
    "order_date": [
        "order_date",
        "orderdate"
    ],
    "ship_date": [
        "ship_date",
        "shipdate"
    ],
    "ship_mode": [
        "ship_mode",
        "shipmode"
    ],
    "customer_id": [
        "customer_id",
        "customerid"
    ],
    "customer_name": [
        "customer_name",
        "customername"
    ],
    "segment": [
        "segment"
    ],
    "country": [
        "country"
    ],
    "city": [
        "city"
    ],
    "state": [
        "state"
    ],
    "postal_code": [
        "postal_code",
        "postalcode",
        "zip_code",
        "zipcode"
    ],
    "region": [
        "region"
    ],
    "product_id": [
        "product_id",
        "productid"
    ],
    "category": [
        "category"
    ],
    "sub_category": [
        "sub_category",
        "subcategory"
    ],
    "product_name": [
        "product_name",
        "productname"
    ],
    "sales": [
        "sales",
        "revenue"
    ],
    "quantity": [
        "quantity",
        "qty"
    ],
    "discount": [
        "discount",
        "discount_rate"
    ],
    "profit": [
        "profit"
    ],
    "shipping_cost": [
        "shipping_cost",
        "shippingcost"
    ],
    "order_priority": [
        "order_priority",
        "priority"
    ]
}


def find_column(df, logical_name):
    """
    Find the actual dataframe column corresponding to a logical field.
    """
    for candidate in ALIASES.get(logical_name, []):
        if candidate in df.columns:
            return candidate

    return None


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    selected_file = None

    for candidate in DATA_CANDIDATES:
        if candidate.exists():
            selected_file = candidate
            break

    if selected_file is None:
        raise FileNotFoundError(
            "Retail Orders CSV file was not found. "
            "Place the dataset inside the 'data' folder."
        )

    df = pd.read_csv(selected_file)
    df = normalize_columns(df)

    return df, selected_file.name


# ============================================================
# PREPARE DATA
# ============================================================

def prepare_data(df):

    df = df.copy()

    # Convert dates
    order_date_col = find_column(df, "order_date")

    if order_date_col:
        df[order_date_col] = pd.to_datetime(
            df[order_date_col],
            errors="coerce"
        )

    # Convert numeric fields
    for logical_name in [
        "sales",
        "profit",
        "quantity",
        "discount",
        "shipping_cost"
    ]:
        col = find_column(df, logical_name)

        if col:
            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    return df


# ============================================================
# FORMATTING FUNCTIONS
# ============================================================

def format_currency(value):
    if pd.isna(value):
        return "N/A"

    if abs(value) >= 1_000_000:
        return f"${value / 1_000_000:.2f}M"

    if abs(value) >= 1_000:
        return f"${value / 1_000:.2f}K"

    return f"${value:,.2f}"


def format_number(value):
    if pd.isna(value):
        return "N/A"

    return f"{value:,.0f}"


def format_percent(value):
    if pd.isna(value):
        return "N/A"

    return f"{value:.2f}%"


# ============================================================
# DATA AVAILABILITY CHECK
# ============================================================

def has_field(df, logical_name):
    return find_column(df, logical_name) is not None


# ============================================================
# MAIN APPLICATION
# ============================================================

try:
    df, file_name = load_data()
    df = prepare_data(df)

except Exception as error:
    st.error("Unable to load the Retail Orders dataset.")
    st.code(str(error))
    st.info(
        "Place your CSV file inside "
        "'05_Interactive_Dashboard/data/' "
        "and restart the Streamlit application."
    )
    st.stop()


# ============================================================
# REQUIRED FIELDS
# ============================================================

sales_col = find_column(df, "sales")
profit_col = find_column(df, "profit")
quantity_col = find_column(df, "quantity")
order_date_col = find_column(df, "order_date")
order_id_col = find_column(df, "order_id")
customer_id_col = find_column(df, "customer_id")
category_col = find_column(df, "category")
region_col = find_column(df, "region")
segment_col = find_column(df, "segment")
sub_category_col = find_column(df, "sub_category")


if sales_col is None:
    st.error(
        "The dataset does not contain a Sales/Revenue column."
    )
    st.stop()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🎛️ Dashboard Filters")

st.sidebar.caption(f"Dataset: `{file_name}`")
st.sidebar.caption(f"Records: {len(df):,}")


# ------------------------------------------------------------
# DATE FILTER
# ------------------------------------------------------------

filtered_df = df.copy()

if order_date_col and filtered_df[order_date_col].notna().any():

    min_date = filtered_df[order_date_col].min().date()
    max_date = filtered_df[order_date_col].max().date()

    date_range = st.sidebar.date_input(
        "Order Date",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    if isinstance(date_range, tuple) and len(date_range) == 2:

        start_date, end_date = date_range

        filtered_df = filtered_df[
            (filtered_df[order_date_col].dt.date >= start_date)
            &
            (filtered_df[order_date_col].dt.date <= end_date)
        ]


# ------------------------------------------------------------
# REGION FILTER
# ------------------------------------------------------------

if region_col:

    region_values = sorted(
        filtered_df[region_col]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_regions = st.sidebar.multiselect(
        "Region",
        region_values,
        default=region_values
    )

    if selected_regions:
        filtered_df = filtered_df[
            filtered_df[region_col].astype(str).isin(
                selected_regions
            )
        ]


# ------------------------------------------------------------
# CATEGORY FILTER
# ------------------------------------------------------------

if category_col:

    category_values = sorted(
        filtered_df[category_col]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_categories = st.sidebar.multiselect(
        "Category",
        category_values,
        default=category_values
    )

    if selected_categories:
        filtered_df = filtered_df[
            filtered_df[category_col].astype(str).isin(
                selected_categories
            )
        ]


# ------------------------------------------------------------
# SEGMENT FILTER
# ------------------------------------------------------------

if segment_col:

    segment_values = sorted(
        filtered_df[segment_col]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_segments = st.sidebar.multiselect(
        "Customer Segment",
        segment_values,
        default=segment_values
    )

    if selected_segments:
        filtered_df = filtered_df[
            filtered_df[segment_col].astype(str).isin(
                selected_segments
            )
        ]


# ------------------------------------------------------------
# RESET NOTE
# ------------------------------------------------------------

st.sidebar.markdown("---")
st.sidebar.caption(
    "Use the filters to dynamically update the KPI cards "
    "and visualizations."
)


# ============================================================
# DASHBOARD HEADER
# ============================================================

st.markdown(
    '<div class="dashboard-title">'
    '📊 Retail Business Performance Dashboard'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-subtitle">'
    'Interactive analysis of sales, profit, customers, products, '
    'categories, and regional performance.'
    '</div>',
    unsafe_allow_html=True
)


if filtered_df.empty:
    st.warning(
        "No records match the selected filters. "
        "Please change the filter selection."
    )
    st.stop()


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_revenue = filtered_df[sales_col].sum()

total_profit = (
    filtered_df[profit_col].sum()
    if profit_col
    else np.nan
)

total_quantity = (
    filtered_df[quantity_col].sum()
    if quantity_col
    else np.nan
)


# Number of orders
if order_id_col:
    total_orders = filtered_df[order_id_col].nunique()
else:
    total_orders = len(filtered_df)


# Number of customers
if customer_id_col:
    total_customers = filtered_df[customer_id_col].nunique()
else:
    total_customers = np.nan


# Average Order Value
if total_orders > 0:
    average_order_value = total_revenue / total_orders
else:
    average_order_value = np.nan


# Profit Margin
if total_revenue != 0 and not pd.isna(total_profit):
    profit_margin = (
        total_profit / total_revenue
    ) * 100
else:
    profit_margin = np.nan


# CAC cannot be calculated without acquisition-cost data
cac_available = (
    "marketing_cost" in filtered_df.columns
    or "acquisition_cost" in filtered_df.columns
    or "customer_acquisition_cost" in filtered_df.columns
)

# Churn cannot be calculated without customer retention history
churn_available = (
    "churn_flag" in filtered_df.columns
    or "churned" in filtered_df.columns
    or "customer_status" in filtered_df.columns
)


# ============================================================
# KPI CARDS
# ============================================================

st.markdown(
    '<div class="section-title">Executive KPIs</div>',
    unsafe_allow_html=True
)

kpi1, kpi2, kpi3, kpi4 = st.columns(4)


with kpi1:

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">💰 Revenue</div>
            <div class="kpi-value">{format_currency(total_revenue)}</div>
            <div class="kpi-note">Total filtered sales</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with kpi2:

    if cac_available:

        acquisition_cost_col = (
            "marketing_cost"
            if "marketing_cost" in filtered_df.columns
            else "acquisition_cost"
        )

        acquisition_cost = pd.to_numeric(
            filtered_df[acquisition_cost_col],
            errors="coerce"
        ).sum()

        if total_customers and total_customers > 0:
            cac_value = acquisition_cost / total_customers
            cac_display = format_currency(cac_value)
        else:
            cac_display = "N/A"

        cac_note = "Calculated from acquisition cost data"

    else:

        cac_display = "N/A"
        cac_note = "Acquisition cost data unavailable"

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">🎯 Customer Acquisition Cost</div>
            <div class="kpi-value">{cac_display}</div>
            <div class="kpi-note">{cac_note}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with kpi3:

    if churn_available:

        if "churn_flag" in filtered_df.columns:
            churn_col = "churn_flag"
        elif "churned" in filtered_df.columns:
            churn_col = "churned"
        else:
            churn_col = "customer_status"

        if churn_col == "customer_status":

            churn_rate = (
                filtered_df[churn_col]
                .astype(str)
                .str.lower()
                .eq("churned")
                .mean()
                * 100
            )

        else:

            churn_rate = pd.to_numeric(
                filtered_df[churn_col],
                errors="coerce"
            ).mean() * 100

        churn_display = format_percent(churn_rate)
        churn_note = "Calculated from customer status data"

    else:

        churn_display = "N/A"
        churn_note = "Customer retention history unavailable"

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">🔄 Churn Rate</div>
            <div class="kpi-value">{churn_display}</div>
            <div class="kpi-note">{churn_note}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with kpi4:

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">🛒 Average Order Value</div>
            <div class="kpi-value">{format_currency(average_order_value)}</div>
            <div class="kpi-note">Revenue per unique order</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# SECONDARY KPIs
# ============================================================

st.markdown(
    '<div class="section-title">Supporting KPIs</div>',
    unsafe_allow_html=True
)

s1, s2, s3, s4 = st.columns(4)


with s1:
    st.metric(
        "Total Orders",
        format_number(total_orders)
    )


with s2:
    st.metric(
        "Customers",
        format_number(total_customers)
    )


with s3:
    st.metric(
        "Total Profit",
        format_currency(total_profit)
    )


with s4:
    st.metric(
        "Profit Margin",
        format_percent(profit_margin)
    )


# ============================================================
# REVENUE TREND
# ============================================================

if order_date_col:

    st.markdown(
        '<div class="section-title">Revenue Trend</div>',
        unsafe_allow_html=True
    )

    trend_df = filtered_df.dropna(
        subset=[order_date_col]
    ).copy()

    trend_df["year"] = (
        trend_df[order_date_col].dt.year
    )

    trend_df["month"] = (
        trend_df[order_date_col].dt.to_period("M")
        .astype(str)
    )

    monthly_revenue = (
        trend_df.groupby("month", as_index=False)[sales_col]
        .sum()
    )

    monthly_revenue.columns = [
        "Month",
        "Revenue"
    ]

    fig_revenue = px.area(
        monthly_revenue,
        x="Month",
        y="Revenue",
        title="Monthly Revenue Trend",
        markers=True
    )

    fig_revenue.update_layout(
        xaxis_title="Month",
        yaxis_title="Revenue",
        hovermode="x unified"
    )

    st.plotly_chart(
        fig_revenue,
        use_container_width=True
    )


# ============================================================
# SALES AND PROFIT TREND
# ============================================================

if order_date_col and profit_col:

    trend_profit = filtered_df.dropna(
        subset=[order_date_col]
    ).copy()

    trend_profit["month"] = (
        trend_profit[order_date_col]
        .dt.to_period("M")
        .astype(str)
    )

    monthly_profit = (
        trend_profit
        .groupby("month", as_index=False)
        .agg(
            Revenue=(sales_col, "sum"),
            Profit=(profit_col, "sum")
        )
    )

    monthly_profit_long = monthly_profit.melt(
        id_vars="month",
        value_vars=["Revenue", "Profit"],
        var_name="Metric",
        value_name="Amount"
    )

    fig_profit = px.line(
        monthly_profit_long,
        x="month",
        y="Amount",
        color="Metric",
        markers=True,
        title="Revenue vs Profit Trend"
    )

    fig_profit.update_layout(
        xaxis_title="Month",
        yaxis_title="Amount",
        hovermode="x unified"
    )

    st.plotly_chart(
        fig_profit,
        use_container_width=True
    )


# ============================================================
# CATEGORY AND REGION ANALYSIS
# ============================================================

col_left, col_right = st.columns(2)


# ------------------------------------------------------------
# CATEGORY
# ------------------------------------------------------------

with col_left:

    if category_col:

        category_data = (
            filtered_df
            .groupby(category_col, as_index=False)
            .agg(
                Revenue=(sales_col, "sum")
            )
            .sort_values(
                "Revenue",
                ascending=False
            )
        )

        fig_category = px.bar(
            category_data,
            x=category_col,
            y="Revenue",
            title="Revenue by Category",
            text_auto=".2s"
        )

        fig_category.update_layout(
            xaxis_title="Category",
            yaxis_title="Revenue"
        )

        st.plotly_chart(
            fig_category,
            use_container_width=True
        )


# ------------------------------------------------------------
# REGION
# ------------------------------------------------------------

with col_right:

    if region_col:

        region_data = (
            filtered_df
            .groupby(region_col, as_index=False)
            .agg(
                Revenue=(sales_col, "sum"),
                Profit=(
                    profit_col,
                    "sum"
                ) if profit_col else (
                    sales_col,
                    "sum"
                )
            )
        )

        fig_region = px.bar(
            region_data,
            x=region_col,
            y="Revenue",
            title="Revenue by Region",
            text_auto=".2s"
        )

        fig_region.update_layout(
            xaxis_title="Region",
            yaxis_title="Revenue"
        )

        st.plotly_chart(
            fig_region,
            use_container_width=True
        )


# ============================================================
# GEOGRAPHIC ANALYSIS
# ============================================================

if region_col:

    st.markdown(
        '<div class="section-title">Geographic Performance</div>',
        unsafe_allow_html=True
    )

    geographic_data = (
        filtered_df
        .groupby(region_col, as_index=False)
        .agg(
            Revenue=(sales_col, "sum"),
            Orders=(
                order_id_col,
                "nunique"
            ) if order_id_col else (
                sales_col,
                "count"
            )
        )
    )

    fig_geo = px.choropleth(
        geographic_data,
        locations=region_col,
        locationmode="USA-states",
        color="Revenue",
        scope="usa",
        title="Regional Revenue Heatmap"
    )

    st.plotly_chart(
        fig_geo,
        use_container_width=True
    )

    st.caption(
        "The geographic visualization is enabled when the dataset "
        "contains compatible geographic fields. For datasets using "
        "business regions rather than state codes, the regional bar "
        "chart above should be used as the primary geographic view."
    )


# ============================================================
# SUB-CATEGORY ANALYSIS
# ============================================================

if sub_category_col:

    subcategory_data = (
        filtered_df
        .groupby(sub_category_col, as_index=False)
        .agg(
            Revenue=(sales_col, "sum"),
            Profit=(
                profit_col,
                "sum"
            ) if profit_col else (
                sales_col,
                "sum"
            )
        )
        .sort_values(
            "Revenue",
            ascending=False
        )
        .head(15)
    )

    fig_subcategory = px.bar(
        subcategory_data,
        x="Revenue",
        y=sub_category_col,
        orientation="h",
        title="Top 15 Sub-Categories by Revenue",
        text_auto=".2s"
    )

    fig_subcategory.update_layout(
        yaxis={
            "categoryorder": "total ascending"
        }
    )

    st.plotly_chart(
        fig_subcategory,
        use_container_width=True
    )


# ============================================================
# DISCOUNT VS PROFIT
# ============================================================

discount_col = find_column(df, "discount")

if discount_col and profit_col:

    discount_profit = (
        filtered_df
        .groupby(discount_col, as_index=False)
        .agg(
            Profit=(profit_col, "sum"),
            Revenue=(sales_col, "sum")
        )
        .sort_values(discount_col)
    )

    fig_discount = px.bar(
        discount_profit,
        x=discount_col,
        y="Profit",
        title="Profit by Discount Level"
    )

    fig_discount.update_layout(
        xaxis_title="Discount",
        yaxis_title="Profit"
    )

    st.plotly_chart(
        fig_discount,
        use_container_width=True
    )


# ============================================================
# TEMPORAL DRILL-DOWN
# ============================================================

if order_date_col:

    st.markdown(
        '<div class="section-title">Temporal Drill-Down</div>',
        unsafe_allow_html=True
    )

    drill_level = st.selectbox(
        "Select Time Level",
        [
            "Year",
            "Quarter",
            "Month"
        ]
    )

    drill_df = filtered_df.dropna(
        subset=[order_date_col]
    ).copy()

    if drill_level == "Year":

        drill_df["Period"] = (
            drill_df[order_date_col]
            .dt.year
            .astype(str)
        )

    elif drill_level == "Quarter":

        drill_df["Period"] = (
            drill_df[order_date_col]
            .dt.to_period("Q")
            .astype(str)
        )

    else:

        drill_df["Period"] = (
            drill_df[order_date_col]
            .dt.to_period("M")
            .astype(str)
        )

    drill_summary = (
        drill_df
        .groupby("Period", as_index=False)
        .agg(
            Revenue=(sales_col, "sum")
        )
    )

    fig_drill = px.bar(
        drill_summary,
        x="Period",
        y="Revenue",
        title=f"Revenue Drill-Down by {drill_level}"
    )

    st.plotly_chart(
        fig_drill,
        use_container_width=True
    )


# ============================================================
# TOP PRODUCTS
# ============================================================

if product_name_col := find_column(df, "product_name"):

    top_products = (
        filtered_df
        .groupby(product_name_col, as_index=False)
        .agg(
            Revenue=(sales_col, "sum"),
            Profit=(
                profit_col,
                "sum"
            ) if profit_col else (
                sales_col,
                "sum"
            )
        )
        .sort_values(
            "Revenue",
            ascending=False
        )
        .head(10)
    )

    st.markdown(
        '<div class="section-title">Top Products</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        top_products,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# DATA QUALITY / DASHBOARD INFORMATION
# ============================================================

st.markdown("---")

st.markdown(
    '<div class="section-title">Dashboard Information</div>',
    unsafe_allow_html=True
)

info_col1, info_col2, info_col3 = st.columns(3)

with info_col1:
    st.metric(
        "Filtered Records",
        f"{len(filtered_df):,}"
    )

with info_col2:
    st.metric(
        "Dataset Columns",
        f"{len(df.columns):,}"
    )

with info_col3:
    st.metric(
        "Filtered Revenue",
        format_currency(total_revenue)
    )


st.info(
    "Note: Customer Acquisition Cost (CAC) and Churn Rate require "
    "additional marketing-cost and customer-retention data. "
    "They are displayed as N/A when those fields are not available "
    "in the Retail Orders dataset rather than being estimated without "
    "supporting data."
)


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Retail Business Performance Dashboard | "
    "Built with Streamlit, Pandas, NumPy and Plotly"
)
