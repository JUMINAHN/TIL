SELECT
    *
FROM
    users
WHERE
    age >= 30 
    AND balance >= 1000


SELECT
    *
FROM
    users
WHERE
    balance <= 1000 AND age <= 20;

--나이가 가장 많은 사람
SELECT
    *, MAX(age) --가장 나이 만ㅇ흔 사람
FROM
    users
WHERE
    first_name LIKE "현%"
    AND country LIKE "제주특별자치도";

SELECT
    *, MIN(age)
FROM
    users
WHERE
    last_name LIKE "%박"
    AND age >= 25;

SELECT 
    *, MAX(balance)
FROM
    users
WHERE
    first_name LIKE "%재은"
    OR first_name LIKE "영일";

SELECT
    *, MAX(balance)
FROM
    users
GROUP BY
    country
ORDER BY
    balance DESC;


-- age가 30세 이상이면서, bal age가 30세 이상인 ㅅ사용자들의 ㅍ평균 bal보다 높은 사용자의 정보 조회
SELECT 
    *
FROM 
    users
WHERE 
    age >= 30 
    AND balance > 
    (SELECT AVG(balance) 
        FROM users 
        WHERE age >= 30);