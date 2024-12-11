CREATE TABLE zoo(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INTEGER NOT NULL,
  height INTEGER NOT NULL,
  age INTEGER NOT NULL
);

INSERT INTO
  zoo (name, eat, weight, height, age)
VALUES
  ('Lion', 'Meat', 200, 120, 5),
  ('Elephant', 'Plants', 5000, 300, 15),
  ('Giraffe', 'Leaves', 1500, 550, 10),
  ('Monkey', 'Fruits', 50, 60, 8);

SELECT
  *
FROM
  zoo