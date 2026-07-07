import streamlit as st
import plotly.express as px

from utils.database import run_query
from utils.sidebar import sidebar
from utils.formatter import money


#-----------------page config-----------------------
st.set_page_config(
    page_title="AdventureWorks Insights | Business Insights",
    page_icon="💡",
    layout="wide"
)

sidebar()

#------------page title--------------------------------
st.title("💡 Business Insights")
st.caption(
    "Executive summary and actionable recommendations."
)

#-------------loading data-----------------------------
insight = run_query(
    "SELECT * FROM business_insights"
).iloc[0]

st.subheader("Executive Highlights")

c1,c2 = st.columns(2)

with c1:
    
    # best performing category:
    st.success(
        f"""
        ### 🏆 Best Performing Category
        **{insight['best_category']}**
        Revenue: **{money(insight['best_category_revenue'])}**
        """
    )

    # best selling product
    st.success(
        f"""
        ### 📦 Best Selling Product
        **{insight['best_product']}**
        Revenue: **{money(insight['best_product_revenue'])}**
        """
    )

with c2:

    # best region
    st.success(
        f"""
        ### 🌍 Strongest Region
        **{insight['best_region']}**
        Revenue: **{money(insight['best_region_revenue'])}**
        """
    )

    # Top salesperson
    st.success(
        f"""
        ### 👨‍💼 Top Salesperson
        **{insight['best_salesperson']}**
        Revenue: **{money(insight['best_salesperson_revenue'])}**
        """
    )

st.divider()

#--------------------------------------------------------------
#-----------------Business Recommendations---------------------
#--------------------------------------------------------------
st.subheader("Business Recommendations")

st.info("""
• Continue investing in the highest revenue product category.
        
• Allocate more inventory toward top-performing products.
        
• Replicate sales strategies from the highest-performing region.
        
• Study techniques used by the top salesperson and share them across the sales team.
        
• Review performance in low-revenue regions for expansion opportunities.
        
""")

st.divider()

#-----------------Revenue By category-----------------------
st.subheader("Revenue by Category (Color = Profit):")

category = run_query("""
SELECT *
FROM category_sales
""")

fig = px.treemap(
    category,
    path=["category"],
    values="revenue",
    color="profit",
    color_continuous_scale="Blues",
    color_continuous_midpoint=0
)

fig.update_layout(
    template="plotly_dark",
    height=600
)

st.plotly_chart(
    fig,
    use_container_width=True
)