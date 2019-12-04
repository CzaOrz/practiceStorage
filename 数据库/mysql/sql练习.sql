-- sql practice

-- SELECT
-- FROM <left_table>
-- ON <join_condition>
-- WHERE <where_condition>
-- GROUP BY <group_by_list>
-- HAVING <having_condition>
--DISTINCT <select_list>
--ORDER BY <order_by_condition>
--LIMIT <limit_number>

-- INNER JOIN只返回同时存在于两张表的行数据
-- RIGHT OUTER JOIN返回右表都存在的行
-- LEFT OUTER JOIN则返回左表都存在的行
-- FULL OUTER JOIN 它会把两张表的所有记录全部选择出来

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