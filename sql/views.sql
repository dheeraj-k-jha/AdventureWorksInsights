CREATE OR REPLACE VIEW sales_summary AS
SELECT
    DATE_TRUNC('month', order_date) AS order_month,
    SUM(revenue) AS total_revenue,
    COUNT(*) AS order_count
FROM sales
GROUP BY DATE_TRUNC('month', order_date);
