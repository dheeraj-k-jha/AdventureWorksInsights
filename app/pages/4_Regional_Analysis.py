import streamlit as st
import plotly.express as px

from utils.database import run_query
from utils.sidebar import sidebar
from utils.formatter import money, number

st.set_page_config(
    page_title="AdventureWorks Insights | Regional Analysis",
    page_icon="🌍",
    layout="wide"
)

sidebar()

st.title("🌍 Regional Analysis")
st.caption("Compare performance across regions, territories and markets.")

# ---------------------------------------------------

region = run_query(
    "SELECT * FROM regional_analysis"
)

# ---------------------------------------------------
# KPIs
# ---------------------------------------------------

best = region.iloc[0]

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "🌍 Regions",
    len(region)
)

c2.metric(
    "🏆 Best Region",
    best["region"]
)

c3.metric(
    "💰 Total Revenue",
    money(region["revenue"].sum())
)

c4.metric(
    "📦 Units Sold",
    number(region["units_sold"].sum())
)

st.divider()

# ---------------------------------------------------
# Revenue by Region
# ---------------------------------------------------

left, right = st.columns(2)

with left:

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

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------------------------------------------
# Profit by Region
# ---------------------------------------------------

with right:

    fig = px.bar(
        region,
        x="region",
        y="profit",
        text_auto=".2s",
        title="Profit by Region"
    )

    fig.update_layout(
        template="plotly_dark",
        height=450,
        title_x=0.03
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------------------------------------------
# Revenue Share
# ---------------------------------------------------
fig = px.pie(
    region,
    names="region",
    values="revenue",
    hole=.55,
    title="Revenue Distribution"
)

fig.update_layout(
    template="plotly_dark",
    height=450
)

st.plotly_chart(
    fig,
    use_container_width=True
)
# ---------------------------------------------------
# Average Order Value
# ---------------------------------------------------
fig = px.bar(
    region,
    x="region",
    y="avg_order_value",
    text_auto=".2s",
    title="Average Order Value"
)

fig.update_layout(
    template="plotly_dark",
    height=450,
    title_x=0.03
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------------------
# Table
# ---------------------------------------------------

st.subheader("Regional Performance")

st.dataframe(
    region,
    use_container_width=True,
    hide_index=True
)