import cx_Oracle

#获取连接对象
# connection = cx_Oracle.connect("username/password@host:port/service_name")
connection = cx_Oracle.connect("agent_user2/123456@172.20.6.22:1521/mpos")

# try:
#     connection = cx_Oracle.connect("agent_user2/123456@172.20.6.22:1521/mpos")
#     print("connection succesfull")
# except:
#     print("connet failed")
#获取游标对象
cursor = connection.cursor()

#执行SQL
SQL = "select * from t_profit_amount where user_id = 50263545"
cursor.execute(SQL)

#获取查询结果
print(cursor.fetchone())

#关闭游标对象
cursor.close()
#关闭连接对象
connection.close()


