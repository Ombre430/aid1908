"""
写操作演示
"""
#1连接数据库
import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password="123456",
                     database='szs',
                     charset='utf8')
#生成游标对象（操作数据库，执行sql语句）
cur = db.cursor()

#执行对数据库写操作
try:
    #执行增删改等语句
    # sql = "insert into class1 (name,age,score) values ('恽树月',27,30);"
    # sql = "delete from class1 where name = '恽树月';"
    # sql = "update class1 set sex = 'w' where name = '白晶霜';"

    #从input输入内容传给sql语句
    # name = input("Name:")
    # age = input("Age:")
    # score = input("Score:")
    # sql = "insert into class1 (name,age,score) values (%s,%s,%s)"
    # cur.execute(sql,[name,age,score])

    #executemany 多次执行sql语句
    exe = []
    for i in range(3):
        name = input("Name:")
        age = input("Age:")
        score = input("Score:")
        exe.append((name,age,score))
    sql = "insert into class1 (name,age,score) values (%s,%s,%s);"
    cur.executemany(sql,exe)
except Exception as e:
    db.rollback()#事物回滚
    print(e)

#关闭游标和数据库连接
cur.close()
db.close()