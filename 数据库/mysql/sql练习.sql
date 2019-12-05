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

-- INNER JOIN ֻ����ͬʱ���������ű��������
-- RIGHT OUTER JOIN �����ұ����ڵ���
-- LEFT OUTER JOIN ����������ڵ���
-- FULL OUTER JOIN �������ű�����м�¼

/* students
id	class_id	name	gender	score
1	1	        С��	M	    90
2	1	        С��	F	    95
3	1	        С��	M	    88
4	1	        С��	F	    73
5	2	        С��	F	    81
6	2	        С��	M	    55
7	2	        С��	M	    85
8	3	        С��	F	    91
9	3	        С��	M	    89
10	3	        С��	F	    88
*/

/* classes
id	name
1	һ��
2	����
3	����
4	�İ�
*/

-- STRUCT OF TABLE
DESC students;
SHOW CREATE TABLE students;
ALTER TABLE students ADD COLUMN birth VARCHAR(20) NOT NULL;
ALTER TABLE students CHANGE COLUMN birth birthday VARCHAR(30) NOT NULL;
ALTER TABLE students DROP COLUMN birthday;

-- EASE SQL
REPLACE INTO students (id, class_id, name, gender, score) VALUES (1, 1, 'cza', 'M', 24);  -- insert one record or replace old one if exist
INSERT INTO students (id, class_id, name, gender, score) VALUES (1, 1, 'cza', 'M', 24) ON DUPLICATE KEY UPDATE name='cza', gender='F', score=22;  -- insert one record or update it if exist;
INSERT IGNORE INTO students (id, class_id, name, gender, score) VALUES (1, 1, 'cza', 'M', 24);
CREATE TABLE students_fast SELECT * FROM students WHERE class_id=1;


-- SELECT
SELECT * FROM students;
SELECT COUNT(*) sum FROM students;
SELECT class_id std_id FROM students WHERE gender = 'M';
SELECT * FROM students ORDER BY score DESC; -- why not not work. must appoint column?
SELECT * FROM students LIMIT 3 OFFSET 0;
SELECT CEILING(COUNT(*)/3) FROM students;
SELECT COUNT(*) FROM students GROUP BY gender;
SELECT COUNT(DISTINCT name) FROM students WHERE score>90;  -- by this way, you can filter by WHERE first, then get the num of all records
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


DROP database if EXISTS cza_test;
CREATE database cza_test;
use cza_test;
CREATE TABLE students (
    `id` bigint NOT NULL auto_increment,
    `class_id` bigint NOT NULL,
    `name` varchar(10) NOT NULL,
    `gender` varchar(5) NOT NULL,
    `score` int NOT NULL,
    primary key (`id`),
    key `idx_name` (`name`),
    unique key `idx_name` (`name`),
) engine=innodb default charset=utf8;


mysql -u root -p
mysql -h 127.0.0.1 -u root -p
