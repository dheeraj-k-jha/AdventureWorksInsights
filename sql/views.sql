-- executive kpis
CREATE OR REPLACE VIEW executive_kpis AS
SELECT
    SUM(sales) AS total_revenue,
    SUM(cost) AS total_cost,
    SUM(sales - cost) AS total_profit,
    COUNT(DISTINCT salesordernumber) AS total_orders,
    SUM(quantity) AS total_quantity
FROM sales;

-- monthly_sales
CREATE OR REPLACE VIEW monthly_sales AS
SELECT
    DATE_TRUNC('month', orderdate) AS month,
    ROUND(SUM(sales)::numeric, 2) AS revenue,
    ROUND(SUM(cost)::numeric, 2) AS cost,
    ROUND(SUM(sales - cost)::numeric, 2) AS profit,
    COUNT(DISTINCT salesordernumber) AS orders
FROM sales
GROUP BY month
ORDER BY month;


-- category kpis
CREATE OR REPLACE VIEW category_kpis AS
SELECT
    ROUND(SUM(s.sales)::numeric, 2) AS total_revenue,
    ROUND(SUM(s.sales - s.cost)::numeric, 2) AS total_profit,
    (
        SELECT p.category
        FROM sales s
        JOIN product p
        ON s.productkey = p.productkey
        GROUP BY p.category
        ORDER BY SUM(s.sales) DESC
        LIMIT 1
    ) AS best_category,
    SUM(quantity) AS total_units
FROM sales s;


-- category sales
CREATE OR REPLACE VIEW category_sales AS
SELECT
    p.category,
    ROUND(SUM(s.sales)::numeric, 2) AS revenue,
    ROUND(SUM(s.cost)::numeric, 2) AS cost,
    ROUND(SUM(s.sales - s.cost)::numeric, 2) AS profit,
    SUM(s.quantity) AS units_sold
FROM sales s
JOIN product p
ON s.productkey = p.productkey
GROUP BY p.category
ORDER BY revenue DESC;

-- Top products:
CREATE OR REPLACE VIEW top_products AS
SELECT
    p.product,
    p.category,
    SUM(s.quantity) AS units_sold,
    ROUND(SUM(s.sales)::numeric, 2) AS revenue,
    ROUND(SUM(s.sales - s.cost)::numeric, 2) AS profit,
    RANK() OVER (ORDER BY SUM(s.sales) DESC) AS revenue_rank
FROM sales s
JOIN product p
ON s.productkey = p.productkey
GROUP BY
    p.product,
    p.category
ORDER BY revenue DESC;


-- region sales:
CREATE OR REPLACE VIEW regional_sales AS
SELECT
    r.region,
    ROUND(SUM(s.sales)::numeric,2) revenue,
    ROUND(SUM(s.sales-s.cost)::numeric,2) profit
FROM sales s
JOIN region r
ON s.salesterritorykey=r.salesterritorykey
GROUP BY r.region
ORDER BY revenue DESC;


-- sales analystics:
CREATE OR REPLACE VIEW sales_analytics AS
SELECT
    DATE_TRUNC('month',orderdate) AS month,
    ROUND(SUM(sales)::numeric,2) AS revenue,
    ROUND(SUM(cost)::numeric,2) AS cost,
    ROUND(SUM(sales-cost)::numeric,2) AS profit,
    COUNT(DISTINCT salesordernumber) AS orders,
    SUM(quantity) AS units,
    ROUND(
        AVG(sales)::numeric,
        2
    ) AS avg_order_value,
    ROUND(
        ((SUM(sales-cost)/SUM(sales))*100)::numeric,
        2
    ) AS profit_margin
FROM sales
GROUP BY month
ORDER BY month;

-- region wise metrics:
CREATE OR REPLACE VIEW regional_analysis AS
SELECT
    r.region,
    r.country,
    r.group,
    ROUND(SUM(s.sales)::numeric,2) AS revenue,
    ROUND(SUM(s.cost)::numeric,2) AS cost,
    ROUND(SUM(s.sales-s.cost)::numeric,2) AS profit,
    SUM(s.quantity) AS units_sold,
    COUNT(DISTINCT s.salesordernumber) AS total_orders,
    ROUND(AVG(s.sales)::numeric,2) AS avg_order_value
FROM sales s
JOIN region r
ON s.salesterritorykey = r.salesterritorykey
GROUP BY
    r.region,
    r.country,
    r.group
ORDER BY revenue DESC;


-- sales person performance analysis-------------------------------
CREATE OR REPLACE VIEW salesperson_analysis AS
WITH sales_summary AS (
    SELECT
        employeekey,
        ROUND(SUM(sales)::numeric,2) AS revenue,
        ROUND(SUM(cost)::numeric,2) AS cost,
        ROUND(SUM(sales-cost)::numeric,2) AS profit,
        SUM(quantity) AS units_sold,
        COUNT(DISTINCT salesordernumber) AS total_orders,
        ROUND(AVG(sales)::numeric,2) AS avg_order_value
    FROM sales
    GROUP BY employeekey
),
target_summary AS (
    SELECT
        employeeid,
        ROUND(SUM(target)::numeric,2) AS target
    FROM targets
    GROUP BY employeeid
)
SELECT
    sp.employeekey,
    sp.salesperson,
    sp.title,

    ss.revenue,
    ss.cost,
    ss.profit,
    ss.units_sold,
    ss.total_orders,
    ss.avg_order_value,

    COALESCE(ts.target,0) AS target,
    ROUND(
        (ss.revenue / NULLIF(ts.target,0)) * 100,
        2
    ) AS target_achievement

FROM salesperson sp
JOIN sales_summary ss
ON sp.employeekey = ss.employeekey

LEFT JOIN target_summary ts
ON sp.employeeid = ts.employeeid

ORDER BY ss.revenue DESC;

---- Business Insights ------------------
CREATE OR REPLACE VIEW business_insights AS
SELECT
    (SELECT category
     FROM category_sales
     ORDER BY revenue DESC
     LIMIT 1) AS best_category,

    (SELECT revenue
     FROM category_sales
     ORDER BY revenue DESC
     LIMIT 1) AS best_category_revenue,

    (SELECT product
     FROM top_products
     ORDER BY revenue DESC
     LIMIT 1) AS best_product,

    (SELECT revenue
     FROM top_products
     ORDER BY revenue DESC
     LIMIT 1) AS best_product_revenue,

    (SELECT region
     FROM regional_analysis
     ORDER BY revenue DESC
     LIMIT 1) AS best_region,

    (SELECT revenue
     FROM regional_analysis
     ORDER BY revenue DESC
     LIMIT 1) AS best_region_revenue,

    (SELECT salesperson
     FROM salesperson_analysis
     ORDER BY revenue DESC
     LIMIT 1) AS best_salesperson,

    (SELECT revenue
     FROM salesperson_analysis
     ORDER BY revenue DESC
     LIMIT 1) AS best_salesperson_revenue;
