CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    order_date DATE,
    revenue NUMERIC(12, 2),
    region VARCHAR(100),
    product_name VARCHAR(255),
    salesperson VARCHAR(255)
);
