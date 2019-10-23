"""
创建数据dict使用utf8编码
创建表words分为三个字段
id words mean
将dict.txt中所有单词存入
"""
#1连接数据库
import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password="123456",
                     database='dict',
                     charset='utf8')
#生成游标对象（操作数据库，执行sql语句）
cur = db.cursor()

#执行对数据库写操作
try:
    #executemany 多次执行sql语句
    f = open("dict.txt")
    for i in f:
        word = i.split(" ",1)[0]
        mean = i.split(" ",1)[1].strip()
        sql = "insert into words (word,mean) values (%s,%s);"
        cur.execute(sql,[word,mean])
    db.commit()
except Exception as e:
    db.rollback()#事物回滚
    print(e)

#关闭游标和数据库连接
cur.close()
db.close()