USE beinex_SQL;
CREATE TABLE Employee_table_kshitij(emp_id int primary key, First_Name VARCHAR(20) not null, Last_Name varchar(20), age INT, email_id VARCHAR(50), city VARCHAR(20), state VARCHAR(30), Date_Of_Birth DATE, phone INT(10), Date_of_Joining DATE);

-- INSERT
INSERT INTO Employee_table_kshitij VALUES(1, 'Kshitij', 'Tiwari', 22, 'k@mail.com', 'bhilai', 'chhattisgarh', '2000-10-09', 0123456789, '2022-10-14');
INSERT INTO Employee_table_kshitij VALUES(5, 'AMAN', 'nagi', 23, 'aman@mail.com', 'nagpur', 'Maharashtra', '1999-12-09', 0123456789, '2021-10-19');
INSERT INTO Employee_table_kshitij VALUES(2, 'PAVAN', 'gangu', 24, 'pavan@mail.com', 'ambala', 'Haryana', '1998-05-01', 0123456789, '2020-11-14');
INSERT INTO Employee_table_kshitij VALUES(3, 'JERIN', 'raju', 21, 'jerin@mail.com', 'agra', 'Uttar Pradesh', '2001-03-25', 0123456789, '2023-10-14');
INSERT INTO Employee_table_kshitij VALUES(6, 'PRANAV', 'Tiwari', 22, 'pranac@mail.com', 'durg', 'chhattisgarh', '2000-08-18', 0123456789, '2022-12-11');
INSERT INTO Employee_table_kshitij VALUES(8, 'DEV', 'jaiswal', 22, 'dev@mail.com', 'indore', 'Madhya pradesh', '2000-11-19', 0123456789, '2022-05-18');
INSERT INTO Employee_table_kshitij VALUES(9, 'ANANYA', 'tiwari', 25, 'ananya@mail.com', 'kochi', 'kerala', '1995-12-14', 0123456789, '2022-02-04');
INSERT INTO Employee_table_kshitij VALUES(7, 'janvi', 'pathak', 20, 'janvi@mail.com', 'delhi', 'delhi', '2002-04-29', 0123456789, '2022-07-13');
INSERT INTO Employee_table_kshitij VALUES(4, 'rashi', 'thomas', 30, 'rashi@mail.com', 'mumbai', 'Maharashtra', '1990-10-29', 0123456789, '2022-09-24');
INSERT INTO Employee_table_kshitij VALUES(10, 'Kruti', 'rajput', 26, 'kruti@mail.com', 'raipur', 'chhattisgarh', '1994-02-10', 0123456789, '2022-02-05');

-- SELECT
SELECT * FROM Employee_table_kshitij;

-- DISTINCT
SELECT DISTINCT state FROM Employee_table_kshitij;

-- WHERE
SELECT * FROM Employee_table_kshitij
 WHERE Last_Name = 'tiwari';

-- AND
SELECT * FROM Employee_table_kshitij
 WHERE Last_Name = 'tiwari' AND age>22;

-- OR 
SELECT * FROM Employee_table_kshitij
 WHERE Date_of_Joining > '2022-10-10' OR city = 'delhi';

-- NOT
SELECT * FROM Employee_table_kshitij
 WHERE Last_Name NOT IN ('tiwari','nagi');

-- ORDER BY
SELECT * FROM Employee_table_kshitij
 ORDER BY age DESC;

-- NULL
SELECT * FROM Employee_table_kshitij
 WHERE city IS NULL;
 
-- NOT NULL
SELECT * FROM Employee_table_kshitij
 WHERE age IS NOT NULL;

-- UPDATE 
UPDATE Employee_table_kshitij
   SET emp_id = 3134668702
 WHERE age = 30;

-- DELETE
DELETE FROM Employee_table_kshitij
 WHERE age=31;

-- LIMIT
SELECT * FROM Employee_table_kshitij
 LIMIT 5;
 
-- COUNT
SELECT COUNT(*) AS cols_num
  FROM Employee_table_kshitij;

-- IN
SELECT * FROM Employee_table_kshitij
 WHERE state IN ('delhi','haryana');

-- BETWEEN
SELECT * FROM Employee_table_kshitij
 WHERE Date_Of_Birth BETWEEN '2000-01-01' AND '2002-10-10';
 
-- LIKE
SELECT First_Name, Last_Name FROM Employee_table_kshitij
 WHERE Last_Name LIKE '%ri';
 
-- GROUP BY
SELECT COUNT(city) AS city_row , state FROM Employee_table_kshitij
 GROUP BY state;
 
-- HAVING
SELECT COUNT(city) AS city_row , state FROM Employee_table_kshitij
 GROUP BY state
HAVING COUNT(city)>1;
	
-- AS - Alias
SELECT phone FROM Employee_table_kshitij AS mobile;

-- CASE WHEN
SELECT state,
  (CASE  Date_of_Joining
	WHEN '2020-10-10' THEN 'Pandemic'
    ELSE 'hello there'
  END) AS pandemic_year
  FROM Employee_table_kshitij;

-- MIN
SELECT MIN(age) AS min_age FROM Employee_table_kshitij;

-- MAX
SELECT MAX(Date_of_Joining) AS max_doj FROM Employee_table_kshitij;

-- SUM
SELECT SUM(age) AS sum_age FROM Employee_table_kshitij;

-- AVG
SELECT AVG(age) AS avg_age FROM Employee_table_kshitij;

-- LEFT JOIN
SELECT Employee_table_kshitij.First_Name , Student_table.Last_Name
  FROM Employee_table_kshitij
  LEFT JOIN Student_table ON Employee_table_kshitij.First_Name = Student_table.First_Name;

-- RIGHT JOIN
SELECT Employee_table_kshitij.First_Name , Student_table.Last_Name
  FROM Employee_table_kshitij
 RIGHT JOIN Student_table ON Employee_table_kshitij.First_Name = Student_table.First_Name;

-- INNER JOIN
SELECT Employee_table_kshitij.First_Name , Student_table.Last_Name
  FROM Employee_table_kshitij
INNER JOIN Student_table ON Employee_table_kshitij.First_Name = Student_table.First_Name;

-- DROP
ALTER TABLE Employee_table_kshitij
DROP COLUMN phone;

-- Length
SELECT LENGTH(First_Name) FROM Employee_table_kshitij;

-- Trim
SELECT TRIM(' skjf asnf,wem  ');

-- Concat
SELECT CONCAT("SQL ", "Tutorial ", "is ", "fun!") AS ConcatenatedString; 

-- Upper 
SELECT UPPER("SQL Tutorial is FUN!"); 
-- Lower
SELECT LOWER("SQL Tutorial is FUN!"); 
-- Abs
SELECT ABS(-0.666);
-- Round
SELECT ROUND(1324.50);
-- Ceil
SELECT ceil(11.4);
-- Floor
SELECT FLOOR(1234.3);

-- Sign
SELECT SIGN(-13213.4);

-- Mod
SELECT MOD(-123, 4);

-- Current_date
SELECT current_date() + 4;

-- Extract
SELECT extract(SECOND FROM '2020-12-20 02:10:47');

-- Coalesce
SELECT COALESCE('asdfsa', NULL, 233);

#Greatest
SELECT GREATEST(3, 20, 45,75);
-- -- Least
SELECT LEAST(3, 20, 45,75);
-- -- Isnull
SELECT isnull('');