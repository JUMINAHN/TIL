-- Active: 1728540452236@@127.0.0.1@3306
SELECT
    *
FROM
    users
WHERE
    first_name LIKE '하%'; -- %는 끝나는 것임 == 따라서 반대로 진행함

SELECT
    *
FROM
    users
WHERE
    phone LIKE '%555';


SELECT
    *
FROM
    users
WHERE
    country LIKE '경상%';

SELECT
    *
FROM
    users
WHERE --따로 써야한다!
    (country Like '경%'
    AND
    country LIKE "__남%")
    OR
    (country LIKE '충%'
    AND
    country LIKE "__남%")
-- WHERE
--     [country LIKE '경%']
--     OR
--     [country LIKE '충%']
--     AND --세번째 글자가 남
--     [country LIKE] ;