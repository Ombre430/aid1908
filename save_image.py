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
                     database='szs',
                     charset='utf8')
#生成游标对象（操作数据库，执行sql语句）
cur = db.cursor()

#执行对数据库写操作

    #executemany 多次执行sql语句
# with open("01.jpg","rb") as f:
#     data = f.read()
#     try:
#         sql = "insert into image values(1,%s,%s)"
#         cur.execute(sql,['01.jpg',data])
#         db.commit()
#     except Exception as e:
#         db.rollback()#事物回滚
#         print(e)

#读取图片
sql = "select filename,img from image where filename = '01.jpg';"
cur.execute(sql)
data = cur.fetchone()
with open("nicai.jpg","wb") as f:
    f.write(data[1])

#关闭游标和数据库连接
cur.close()
db.close()