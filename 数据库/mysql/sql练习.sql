-- sql practice

-- SELECT
-- INSERT
-- UPDATE
-- DELETE
-- WHERE <where_condition>
-- GROUP BY <group_by_list>
-- HAVING <having_condition>
-- DISTINCT <select_list>
-- ORDER BY <order_by_condition>
-- LIMIT <limit_number> OFFSET <offset_number>
-- SUM
-- AVG
-- MAX
-- MIN

-- INNER JOIN 只返回同时存在于两张表的行数据
-- RIGHT OUTER JOIN 返回右表都存在的行
-- LEFT OUTER JOIN 返回左表都存在的行
-- FULL OUTER JOIN 返回两张表的所有记录

/* students
id	class_id	name	gender	score
1	1	        小明	M	    90
2	1	        小红	F	    95
3	1	        小军	M	    88
4	1	        小米	F	    73
5	2	        小白	F	    81
6	2	        小兵	M	    55
7	2	        小林	M	    85
8	3	        小新	F	    91
9	3	        小王	M	    89
10	3	        小丽	F	    88
*/

/* classes
id	name
1	一班
2	二班
3	三班
4	四班
*/


-- SELECT
SELECT * FROM students;
SELECT COUNT(*) sum FROM students;
SELECT class_id std_id FROM students WHERE gender = 'M';
SELECT * FROM students ORDER BY score DESC; -- why not not work. must appoint column?
SELECT * FROM students LIMIT 3 OFFSET 0;
SELECT CEILING(COUNT(*)/3) FROM students;
SELECT COUNT(*) FROM students GROUP BY gender;
SELECT students.id students_id, classes.id classes_id FROM students, classes;
SELECT *
FROM students s
INNER JOIN classes c
ON s.id = c.id;


-- INSERT
INSERT INTO students (class_id, name, gender, score) VALUES (1, 'cza', 'M', 24);
INSERT INTO students (class_id, name, gender, score) VALUES
(1, 'cza', 'M', 24),
(1, 'cza', 'M', 24);


--UPDATE
UPDATE students SET name = 'cza', score = 100 WHERE id = 1;
UPDATE students SET score=score+1 WHERE score < 98;
UPDATE students SET score = 59;


--DELETE
DELETE FROM students WHERE name = 'cza';
DELETE FROM students;
