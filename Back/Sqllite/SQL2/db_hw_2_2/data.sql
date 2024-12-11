-- Active: 1728547066499@@127.0.0.1@3306
CREATE TABLE orders(
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_date DATE NOT NULL,
    total_amount REAL NOT NULL
);

CREATE TABLE customers(
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);

ALTER TABLE 
    customers
ADD COLUMN 
    phone TEXT NOT NULL;

ALTER TABLE
    customers
DROP COLUMN
    phone

INSERT INTO
    orders (order_date, total_amount)
VALUES
    ('2023-07-15', 50.99),
    ('2023-07-16', 75.5),
    ('2023-07-17', 30.25)

INSERT INTO
    customers (name, email)
VALUES
    ('허균', 'hong.gildong@example.com'),
    ('김영희', 'kim.younghee@example.com'),
    ('이철수', 'lee.cheolsu@example.com');
    
UPDATE
    customers
SET
    name = '홍길동'
WHERE
    customer_id = 1;
-- DROP TABLE orders

SELECT
    *
FROM
    customers;

SELECT
    *
FROM
    orders;
