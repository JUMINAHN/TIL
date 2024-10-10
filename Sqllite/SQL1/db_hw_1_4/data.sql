-- Active: 1728526628954@@127.0.0.1@3306

SELECT
    *
FROM
    tracks
WHERE
    Name LIKE "%Love";

SELECT
    *
FROM
    tracks
WHERE
    GenreId LIKE 1
    AND
    Milliseconds >= 300000 -- and안해도되나? keep
ORDER BY
    UnitPrice DESC;

-- 그룹화
SELECT
    --*,
    GenreId,
    COUNT(GenreId) AS "TotalTracks"
FROM
    tracks
GROUP BY
    GenreId;

SELECT
    GenreId,
    SUM(UnitPrice) AS "TotalPrice" --100개이상인 데이터만
FROM
    tracks
-- WHERE
--     "TotalPrice" >= 100
GROUP BY
    GenreId
HAVING
    "TotalPrice" >= 100;
