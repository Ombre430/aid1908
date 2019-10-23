"""
使用数据库支持登录注册
注册：输入信息--》存储到数据库
user:    id   name（不能重复）   passwd
登录：输入信息 --》 通过数据库查询比对
"""
#1连接数据库
import pymysql

def enrollment(cur,name,passwd):
    sql = "select count(1) num from user where name = %s;"
    cur.execute(sql,name)
    data = cur.fetchone()
    if data[0] == 0:
        try:
            sql = "insert into user(name,passwd) values(%s,%s)"
            cur.execute(sql,[name,passwd])
            db.commit()
        except Exception as e:
            db.rollback()#事物回滚
            print(e)
    else:
        return print("该用户已存在")

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password="123456",
                     database='szs',
                     charset='utf8')
#生成游标对象（操作数据库，执行sql语句）
cur = db.cursor()

while True:
    name = input('Name:')
    if not name:
        break
    passwd = input('Passwd:')
    enrollment(cur, name, passwd)
#关闭游标和数据库连接
cur.close()
db.close()