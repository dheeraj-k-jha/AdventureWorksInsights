import streamlit as st
import plotly.express as px
from utils.database import run_query
from utils.sidebar import sidebar
from utils.formatter import money , number


# page config:
st.set_page_config(
    page_title="AdventureWorks Insights | Product Insights",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

sidebar()

st.title("📦 Product Insights")
st.caption("Analyze category performance, product revenue, and profitability.")

#----------------------loading data -------------------------------
kpi = run_query("SELECT * FROM category_kpis")
category = run_query("SELECT * FROM category_sales")
top_products = run_query("""
SELECT *
FROM top_products
LIMIT 10
""")

row = kpi.iloc[0]

# -------------------------------
# KPI Cards
# -------------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Revenue",
    money(row['total_revenue'])
)

c2.metric(
    "Profit",
    money(row['total_profit'])
)

c3.metric(
    "Best Category",
    row["best_category"]
)

c4.metric(
    "Units Sold",
    number(row['total_units'])
)

st.divider()


#---------------------Revenue by Category------------------------------
fig = px.bar(
    category,
    x="category",
    y="revenue",
    text_auto=".2s",
    title="Revenue by Category"
)

fig.update_layout(
    xaxis_title="Category",
    yaxis_title="Revenue (₹)",
    height=450
)

st.plotly_chart(fig, use_container_width=True)


#---------------Profit by Category-------------------------------


fig = px.bar(
    category,
    x="category",
    y="profit",
    text_auto=".2s",
    title="Profit by Category"
)

fig.update_layout(
    xaxis_title="Category",
    yaxis_title="Profit (₹)",
    height=450
)

st.plotly_chart(fig, use_container_width=True)


#------------------------Revenue Share------------------------------------


fig = px.pie(
    category,
    names="category",
    values="revenue",
    hole=0.45,
    title="Revenue Distribution"
)

st.plotly_chart(fig, use_container_width=True)


#---------------------Top Products------------------------
fig = px.bar(
    top_products,
    x="revenue",
    y="product",
    orientation="h",
    text_auto=".2s",
    title="Top 10 Products by Revenue"
)

fig.update_layout(
    yaxis=dict(categoryorder="total ascending"),
    xaxis_title="Revenue (₹)",
    yaxis_title="Product",
    height=650
)

st.plotly_chart(fig, use_container_width=True)


# ----------------------Detailed Table-----------------------------
st.subheader("Category Performance")

st.dataframe(
    category,
    use_container_width=True,
    hide_index=True
)

st.subheader("Top 10 Products")

st.dataframe(
    top_products,
    use_container_width=True,
    hide_index=True
)