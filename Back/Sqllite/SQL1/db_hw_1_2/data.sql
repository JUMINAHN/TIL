-- Active: 1728526179034@@127.0.0.1@3306
SELECT
    *
FROM
    tracks;

SELECT
    Name, Milliseconds, UnitPrice
FROM
    tracks;

SELECT 
    *
FROM
    tracks
WHERE
    GenreID LIKE 1; --확인 필요

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