-- Active: 1728528126917@@127.0.0.1@3306
SELECT
    *
FROM
    users
WHERE
    age < 19
ORDER BY
    age DESC;
    
SELECT
    last_name, age
FROM
    users
WHERE
    age < 19
ORDER BY
    last_name, age DESC

--중복 제외
SELECT DISTINCT
    last_name, age
FROM
    users
WHERE
    age < 19
ORDER BY
    last_name, age DESC