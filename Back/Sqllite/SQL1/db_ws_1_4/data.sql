SELECT --사용자의 평균 age, 평균 age만
    AVG(age)
FROM
    users;

-- 이거 확인
SELECT --지금 전라북도만 뜸.. 왜?
    country, COUNT(country) AS "user_count"
    -- country, COUNT(country)
FROM
    users
GROUP BY --그룹별로 묶어야 각지 역마다 계산할 수 있음
    country;
    

--balance가 많은 정보 중, 가장 먼저 조회되는 한명
SELECT
    *, COUNT(balance)
FROM
    users
ORDER BY
    balance
LIMIT
    1;

SELECT 
    country, AVG(balance) AS avg_balance
FROM   
    users
GROUP BY
    country;

-- 각이면 groub을 하고, 그게 아니면 굳이 할 필요가 없음
SELECT -- 제대로 읽어보기
    (MAX(balance) - MIN(balance))
FROM
    users

