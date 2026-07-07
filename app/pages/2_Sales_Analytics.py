import streamlit as st
import plotly.express as px
from utils.database import run_query
from utils.sidebar import sidebar
from utils.formatter import money , number


# page config:
st.set_page_config(
    page_title="AdventureWorks Insights | Product Insights",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="expanded"
)

sidebar()

st.title("💸 Sales Analytics")
st.caption("Analyze monthly sales ,revenue , profit , revenue v/s profit , units sold.")

#---------------computed values-------------------------------------
sales = run_query("SELECT * FROM sales_analytics")

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "💰 Revenue",
    money(sales["revenue"].sum())
)

col2.metric(
    "📈 Profit",
    money(sales["profit"].sum())
)

col3.metric(
    "🛒 Avg Order Value",
    money(sales["avg_order_value"].mean())
)

col4.metric(
    "📊 Avg Profit Margin",
    f"{sales['profit_margin'].mean():.2f}%"
)

#------------------------------charts------------------------------
left, right = st.columns(2)

# Revenue Trend
with left:

    fig = px.line(
        sales,
        x="month",
        y="revenue",
        markers=True,
        title="Revenue Trend"
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

# Profit Trend
with right:

    fig = px.area(
        sales,
        x="month",
        y="profit",
        title="Profit Trend"
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


# charts: 
left, right = st.columns(2)

# Orders
with left:

    fig = px.bar(
        sales,
        x="month",
        y="orders",
        title="Orders per Month"
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

# Revenue vs Cost
with right:

    fig = px.line(
        sales,
        x="month",
        y=["revenue", "cost"],
        markers=True,
        title="Revenue vs Cost"
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


# Units Sold
fig = px.bar(
    sales,
    x="month",
    y="units",
    title="Units Sold per Month"
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


#-----------------Table-----------------------------------------
st.dataframe(
    sales,
    use_container_width=True,
    hide_index=True
)