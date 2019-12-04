import pymysql
from pprint import pprint

db = pymysql.connect(host='localhost',
                             user='root',
                             password='--',
                             db='cza_test',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()

def execute_sql(sql):
    cursor.execute(sql)
    results = cursor.fetchall()
    pprint(results)

sql1 = """
insert into students (test_datetime) values
    ('2019.12.13'),
    ('2019-1-6 01:12:25'),
    ('2019-12-01 14:14:14')
"""
# execute_sql(sql1)

sql2 = """
select * from students
"""
execute_sql(sql2)

sql3 = """
select * from students where test_datetime > '2019.05.05'
"""# well, i guess we can
execute_sql(sql3)