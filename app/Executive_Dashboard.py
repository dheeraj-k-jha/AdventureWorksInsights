import plotly.express as px
import streamlit as st
from utils.formatter import money , number
from utils.sidebar import sidebar


# adding root folder to sys.path
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

# connecting to database:
from utils.database import run_query

# page config:
st.set_page_config(
    page_title="AdventureWorks Insights | Executive Dashbaord",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

sidebar()

st.title("📊 AdventureWorks Insights")
st.markdown(
"""
### Welcome

AdventureWorks Insights is an executive business intelligence dashboard
designed for interactive sales and product analysis.
"""
)

# kpi cards
st.header("Key KPI's: ")
kpi = run_query("SELECT * FROM executive_kpis")

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "💰 Revenue",
    money(kpi.iloc[0]['total_revenue'])
)

c2.metric(
    "📈 Profit",
    money(kpi.iloc[0]['total_profit'])
)

c3.metric(
    "🧾 Orders",
    number(kpi.iloc[0]['total_orders'])
)

c4.metric(
    "📦 Units",
    number(kpi.iloc[0]['total_quantity'])
)


# monthly trend:
monthly = run_query("""
SELECT *
FROM monthly_sales
""")

fig = px.line(
    monthly,
    x="month",
    y="revenue",
    markers=True,
    title="Monthly Revenue Trend"
)

fig.update_layout(
    template="plotly_dark",
    height=450,
    title_x=0.03,
    xaxis_title="Month",
    yaxis_title="Revenue (₹)",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)

#--------------region sales--------------------------------
region = run_query("SELECT * FROM regional_sales")

fig = px.bar(
    region,
    x="region",
    y="revenue",
    text_auto=".2s",
    title="Revenue by Region"
)

fig.update_layout(
    template="plotly_dark",
    height=450,
    title_x=0.03
)

st.plotly_chart(fig, use_container_width=True)

# ------------------category wise revenue----------------------------------
category = run_query("SELECT * FROM category_sales")

fig = px.pie(
    category,
    names="category",
    values="revenue",
    hole=.55,
    title="Revenue Distribution"
)

fig.update_layout(
    template="plotly_dark",
    height=450
)

st.plotly_chart(fig, use_container_width=True)

#---------------------------Top Products-----------------------------------
top_products = run_query("""
SELECT *
FROM top_products
LIMIT 5
""")

fig = px.bar(
    top_products,
    x="revenue",
    y="product",
    orientation="h",
    text_auto=".2s",
    title="Top Products"
)

fig.update_layout(
    template="plotly_dark",
    height=450,
    yaxis=dict(categoryorder="total ascending")
)

st.plotly_chart(fig, use_container_width=True)

# Top products table:
st.subheader("🏆 Top Products")

st.dataframe(
    top_products,
    use_container_width=True,
    hide_index=True
)