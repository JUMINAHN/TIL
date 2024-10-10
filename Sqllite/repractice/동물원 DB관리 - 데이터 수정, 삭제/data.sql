--열 추가
ALTER TABLE
  zoo
ADD COLUMN
  species TEXT ;

-- 데이터 한개만 수정 불가능한가? == data접근했던 것처럼 == Updates -> 레코드 수정
UPDATE
  zoo
SET
  species = "Panthera leo"
WHERE
  name="Lion";

UPDATE
  zoo
SET
  species = "Loxodonta africana"
WHERE
  name="Elephant";

UPDATE
  zoo
SET
  species = "Giraffa camelopardalis"
WHERE
  name="Giraffe";

UPDATE
  zoo
SET
  species = "Cebus capucinus"
WHERE
  name="Monkey";

--height 값을 2.54가 곱해진 값으로 수정
UPDATE
  zoo
SET
  height = height * 2.54; --이게맞다

SELECT
  *
FROM
  zoo