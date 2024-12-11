
-- 용어 정리 후
SELECT --전체 사용자의 평균 : 각 데이터를 하나씩 출력할 필요가 없음
  AVG(age) AS average_age
FROM
  users;

--각 country 별로 사용자의 수
SELECT
  country, COUNT(*) AS 'user_count'--사용자의 수
FROM
  users
GROUP BY
  country;

-- balance가 가장 많은 사용자의 정보 중, 가장 먼저 조회되는 한 명의 정보
SELECT
  * --사용자 정보 : balance가 가장 많은 사용자 정보 
FROM
  users
WHERE -- 서브 쿼리
  --구할 값에 대한 조건
  balance = (
  SELECT 
    MAX(balance)
  FROM
    users
  )
LIMIT
  1;

--각 country별 평균 balance
SELECT
  country, AVG(balance) AS 'avg_balance' --요약
FROM
  users
GROUP BY
  country;

--bal이 가장 많은 사용자와 적은 사용자의 balance 차이
SELECT
  MAX(balance) - MIN(balance) AS 'balance_difference' --요약
FROM
  users



---------------------------------------------------------------
-- 헷갈려 할 때
SELECT
  AVG(age) AS 'average_age'--평균을 구한다 == 단순 평균을 구한다.
  -- 전체
FROM
  users;
-- 평균으로 뭘 하는게 아니니 조건절을 사용할 필요가 없다

--`각 country별` == 각으로 GROUB화 
--사용자를 나타내는게 아니라, 사용자 수를 구하고자 하는 것
SELECT
  COUNT(country) AS 'user_count' 
FROM
  users
GROUP BY
  country;

SELECT
  country, COUNT(country) AS 'user_count' 
FROM
  users
GROUP BY
  country;

--max만
SELECT
  MAX(balance) 
  --balance가 가장 많은 사용자 == 구하고자 하는 값
FROM
  users
LIMIT
  1; --1명만 조회

SELECT
  *, MAX(balance) --이 값이 나오면 안됨..
FROM
  users
-- GROUP BY --Having == GROUP BY에 주로 사용
--   balance
HAVING
  MAX(balance) -- 집계함수를 여기서 쓰는게 맞나 : HAVING?..?
LIMIT
  1;

SELECT *
FROM users
WHERE balance = ( -- 서브쿼리를 사용하면 된다.
    SELECT MAX(balance)
    FROM users
)
LIMIT 1;

SELECT
  AVG(balance)
FROM
  users
GROUP BY
  country; --각 country == 그룹이 country

SELECT
  --가장 많은 사용자, 가장 적은 사용자
  MAX(balance) - MIN(balance)
FROM
  users;
