-- Active: 1728744664387@@127.0.0.1@3306
-- 데이터베이스 생성
CREATE TABLE orders(
  order_id INTEGER PRIMARY KEY AUTOINCREMENT, --db는 이거 입력해줘야 함
  order_date DATE NOT NULL,
  total_amount REAL NOT NULL
);

--orders 테이블에 데이터 삽입
INSERT INTO --orders 테이블, 어떠한 값에? --> 자동으로 등록되는것 외에 내용 등록
  orders (order_date, total_amount)
VALUES
  ('2023-07-15', 50.99),
  ('2023-07-16', 75.5),
  ('2023-07-17', 30.25)

-- 데이터 수정
DROP TABLE --3번째 레코드 삭제
  orders --orders의 테이블에
WHERE --어디? = 3번쨰 레코드
  order_id = 3;

-- 레코드 자체를 삭제하는 것은 DELETE 사용
DELETE FROM
  orders
WHERE
  order_id = 3;

-- customer 테이블 생성
CREATE TABLE customers (
  customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  phone TEXT NOT NULL
);

INSERT INTO
  customers (name, email, phone)
VALUES
  ('허균', 'hong.gildong@example.com', '010-1234-5678'),
  ('김영희', 'kim.younghee@example.com', '010-9876-5432'),
  ('이철수', 'lee.cheolsu@example.com', '010-5555-4444');


-- 특정 레코드 수정
UPDATE
  customers --table명 : 잘못 기재
SET --어떠한 영역?
  name = '홍길동' --name영역을 홍길동으로 바꿀거야
WHERE --어디?
  customer_id = 1; --customer id가 1인 곳

SELECT
  *
FROM
  orders;

SELECT
  *
FROM
  customers;