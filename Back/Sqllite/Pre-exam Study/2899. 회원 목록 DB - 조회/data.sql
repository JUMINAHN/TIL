-- Active: 1728783501886@@127.0.0.1@3306
SELECT
  *
FROM
  users;

SELECT
  *
FROM
  users
WHERE
  age < 18;

SELECT
  age, phone --age와 phone의 필드만 조회
FROM
  users
WHERE
  age < 18;