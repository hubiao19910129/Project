import pymysql

#创建连接
connection = pymysql.connect("172.20.2.126",
                             "sp_user",
                             "testjob",
                             "sp_db")
print("connection succesfull!")

#创建游标对象sp_db
cursor = connection.cursor()

#执行方法SQL
sql = "select * from table_book"
cursor.execute(sql)

#获取执行结果
result = cursor.fetchall()
print(result)

#关闭游标对象
cursor.close()
#关闭连接对象
connection.close()