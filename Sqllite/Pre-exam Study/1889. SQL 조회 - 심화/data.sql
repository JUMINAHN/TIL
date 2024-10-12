SELECT
  *
FROM
  tracks
WHERE
  Name LIKE "%LOVE%"; --양 옆으로 %%를 하면 love가 포함된 전체를 다룰 수 있음

  -- Name LIKE "%Love" --love로 끝나는 것
  -- OR Name LIKE "Love%"; --love를 포함한 데이터 %
  -- -- LIKE "love%"는 love로 시작하는 데이터
  -- -- LIKE "love"는 love만 추출
  -- -- love가 모두 있으려면? 

SELECT
  *
FROM
  tracks
WHERE
  GenreId = 1
  AND Milliseconds >= 300000
ORDER BY
  UnitPrice DESC;

-- genreid와 각 그룹별 데이터 수 -> 그룹을 genreid로 했으니까
-- 각 그룹별 데이터 수 추출
SELECT
  GenreId, COUNT(GenreId) AS 'TotalTracks' --그룹별 데이터 수
FROM
  tracks
GROUP BY 
  GenreId;

-- 그룹별 OOOO :: 이 말은 즉 그룹화된 -> sth을 구해라
SELECT --그룹별 unitprice의 총합
  GenreId, --그룹화하는 친구들 뽑고
  -- 그 그룹의 UnitPrice
  SUM(UnitPrice) AS 'TotalPrice' --genreid로 묶여있으니까 => 여기에 대한 unitprice가 매겨질 것 => 조회하는 것
FROM
  tracks
GROUP BY
  GenreId --이걸로 그릅화했다
HAVING
  TotalPrice >= 100;--위에서 정의한 개념으로 조건 나누기   