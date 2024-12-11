--age가 30에 이상이면서 bal이 1000이상인 사용자 정보 조회
SELECT
  *
FROM
  users
WHERE
  age>=30
  AND balance >= 1000;

-- bal이 1000이하인 사용자 중에서 age가 20세 이하인 사용자 정보 조회
SELECT
  *
FROM
  users
WHERE
  balance <= 1000
  AND age <= 20;

--first_name이 '현'으로 시작하고 country가 '제주특별자치도'인 사용자 중 나이가 가장 많은 사용자
SELECT
  *
FROM
  users u1
WHERE
  (first_name LIKE '현%' --해당 조건을 추가로 걸지 않으면 : 하기에서 추출한 것에서 1차 필터링된것과 비교되어 가장 나이가 많은 값만 나올 것
  AND country LIKE '제주특별자치도') --제주 특별 자치도에서 나이가 가장 많은 사람
  AND age = ( --나이가 가장 많은 사람 추출
    SELECT
      MAX(age) --나이가 가장 많은 사람 : 1명
    FROM
      users u2
    WHERE
      (first_name LIKE '현%'
    AND country LIKE '제주특별자치도')
  );

--last_name이 '박'이고 age가 25세 이상인 사용자 중에서 가장 age가 어린 사용자 정보 조회
SELECT
  *
FROM
  users
WHERE
  (last_name LIKE '박'
  AND age >= 25)
  AND age = (
    SELECT
      MIN(age)
    FROM
      users
    WHERE
      (last_name LIKE '박'
      AND age >= 25)
  );

-- first_name이 재은이거나 영일인 사용자들 중에서 bal가 가장 많은 사용자 정보
SELECT 
  * 
FROM
  users
WHERE
  first_name LIKE '재은'
  OR first_name LIKE '영일'
  AND balance = (
    SELECT 
      MAX(balance)
    FROM
      users
    WHERE
      first_name LIKE '재은'
      OR first_name LIKE '영일'
  );

-- 상기 내용과 동일한 것 참고 : 아빠가 설명해준 것이랑 비슷한 구조
SELECT u.*
FROM users u
JOIN ( --일반적으로 join 다음 where절이 온다.
  SELECT MAX(balance) as max_balance
  FROM users
  WHERE first_name IN ('재은', '영일')
) sub --table명을 sub로
ON u.balance = sub.max_balance --balance끼리 비교
AND u.first_name IN ('재은', '영일');

-- SELECT [columns]
-- FROM [table1]
-- JOIN [table2] ON [join condition]
-- WHERE [filter conditions]
-- GROUP BY [columns]
-- HAVING [group filter conditions]
-- ORDER BY [columns]


-- 각 country 별 가장 많은 bal을 가진 사용자 정보를 조회하고 bal 내림차순 정렬
-- 그룹화되는 것을 1차로 묶고 >> 서브로 돌리면 편하다
-- 그룹일 때 유의
SELECT
  *
FROM
  users
WHERE  --일반적 in 구문 : balance IN (1000, 2000, 3000) 
  (country, balance) IN ( --복합 iN조건
    SELECT
      country, MAX(balance) --(country, balance) IN (SELECT country, MAX(balance)가 묶음
    FROM
      users
    GROUP BY
      country
  )
ORDER BY 
  balance DESC;

SELECT
  *
FROM
  users
WHERE
  age >= 30 --높아야 함
  AND balance >= ( --age가 30세 이상인 사용자들의 평균 BAL보다 
    SELECT
      AVG(balance)
    FROM
      users
    WHERE
      age >= 30
  );

