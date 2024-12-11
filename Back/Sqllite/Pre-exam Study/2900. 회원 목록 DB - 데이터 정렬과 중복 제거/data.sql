-- Active: 1728783798367@@127.0.0.1@3306
SELECT
  * --유저를 2. 유저를 나타냄 
FROM
  users --유저를 2.
WHERE --OO미만인 유저
  age < 18  -- 특정 조건의 1.
ORDER BY
  age DESC; -- 내림차순 기준


SELECT
  last_name, age --특정 필드만 출력하되, ==특정 필드
FROM
  users
WHERE
  age < 18 --age가 18세 미만인 == 특정 조건
ORDER BY
  last_name, age DESC --네임이 같은 경우 > age기준으로 내림차순

--상기와 동일한 조회를 하되,
SELECT DISTINCT--동일한 중복 데이터를 제외하고 조회
  last_name, age
FROM
  users
WHERE
  age < 18
ORDER BY
  last_name, age DESC; 
