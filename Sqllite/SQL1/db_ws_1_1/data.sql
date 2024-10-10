-- Active: 1728527871096@@127.0.0.1@3306
SELECT
    *
FROM
    users;
    

SELECT
    *
FROM 
    users
WHERE --18세미만
    age < 19;

SELECT
    age, phone
FROM
    users
WHERE
    age < 19;