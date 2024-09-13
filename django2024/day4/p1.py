import pymysql

def connectbd():
    connect = pymysql.Connect(
        host='localhost',port=3306,
        user='root' ,password='root',
        db='mobiles', charset='utf8')
    print('connected successfully')
    return connect
connection = connectbd()
connection.close()
print('succcessfully closed')