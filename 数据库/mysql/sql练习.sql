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


-- SELECT
SELECT * FROM students;
SELECT COUNT(*) sum FROM students;
SELECT class_id std_id FROM students WHERE gender = 'M';
SELECT * FROM students ORDER BY score DESC; -- ??? why not not work
