-- Active: 1728784234670@@127.0.0.1@3306
SELECT
  * --그냥 단순 사용자 정보 조회
FROM
  users
WHERE
  first_name LIKE '하%'; --하로 시작

SELECT
  * --사용자들의 정보
FROM
  users
WHERE
  phone LIKE '%555'; --555로 끝남
  

SELECT
  *
FROM
  users
WHERE
  country LIKE '경상%'; --경상으로 시작하는 사용자들의 정보

SELECT
  *
FROM
  users
WHERE
  (country LIKE '경%' OR country LIKE '충%')
  AND country LIKE '__남%'; --남의 키워드가 조회되지 않음 == 방금은 단순 남, 그리고 세번째가 남이고 그 뒤에 조건 유의
  


  -- 
  -- AND country LIKE '__남';
-- WHERE --A또는 B이고, X인 경우 -> AX, BX로 표기
--   (country LIKE '경%' AND country LIKE '__남')
--   OR (country LIKE '충%' AND country LIKE '__남');