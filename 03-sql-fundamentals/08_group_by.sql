/*
TOPIC: GROUP BY
GOAL: Aggregate data by category.
*/
SELECT
    product,
    SUM(sales_amount) AS total_sales
FROM sales
GROUP BY product;
