-- Active: 1728568381780@@127.0.0.1@3306
-- orders 테이블 생성: 주문 정보를 저장하기 위한 테이블
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,   -- 주문 ID (기본 키)
    order_date DATE,                -- 주문 날짜 (날짜 타입)
    total_amount REAL               -- 총 주문 금액 (실수 타입)
);

--일반 삭제는 DELETE FROM : 레코드
DROP TABLE --일반 테이블 삭제만 해도 삭제가 이루어짐
    orders;
-- orderstable을 customer과의 관계설정 : customer_id
-- orderid와 연계시킬 것 

--customer과의 관계설정
CREATE TABLE orders(
    order_id INTEGER PRIMARY KEY,   -- 주문 ID (기본 키)
    order_date DATE,                -- 주문 날짜 (날짜 타입)
    total_amount REAL,             -- 총 주문 금액 (실수 타입)
    customer_id INTEGER, --foreign_key가 될 것
    Foreign Key (customer_id) --일단 여기서 설정하라고 함 -> foreign키로 
    REFERENCES customer(customer_id) --무엇을 참고해서? : customer_id -> 바로 customer에 있는
    -- 관계 형성
);


-- orders 테이블에 데이터 삽입
INSERT INTO orders (order_id, order_date, total_amount) VALUES
    (1, '2023-07-15', 50.99),      -- 2023년 7월 15일 주문, 총 주문 금액: 50.99
    (2, '2023-07-16', 75.50),      -- 2023년 7월 16일 주문, 총 주문 금액: 75.50
    (3, '2023-07-17', 30.25);      -- 2023년 7월 17일 주문, 총 주문 금액: 30.25

-- customers 테이블 생성: 고객 정보를 저장하기 위한 테이블
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY, -- 고객 ID (기본 키)
    name TEXT,                      -- 고객 이름 (텍스트 타입)
    email TEXT,                     -- 고객 이메일 (텍스트 타입)
    phone TEXT                      -- 고객 전화번호 (텍스트 타입)
);

-- customers 테이블에 데이터 삽입
INSERT INTO customers (name, email, phone) VALUES
    ('허균', 'hong.gildong@example.com', '010-1234-5678'),    -- 허균 고객 정보
    ('김영희', 'kim.younghee@example.com', '010-9876-5432'),  -- 김영희 고객 정보
    ('이철수', 'lee.cheolsu@example.com', '010-5555-4444');    -- 이철수 고객 정보

-- orders 테이블에서 order_id가 3인 주문 정보 삭제
DELETE FROM orders WHERE order_id = 3;

-- customers 테이블에서 customer_id가 1인 고객의 이름을 '홍길동'으로 수정
UPDATE customers SET name = '홍길동' WHERE customer_id = 1;

-- orders 테이블의 모든 데이터 조회
SELECT * FROM orders;

-- customers 테이블의 모든 데이터 조회
SELECT * FROM customers;

-- orders 테이블 수정 : orders테이블에 pirce 컬럼 추가
ALTER Table
    orders
ADD COLUMN
    price;

ALTER TABLE
    orders
DROP COLUMN
    total_amount;

--orders table에 데이터 최소 3개이상 생성
INSERT INTO
    orders (order_date, customer_id, price)
VALUES 
    ('2023-07-15', 1, 50),
    ('2023-07-16', 2, 75),
    ('2023-07-17', 3, 30);

--orders에 모든 데이터를 조회한다.
SELECT --순서대로 출력을 위해 하나씩 찍어보자
    --customer_id는 customer_id로 출력하면 안됨
    -- 즉 이곳에는 나타낼 값
    orders.order_id, customers.name, orders.order_date, orders.price
    -- customer.id가 아니라 원하는 출력값을 적는다..?
    --단순히 : order_id, customer_id, order_date, price를 하면안됨 어디에 어떤것을 나타낼 것인지?
FROM
    orders --orders의 모든 데이터를 조회한다, 관계를 맺고있는것도 함께 출력해준다.
--JOIN과 관련된 메서드 작성
--inner join
--두 테이블에서 값이 일치하는 레코드에 대해서만 반환
--join된 테이블이름 작성
INNER JOIN customers --어떤게 일치하는지 작성하기 --> ambiguous : 모호한 컬럼 이름
    ON customers.customer_id = orders.customer_id --각각 연결되는 내용에 대해 적기