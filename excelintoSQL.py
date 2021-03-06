import mysql.connector
import xlrd
import sys
from xlrd import xldate_as_datetime
from xlrd import xldate_as_tuple
import json
from datetime import datetime

'''
    连接数据库
    args：db_name（数据库名称）
    returns:db

'''


def mysql_link(de_name):
    try:
        db = mysql.connector.connect(
            host="47.91.245.218",  # 数据库主机地址
            user="root",  # 数据库用户名
            passwd="root", # 数据库密码
            database ="CheckCai" #数据库名
        )
        print("连接数据库成功")
        return db
    except:
        print("could not connect to mysql server")


'''
    读取excel函数
    args：excel_file（excel文件，目录在py文件同目录）
    returns：book
'''


def open_excel(excel_file):
    try:
        book = xlrd.open_workbook(excel_file)  # 文件名，把文件与py文件放在同一目录下
        print(sys.getsizeof(book))
        print("获取execl表成功")
        return book
    except:
        print("open excel file failed!")



'''
    执行插入操作
    args:db_name（数据库名称）
         table_name(表名称）
         excel_file（excel文件名，把文件与py文件放在同一目录下）

'''


def store_to(db_name, table_name, excel_file):
    db = mysql_link(db_name)  # 打开数据库连接
    cursor = db.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor

    book = open_excel(excel_file)  # 打开excel文件
    sheets = book.sheet_names()  # 获取所有sheet表名



    # for sheet in sheets:
    #     print("打开表成功")
    #     sh = book.sheet_by_name(sheet)  # 打开每一张表
    #     row_num = sh.nrows
    #     print(row_num)
    #     list = []  # 定义列表用来存放数据
    #     num = 0  # 用来控制每次插入的数量
    #
    #     '''
    #      sql = "INSERT INTO double (issue, red1, red2, red3, red4, red5, red6, blue,jackpot , first_prize_number, first_prize_bonus,second_prize_number, second_prize_bonus, current_bankroll, prize_date)\
    #         VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #
    #     sql2 = "INSERT INTO `" + table_name + "` (issue, red1, red2, red3, red4, red5, red6, blue,jackpot" \
    #            ", first_prize_number, first_prize_bonus,second_prize_number" \
    #            ", second_prize_bonus, current_bankroll, prize_date) " \
    #            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #
    #     val = [
    #         ('18113','1','6','9','16','25','26','9', '1073781687','11','5895165','208','59175','314160394','2018/9/27'),
    #         ('18112','5','8','18','25','26','31','4','1101702921','11','6090396','154','97356','302328982','2018/9/25')
    #     ]
    #
    #     cursor.executemany(sql2, val)
    #
    #    #cursor.executemany(sql,val)  # 执行sql语句
    #    '''
    #
    #
    #     for i in range(0, row_num-1):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
    #         row_data = sh.row_values(i) # 按行获取excel的值
    #         print(row_data)
    #         value = (int(row_data[0]), int(row_data[1]), int(row_data[2]), int(row_data[3]), int(row_data[4]), int(row_data[5]), int(row_data[6]), int(row_data[7]), int(row_data[8]), int(row_data[9]), int(row_data[10]), int(row_data[11]), int(row_data[12]),int(row_data[13]))
    #         list.append(value)  # 将数据暂存在列表
    #         print(list)
    #         a = int(row_data[0])
    #         #row_data[14] = xldate_as_datetime(row_data[14],0)
    #
    #         num += 1
    #         if (num >= 10):  # 每一万条数据执行一次插入
    #             print("开始写入")
    #             print(sys.getsizeof(list))
    #             #row_data[14] = xldate_as_datetime(row_data[14], 0)
    #             #print(row_data[14])
    #             sql = "INSERT INTO `double` (issue, red1, red2, red3, red4, red5, red6, blue,jackpot , first_prize_number, first_prize_bonus,second_prize_number, second_prize_bonus, current_bankroll) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #             cursor.executemany(sql,list)  # 执行sql语句
    #             num = 0  # 计数归零
    #             list.clear()  # 清空list
    #             print("worksheets: " + sheet + " has been inserted 10 datas!")

    for sheet in sheets:
        print("打开表成功")
        sh = book.sheet_by_name(sheet)  # 打开每一张表
        row_num = sh.nrows
        print(row_num)
        list = []  # 定义列表用来存放数据
        num = 0  # 用来控制每次插入的数量


        for i in range(0, row_num-1):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
            row_data = sh.row_values(i)  # 按行获取excel的值
            value = xldate_as_datetime(row_data[0],0)
            print(value)
            list.append(value)  # 将数据暂存在列表
            print(list)
            # row_data[14] = xldate_as_datetime(row_data[14],0)

            num += 1
            if (num >= 10):  # 每一万条数据执行一次插入
                print("开始写入")
                print(sys.getsizeof(list))
                sql = "INSERT INTO `double` prize_data VALUES %Y-%m-%d"
                cursor.executemany(sql, list)  # 执行sql语句
                num = 0  # 计数归零
                list.clear()  # 清空list
                print("日期表格输入数据库成功")


    print("worksheets: " + sheet + " has been inserted " + str(row_num) + " datas!")
    db.commit()  # 提交
    cursor.close()  # 关闭连接
    db.close()




def from_store(db_name):

    db = mysql_link(db_name)  # 打开数据库连接
    cursor = db.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor

    sql2 = "SELECT * FROM `double`"
    cursor.execute(sql2)
    rows = cursor.fetchall()
    jsonData = []

    for row in rows:
        result = {}
        data = {}
        data['issue'] = row[0]
        data['red1'] = row[1]
        data['red2'] = row[2]
        data['red3'] = row[3]
        data['red4'] = row[4]
        data['red5'] = row[5]
        data['red6'] = row[6]
        data['blue'] = row[7]
        data['Jackpot'] = row[8]
        data['first_prize_number'] = row[9]
        data['first_prize_bonus'] = row[10]
        data['second_prize_number'] = row[11]
        data['second_prize_bonus'] = row[12]
        data['prize_data'] = row[13]
        data['current_bankroll'] =row[14]
        result["data"]= data
        jsonData.append(result)


    print(jsonData)

    cursor.close()  # 关闭连接
    db.close()

    return jsonData

def from_store_1(db_name):

    db = mysql_link(db_name)  # 打开数据库连接
    cursor = db.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor

    sql2 = "SELECT * FROM `double` LIMIT 0,20"
    cursor.execute(sql2)
    rows = cursor.fetchall()
    jsonData = []

    for row in rows:
        result = {}
        data = {}
        data['issue'] = row[0]
        data['red1'] = row[1]
        data['red2'] = row[2]
        data['red3'] = row[3]
        data['red4'] = row[4]
        data['red5'] = row[5]
        data['red6'] = row[6]
        data['blue'] = row[7]
        data['Jackpot'] = row[8]
        data['first_prize_number'] = row[9]
        data['first_prize_bonus'] = row[10]
        data['second_prize_number'] = row[11]
        data['second_prize_bonus'] = row[12]
        data['prize_data'] = row[13]
        data['current_bankroll'] =row[14]
        result["data"]= data
        jsonData.append(result)


    print(jsonData)

    cursor.close()  # 关闭连接
    db.close()

    return jsonData

if __name__ == "__main__":
    double = store_to('CheckCai','double','dateB.xlsx')