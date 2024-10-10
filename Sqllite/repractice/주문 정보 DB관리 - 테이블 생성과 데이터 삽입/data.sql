-- Active: 1728566794491@@127.0.0.1@3306
CREATE TABLE orders( --orders라는 테이블을 생성한다.
  order_id INTEGER PRIMARY KEY AUTOINCREMENT,
  order_date DATE NOT NULL,
  total_amount REAL NOT NULL
);

INSERT INTO --어떤것을?
  --table명과 관련 내용
  orders (order_date, total_amount)
VALUES
  ('2023-07-15', 50.99),
  ('2023-07-16', 75.5),
  ('2023-07-17', 30.25);

CREATE TABLE customer(
  customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  phone TEXT NOT NULL
);

INSERT INTO
  customer(name, email, phone)
VALUES
  ('허균', 'hong.gildong@example.com', '010-1234-5678'),
  ('김영희', 'kim.younghee@example.com', '010-9876-5432'),
  ('이철수', 'lee.cheolsu@example.com', '010-5555-4444')


-- 3번쨰 레코드를 삭제 -> 테이블을 아니라 레코드 자체를 삭제하는 것
-- 레코드를 삭제하더라도 테이블을 호출해야함 -> delete from : select없이 
-- 행 자체 레코드 삭제는 delete
DELETE FROM 
  orders --테이블명
WHERE
  order_id = 3; --3번쨰 레코드

--레코드 자체를 수정
UPDATE  --그냥 update
  customer
SET 
  name = "홍길동"
WHERE
  customer_id = 1;

--데이터 조회
SELECT
  *
FROM
  orders;

SELECT
  *
FROM
  customer;