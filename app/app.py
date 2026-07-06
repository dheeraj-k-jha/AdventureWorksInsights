import streamlit as st

st.set_page_config(
    page_title="AdventureWorksInsights",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AdventureWorksInsights")

st.subheader("Business Intelligence & Sales Analytics Platform")

st.markdown("""
Welcome to **AdventureWorksInsights**.

This dashboard provides interactive analytics on:

- Executive KPIs
- Sales Performance
- Product Insights
- Regional Performance
- Salesperson Analytics
- Business Insights

Built using PostgreSQL, Python and Streamlit.
""")