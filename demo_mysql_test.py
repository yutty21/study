import mysql.connector

mydb = mysql.connector.connect(
    host="47.91.245.218",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="root", # 数据库密码
    database ="interface" #数据库名
)


mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE interface")

mycursor.execute("show tables")
for x in mycursor:
  print(x)