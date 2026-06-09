/*
TOPIC: INNER JOIN
GOAL: Combine data from multiple tables.
*/
SELECT
    users.name,
    orders.product
FROM users
INNER JOIN orders
ON users.id = orders.user_id;
