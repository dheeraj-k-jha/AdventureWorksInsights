import streamlit as st
import plotly.express as px

from utils.database import run_query
from utils.sidebar import sidebar
from utils.formatter import money, number

st.set_page_config(
    page_title="AdventureWorks Insights | Salesperson Performance",
    page_icon="👨‍💼",
    layout="wide"
)

sidebar()

st.title("👨‍💼 Salesperson Performance")
st.caption(
    "Track salesperson productivity, revenue contribution and target achievement."
)

sales = run_query(
    "SELECT * FROM salesperson_analysis"
)

# -------------------------------------------------
# KPIs
# -------------------------------------------------

best = sales.iloc[0]

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "👨‍💼 Salespersons",
    len(sales)
)

c2.metric(
    "🏆 Top Performer",
    best["salesperson"]
)

c3.metric(
    "💰 Revenue",
    money(sales["revenue"].sum())
)

c4.metric(
    "📦 Orders",
    number(sales["total_orders"].sum())
)

st.divider()

# -------------------------------------------------
# Revenue
# -------------------------------------------------

left,right = st.columns(2)

with left:

    fig = px.bar(
        sales,
        x="salesperson",
        y="revenue",
        text_auto=".2s",
        title="Revenue by Salesperson"
    )

    fig.update_layout(
        template="plotly_dark",
        height=500,
        title_x=.03
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -------------------------------------------------
# Profit
# -------------------------------------------------

with right:

    fig = px.bar(
        sales,
        x="salesperson",
        y="profit",
        text_auto=".2s",
        title="Profit by Salesperson"
    )

    fig.update_layout(
        template="plotly_dark",
        height=500,
        title_x=.03
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -------------------------------------------------
# Revenue vs Target
# -------------------------------------------------
fig = px.bar(
    sales,
    x="salesperson",
    y=["revenue","target"],
    barmode="group",
    title="Revenue vs Target"
)

fig.update_layout(
    template="plotly_dark",
    height=500,
    title_x=.03,
    xaxis_title="Salesperson",
    yaxis_title="Amount"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------------------------------------
# Units Sold
# -------------------------------------------------
fig = px.bar(
    sales,
    x="salesperson",
    y="units_sold",
    text_auto=True,
    title="Units Sold"
)

fig.update_layout(
    template="plotly_dark",
    height=500,
    title_x=.03
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------------------------------------
# Revenue Share
# -------------------------------------------------

fig = px.pie(
    sales,
    names="salesperson",
    values="revenue",
    hole=.55,
    title="Revenue Contribution"
)

fig.update_layout(
    template="plotly_dark",
    height=550
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------------------------------------
# Table
# -------------------------------------------------

st.subheader("Salesperson Performance (Highest to Lowest):")

st.dataframe(
    sales,
    use_container_width=True,
    hide_index=True
)