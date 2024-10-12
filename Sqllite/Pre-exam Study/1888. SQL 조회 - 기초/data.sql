-- Active: 1728740926409@@127.0.0.1@3306
--tracks의 모든 테이블 조회
SELECT 
  *
FROM 
  tracks;

SELECT
  Name, 
  Milliseconds, 
  UnitPrice
FROM
  tracks;

SELECT
  *
FROM
  tracks
WHERE
  GenreId = 1;

SELECT
  *
FROM
  tracks
ORDER BY
  Name;

SELECT
  *
FROM
  tracks
LIMIT
  10;