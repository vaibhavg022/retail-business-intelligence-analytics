import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio
import streamlit.components.v1 as components
from pathlib import Path

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Retail Business Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# DESIGN TOKENS
# ============================================================

BG = "#0A0E16"
PANEL = "#121826"
PANEL_BORDER = "#232B3D"
TEXT = "#E7EBF2"
TEXT_DIM = "#8892A6"
ACCENT = "#F5A623"      # amber — primary signal
ACCENT_2 = "#2FD3C6"    # teal — secondary signal
DANGER = "#FF6B6B"

COLORWAY = [
    "#F5A623", "#2FD3C6", "#5B8DEF", "#FF6B6B",
    "#B98CF7", "#7ED957", "#FFD166", "#4EA8DE"
]

# ============================================================
# PLOTLY DARK TEMPLATE (applies to every px chart below)
# ============================================================

pio.templates["control_room"] = pio.templates["plotly_dark"]
pio.templates["control_room"].layout.update(
    paper_bgcolor=PANEL,
    plot_bgcolor=PANEL,
    font=dict(family="Inter, sans-serif", color=TEXT, size=13),
    title=dict(font=dict(family="Space Grotesk, sans-serif", size=16, color=TEXT)),
    colorway=COLORWAY,
    xaxis=dict(gridcolor=PANEL_BORDER, zerolinecolor=PANEL_BORDER, linecolor=PANEL_BORDER),
    yaxis=dict(gridcolor=PANEL_BORDER, zerolinecolor=PANEL_BORDER, linecolor=PANEL_BORDER),
    legend=dict(bgcolor="rgba(0,0,0,0)"),
    margin=dict(t=60, l=10, r=10, b=10),
)
pio.templates.default = "control_room"

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@600;700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@500;600&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
    }}

    .stApp {{
        background: {BG};
        color: {TEXT};
    }}

    section[data-testid="stSidebar"] {{
        background: {PANEL};
        border-right: 1px solid {PANEL_BORDER};
    }}

    section[data-testid="stSidebar"] * {{
        color: {TEXT} !important;
    }}

    .main .block-container {{
        padding-top: 1.5rem;
        max-width: 1300px;
    }}

    /* ---- Header ---- */
    .db-header {{
        border-left: 3px solid {ACCENT};
        padding-left: 16px;
        margin-bottom: 4px;
    }}

    .db-header h1 {{
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        font-size: 30px;
        color: {TEXT};
        margin: 0;
        line-height: 1.2;
    }}

    .db-header p {{
        color: {TEXT_DIM};
        font-size: 15px;
        margin: 4px 0 0 0;
    }}

    .db-meta {{
        font-family: 'IBM Plex Mono', monospace;
        color: {TEXT_DIM};
        font-size: 12.5px;
        margin: 10px 0 24px 19px;
        letter-spacing: 0.2px;
    }}

    /* ---- Section headers (replace st.subheader look) ---- */
    .db-section {{
        display: flex;
        align-items: baseline;
        gap: 10px;
        margin: 34px 0 14px 0;
        padding-bottom: 8px;
        border-bottom: 1px solid {PANEL_BORDER};
    }}

    .db-section .bar {{
        width: 8px;
        height: 8px;
        border-radius: 2px;
        background: {ACCENT};
        flex-shrink: 0;
        margin-bottom: 3px;
    }}

    .db-section h3 {{
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 600;
        font-size: 19px;
        color: {TEXT};
        margin: 0;
    }}

    .db-section span.sub {{
        color: {TEXT_DIM};
        font-size: 13px;
    }}

    /* ---- KPI cards ---- */
    .kpi-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(175px, 1fr));
        gap: 12px;
        margin-bottom: 6px;
    }}

    .kpi-card {{
        background: {PANEL};
        border: 1px solid {PANEL_BORDER};
        border-top: 2px solid var(--kpi-accent, {ACCENT});
        border-radius: 8px;
        padding: 16px 18px;
    }}

    .kpi-card .kpi-label {{
        color: {TEXT_DIM};
        font-size: 12.5px;
        font-weight: 500;
        margin-bottom: 6px;
    }}

    .kpi-card .kpi-value {{
        font-family: 'IBM Plex Mono', monospace;
        font-weight: 600;
        font-size: 24px;
        color: {TEXT};
        letter-spacing: -0.3px;
    }}

    /* ---- Misc Streamlit element overrides ---- */
    div[data-testid="stMetric"] {{
        background: {PANEL};
        border: 1px solid {PANEL_BORDER};
        border-radius: 8px;
        padding: 14px 16px;
    }}

    .stDataFrame {{
        border: 1px solid {PANEL_BORDER};
        border-radius: 8px;
        overflow: hidden;
    }}

    .stAlert {{
        background: {PANEL};
        border: 1px solid {PANEL_BORDER};
        border-radius: 8px;
    }}

    hr {{
        border-color: {PANEL_BORDER};
    }}

    /* ---- Entrance + reveal animation ---- */
    @keyframes fadeInUp {{
        from {{ opacity: 0; transform: translateY(14px); }}
        to   {{ opacity: 1; transform: translateY(0); }}
    }}

    @keyframes pulseGlow {{
        0%, 100% {{ box-shadow: 0 0 0 0 rgba(245,166,35,0.45); }}
        50%      {{ box-shadow: 0 0 7px 2px rgba(245,166,35,0.45); }}
    }}

    .kpi-card {{
        animation: fadeInUp 0.55s ease-out backwards;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }}
    .kpi-card:hover {{
        transform: translateY(-3px);
        border-color: var(--kpi-accent, {ACCENT});
    }}
    .kpi-card:nth-child(1) {{ animation-delay: 0.02s; }}
    .kpi-card:nth-child(2) {{ animation-delay: 0.08s; }}
    .kpi-card:nth-child(3) {{ animation-delay: 0.14s; }}
    .kpi-card:nth-child(4) {{ animation-delay: 0.20s; }}
    .kpi-card:nth-child(5) {{ animation-delay: 0.26s; }}
    .kpi-card:nth-child(6) {{ animation-delay: 0.32s; }}

    .db-section .bar {{
        animation: pulseGlow 2.4s ease-in-out infinite;
    }}

    /* Charts & tables fade/slide into view as you scroll to them */
    div[data-testid="stPlotlyChart"],
    div[data-testid="stDataFrame"] {{
        opacity: 0;
        transform: translateY(18px);
        transition: opacity 0.7s ease, transform 0.7s ease;
    }}
    div[data-testid="stPlotlyChart"].tr-in-view,
    div[data-testid="stDataFrame"].tr-in-view {{
        opacity: 1 !important;
        transform: translateY(0) !important;
    }}
</style>
""", unsafe_allow_html=True)


def inject_dynamic_fx():
    """Injects a low-key animated particle network behind the app and a
    scroll-reveal observer for charts/tables. Runs in the parent document
    so it persists as a fixed background across the whole page."""
    components.html("""
    <script>
    (function() {
        const doc = window.parent.document;

        // ---------- animated particle network background ----------
        if (!doc.getElementById('tech-bg-canvas')) {
            const canvas = doc.createElement('canvas');
            canvas.id = 'tech-bg-canvas';
            Object.assign(canvas.style, {
                position: 'fixed', top: '0', left: '0',
                width: '100vw', height: '100vh',
                zIndex: '-1', pointerEvents: 'none', opacity: '0.5'
            });
            doc.body.appendChild(canvas);

            const ctx = canvas.getContext('2d');
            let w, h;
            function resize() {
                w = canvas.width = window.parent.innerWidth;
                h = canvas.height = window.parent.innerHeight;
            }
            resize();
            window.parent.addEventListener('resize', resize);

            const COUNT = 65;
            const colors = ['__ACCENT__', '__ACCENT2__'];
            const pts = [];
            for (let i = 0; i < COUNT; i++) {
                pts.push({
                    x: Math.random() * w, y: Math.random() * h,
                    vx: (Math.random() - 0.5) * 0.28,
                    vy: (Math.random() - 0.5) * 0.28,
                    r: Math.random() * 1.4 + 0.6,
                    c: colors[i % 2]
                });
            }

            (function tick() {
                ctx.clearRect(0, 0, w, h);
                for (const p of pts) {
                    p.x += p.vx; p.y += p.vy;
                    if (p.x < 0 || p.x > w) p.vx *= -1;
                    if (p.y < 0 || p.y > h) p.vy *= -1;
                }
                for (let i = 0; i < COUNT; i++) {
                    for (let j = i + 1; j < COUNT; j++) {
                        const dx = pts[i].x - pts[j].x, dy = pts[i].y - pts[j].y;
                        const dist = Math.sqrt(dx * dx + dy * dy);
                        if (dist < 125) {
                            ctx.strokeStyle = 'rgba(47,211,198,' + (0.14 * (1 - dist / 125)) + ')';
                            ctx.lineWidth = 0.6;
                            ctx.beginPath();
                            ctx.moveTo(pts[i].x, pts[i].y);
                            ctx.lineTo(pts[j].x, pts[j].y);
                            ctx.stroke();
                        }
                    }
                }
                for (const p of pts) {
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
                    ctx.fillStyle = p.c;
                    ctx.fill();
                }
                requestAnimationFrame(tick);
            })();
        }

        // ---------- scroll-reveal for charts & tables ----------
        if (!window.parent.__trObserver) {
            window.parent.__trObserver = new IntersectionObserver((entries) => {
                entries.forEach(e => {
                    if (e.isIntersecting) {
                        e.target.classList.add('tr-in-view');
                        window.parent.__trObserver.unobserve(e.target);
                    }
                });
            }, { threshold: 0.15 });
        }

        setInterval(() => {
            doc.querySelectorAll('[data-testid="stPlotlyChart"]:not(.tr-observed), [data-testid="stDataFrame"]:not(.tr-observed)')
                .forEach(el => {
                    el.classList.add('tr-observed');
                    window.parent.__trObserver.observe(el);
                });
        }, 400);
    })();
    </script>
    """.replace("__ACCENT__", ACCENT).replace("__ACCENT2__", ACCENT_2), height=0, width=0)


inject_dynamic_fx()


def section_header(title, subtitle=None):
    """Renders a styled section header in place of st.subheader."""
    sub_html = f'<span class="sub">— {subtitle}</span>' if subtitle else ""
    st.markdown(
        f'<div class="db-section"><div class="bar"></div>'
        f'<h3>{title}</h3>{sub_html}</div>',
        unsafe_allow_html=True
    )


def kpi_grid(cards):
    """cards: list of (label, value, accent_color) tuples."""
    html = '<div class="kpi-grid">'
    for label, value, accent in cards:
        html += (
            f'<div class="kpi-card" style="--kpi-accent:{accent}">'
            f'<div class="kpi-label">{label}</div>'
            f'<div class="kpi-value">{value}</div>'
            f'</div>'
        )
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


# ============================================================
# DATASET CONFIGURATION
# ============================================================

EXPECTED_COLUMNS = [
    "transaction_id",
    "customer_id",
    "category",
    "item",
    "price_per_unit",
    "quantity",
    "total_spent",
    "payment_method",
    "transaction_date",
    "discount_applied",
    "year",
    "month",
    "month_name",
    "average_transaction_value",
    "discount_status"
]


# ============================================================
# FIND DATASET
# ============================================================

def find_dataset():

    base_dir = Path(__file__).resolve().parent
    data_dir = base_dir / "data"

    possible_files = [
        data_dir / "retail-orders-clean.csv",
        data_dir / "clean_dataset.csv",
        data_dir / "retail_orders_clean.csv",
        data_dir / "retail_orders.csv"
    ]

    for file in possible_files:
        if file.exists():
            return file

    csv_files = list(data_dir.glob("*.csv"))

    if len(csv_files) == 1:
        return csv_files[0]

    if len(csv_files) > 1:
        st.error(
            "Multiple CSV files found in the data folder. "
            "Please keep only the Task 03 cleaned dataset."
        )

        st.write("CSV files found:")

        for file in csv_files:
            st.write(f"- `{file.name}`")

        st.stop()

    return None


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_dataset(file_path):

    df = pd.read_csv(file_path)

    # Remove accidental spaces from column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Remove accidental markdown ** if present
    df.columns = df.columns.str.replace("*", "", regex=False)

    # Remove BOM
    df.columns = df.columns.str.replace("\ufeff", "", regex=False)

    # Check columns
    missing_columns = [
        col for col in EXPECTED_COLUMNS
        if col not in df.columns
    ]

    if missing_columns:
        st.error("Dataset columns do not match the expected Task 03 dataset.")

        st.write("### Missing columns")
        st.write(missing_columns)

        st.write("### Columns detected in your CSV")
        st.write(list(df.columns))

        st.stop()

    # Keep expected columns
    df = df[EXPECTED_COLUMNS].copy()

    # --------------------------------------------------------
    # DATA TYPE CONVERSION
    # --------------------------------------------------------

    numeric_columns = [
        "price_per_unit",
        "quantity",
        "total_spent",
        "discount_applied",
        "year",
        "month",
        "average_transaction_value"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["transaction_date"] = pd.to_datetime(
        df["transaction_date"],
        errors="coerce"
    )

    # Remove rows where essential values are missing
    df = df.dropna(
        subset=[
            "transaction_id",
            "customer_id",
            "category",
            "total_spent",
            "transaction_date"
        ]
    )

    return df


# ============================================================
# GET DATASET
# ============================================================

dataset_path = find_dataset()

if dataset_path is None:

    st.error(
        "No CSV dataset found."
    )

    st.info(
        "Place your cleaned CSV inside the `data` folder "
        "and name it `retail-orders-clean.csv`."
    )

    st.stop()


df = load_dataset(dataset_path)


# ============================================================
# CALCULATED METRICS
# ============================================================

total_revenue = df["total_spent"].sum()

total_transactions = df["transaction_id"].nunique()

total_customers = df["customer_id"].nunique()

average_order_value = (
    total_revenue / total_transactions
    if total_transactions > 0
    else 0
)

total_quantity = df["quantity"].sum()

discount_transactions = (
    df["discount_applied"].eq(1).sum()
)

discount_percentage = (
    discount_transactions / len(df) * 100
    if len(df) > 0
    else 0
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="db-header">'
    '<h1>Retail Business Dashboard</h1>'
    '<p>Interactive sales, customer & business performance analysis</p>'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="db-meta">DATASET: {dataset_path.name}  |  RECORDS: {len(df):,}</div>',
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.markdown("### 🔎 Dashboard Filters")

# Date filter

min_date = df["transaction_date"].min().date()
max_date = df["transaction_date"].max().date()

date_range = st.sidebar.date_input(
    "Transaction Date",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if isinstance(date_range, tuple) and len(date_range) == 2:

    start_date = pd.Timestamp(date_range[0])
    end_date = pd.Timestamp(date_range[1])

else:

    start_date = pd.Timestamp(min_date)
    end_date = pd.Timestamp(max_date)


# Category

categories = sorted(
    df["category"].dropna().unique().tolist()
)

selected_categories = st.sidebar.multiselect(
    "Category",
    categories,
    default=categories
)


# Payment method

payment_methods = sorted(
    df["payment_method"].dropna().unique().tolist()
)

selected_payment = st.sidebar.multiselect(
    "Payment Method",
    payment_methods,
    default=payment_methods
)


# Discount

discount_options = sorted(
    df["discount_status"].dropna().unique().tolist()
)

selected_discount = st.sidebar.multiselect(
    "Discount Status",
    discount_options,
    default=discount_options
)


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df[
    (df["transaction_date"] >= start_date)
    & (df["transaction_date"] <= end_date)
    & (df["category"].isin(selected_categories))
    & (df["payment_method"].isin(selected_payment))
    & (df["discount_status"].isin(selected_discount))
].copy()


# ============================================================
# FILTERED KPIs
# ============================================================

revenue = filtered_df["total_spent"].sum()

transactions = filtered_df["transaction_id"].nunique()

customers = filtered_df["customer_id"].nunique()

aov = revenue / transactions if transactions > 0 else 0

quantity = filtered_df["quantity"].sum()


# ============================================================
# KPI CARDS
# ============================================================

section_header("Executive KPIs")

kpi_grid([
    ("Revenue", f"₹{revenue:,.0f}", ACCENT),
    ("Transactions", f"{transactions:,}", ACCENT_2),
    ("Customers", f"{customers:,}", ACCENT),
    ("Avg order value", f"₹{aov:,.2f}", ACCENT_2),
    ("Total quantity", f"{quantity:,.0f}", ACCENT),
    ("Discount transactions", f"{discount_percentage:.1f}%", ACCENT_2),
])


# ============================================================
# CHECK EMPTY DATA
# ============================================================

if filtered_df.empty:

    st.warning(
        "No data available for the selected filters."
    )

    st.stop()


# ============================================================
# REVENUE TREND
# ============================================================

section_header("Revenue Trend")

monthly_revenue = (
    filtered_df
    .groupby(
        filtered_df["transaction_date"].dt.to_period("M")
    )["total_spent"]
    .sum()
    .reset_index()
)

monthly_revenue["transaction_date"] = (
    monthly_revenue["transaction_date"]
    .dt.to_timestamp()
)

fig_revenue = px.area(
    monthly_revenue,
    x="transaction_date",
    y="total_spent",
    markers=True,
    title="Monthly Revenue Trend"
)

fig_revenue.update_traces(line_color=ACCENT, fillcolor="rgba(245,166,35,0.12)")

fig_revenue.update_layout(
    xaxis_title="Month",
    yaxis_title="Revenue (₹)",
    hovermode="x unified"
)

st.plotly_chart(
    fig_revenue,
    use_container_width=True
)


# ============================================================
# CATEGORY ANALYSIS
# ============================================================

section_header("Category Performance")

col1, col2 = st.columns(2)


category_revenue = (
    filtered_df
    .groupby("category")["total_spent"]
    .sum()
    .reset_index()
    .sort_values("total_spent", ascending=False)
)


with col1:

    fig_category = px.bar(
        category_revenue,
        x="category",
        y="total_spent",
        title="Revenue by Category",
        text_auto=".2s",
        color="category",
        color_discrete_sequence=COLORWAY
    )

    fig_category.update_layout(
        xaxis_title="Category",
        yaxis_title="Revenue (₹)",
        showlegend=False
    )

    st.plotly_chart(
        fig_category,
        use_container_width=True
    )


with col2:

    fig_category_pie = px.pie(
        category_revenue,
        names="category",
        values="total_spent",
        title="Revenue Share by Category",
        hole=0.55,
        color_discrete_sequence=COLORWAY
    )

    st.plotly_chart(
        fig_category_pie,
        use_container_width=True
    )


# ============================================================
# PAYMENT METHOD
# ============================================================

section_header("Payment Method Analysis")

payment_revenue = (
    filtered_df
    .groupby("payment_method")["total_spent"]
    .sum()
    .reset_index()
    .sort_values("total_spent", ascending=False)
)

fig_payment = px.bar(
    payment_revenue,
    x="payment_method",
    y="total_spent",
    color="payment_method",
    title="Revenue by Payment Method",
    text_auto=".2s",
    color_discrete_sequence=COLORWAY
)

fig_payment.update_layout(
    xaxis_title="Payment Method",
    yaxis_title="Revenue (₹)",
    showlegend=False
)

st.plotly_chart(
    fig_payment,
    use_container_width=True
)


# ============================================================
# DISCOUNT ANALYSIS
# ============================================================

section_header("Discount Analysis")

discount_analysis = (
    filtered_df
    .groupby("discount_status")
    .agg(
        Revenue=("total_spent", "sum"),
        Transactions=("transaction_id", "nunique"),
        Quantity=("quantity", "sum")
    )
    .reset_index()
)


col1, col2 = st.columns(2)

with col1:

    fig_discount = px.bar(
        discount_analysis,
        x="discount_status",
        y="Revenue",
        title="Revenue by Discount Status",
        text_auto=".2s",
        color="discount_status",
        color_discrete_sequence=COLORWAY
    )

    fig_discount.update_layout(showlegend=False)

    st.plotly_chart(
        fig_discount,
        use_container_width=True
    )

with col2:

    fig_discount_pie = px.pie(
        discount_analysis,
        names="discount_status",
        values="Transactions",
        title="Transactions by Discount Status",
        hole=0.55,
        color_discrete_sequence=COLORWAY
    )

    st.plotly_chart(
        fig_discount_pie,
        use_container_width=True
    )


# ============================================================
# CATEGORY × MONTH HEATMAP
# ============================================================

section_header("Category × Monthly Revenue Heatmap")

heatmap_data = (
    filtered_df
    .assign(
        month_period=filtered_df["transaction_date"].dt.to_period("M")
    )
    .groupby(
        ["category", "month_period"]
    )["total_spent"]
    .sum()
    .reset_index()
)

heatmap_data["month_period"] = (
    heatmap_data["month_period"].astype(str)
)

heatmap_pivot = heatmap_data.pivot(
    index="category",
    columns="month_period",
    values="total_spent"
).fillna(0)

fig_heatmap = px.imshow(
    heatmap_pivot,
    aspect="auto",
    title="Monthly Revenue by Category",
    labels={
        "x": "Month",
        "y": "Category",
        "color": "Revenue"
    },
    color_continuous_scale=[PANEL, ACCENT_2, ACCENT]
)

st.plotly_chart(
    fig_heatmap,
    use_container_width=True
)


# ============================================================
# TOP ITEMS
# ============================================================

section_header("Top Performing Items")

item_revenue = (
    filtered_df
    .groupby("item")["total_spent"]
    .sum()
    .reset_index()
    .sort_values(
        "total_spent",
        ascending=False
    )
    .head(10)
)

fig_items = px.bar(
    item_revenue,
    x="total_spent",
    y="item",
    orientation="h",
    title="Top 10 Items by Revenue",
    text_auto=".2s",
    color_discrete_sequence=[ACCENT]
)

fig_items.update_layout(
    xaxis_title="Revenue (₹)",
    yaxis_title="Item",
    yaxis={
        "categoryorder": "total ascending"
    }
)

st.plotly_chart(
    fig_items,
    use_container_width=True
)


# ============================================================
# YEARLY PERFORMANCE
# ============================================================

section_header("Yearly Performance")

yearly_data = (
    filtered_df
    .groupby("year")
    .agg(
        Revenue=("total_spent", "sum"),
        Transactions=("transaction_id", "nunique"),
        Customers=("customer_id", "nunique"),
        Quantity=("quantity", "sum")
    )
    .reset_index()
)

fig_year = px.bar(
    yearly_data,
    x="year",
    y="Revenue",
    text_auto=".2s",
    title="Revenue by Year",
    color_discrete_sequence=[ACCENT_2]
)

st.plotly_chart(
    fig_year,
    use_container_width=True
)


# ============================================================
# CUSTOMER ANALYSIS
# ============================================================

section_header("Customer Analysis")

customer_data = (
    filtered_df
    .groupby("customer_id")
    .agg(
        Total_Spent=("total_spent", "sum"),
        Transactions=("transaction_id", "nunique"),
        Quantity=("quantity", "sum")
    )
    .reset_index()
    .sort_values(
        "Total_Spent",
        ascending=False
    )
)

col1, col2 = st.columns(2)

with col1:

    st.markdown("**Top Customers**")

    st.dataframe(
        customer_data.head(10),
        use_container_width=True,
        hide_index=True
    )


with col2:

    fig_customer = px.scatter(
        customer_data,
        x="Transactions",
        y="Total_Spent",
        size="Quantity",
        hover_name="customer_id",
        title="Customer Spending vs Transactions",
        color_discrete_sequence=[ACCENT]
    )

    st.plotly_chart(
        fig_customer,
        use_container_width=True
    )


# ============================================================
# DATA QUALITY
# ============================================================

section_header("Data Quality Overview")

quality_col1, quality_col2, quality_col3 = st.columns(3)

with quality_col1:

    st.metric(
        "Rows",
        f"{len(filtered_df):,}"
    )

with quality_col2:

    st.metric(
        "Columns",
        f"{len(filtered_df.columns):,}"
    )

with quality_col3:

    missing_values = int(
        filtered_df.isnull().sum().sum()
    )

    st.metric(
        "Missing Values",
        f"{missing_values:,}"
    )


# ============================================================
# DATA PREVIEW
# ============================================================

with st.expander("📋 View Dataset"):

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# LIMITATIONS / DATASET NOTE
# ============================================================

st.info(
    """
    **Dashboard Data Note**

    The dataset contains transaction, customer, category, item,
    payment, date, quantity, revenue and discount information.

    Customer Acquisition Cost (CAC) and Churn Rate cannot be
    calculated from this dataset because acquisition-cost and
    customer-churn fields are not present.

    Geographic heatmaps are also not included because the
    `location`/geographic field is not available in this
    15-column dataset.
    """
)


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

