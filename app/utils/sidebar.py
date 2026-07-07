import streamlit as st

def sidebar():
    st.sidebar.title("📊 AdventureWorks Insights")
    st.sidebar.caption("Business Intelligence Platform")

    st.sidebar.divider()

    st.sidebar.info(
        """
        **Tech Stack**

        • PostgreSQL

        • Python

        • SQLAlchemy

        • Plotly

        • Streamlit
        """
    )