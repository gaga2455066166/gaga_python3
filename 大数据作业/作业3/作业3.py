import pymongo
import pymysql
from pymongo import MongoClient


def my_db(table_name):
    coon = pymysql.connect(
        user='root', passwd='123456', host='127.0.0.1', port=3306,
        db='db_python', charset='utf8'
    )
    cur = coon.cursor(cursor=pymysql.cursors.DictCursor)
    sql = 'select * from %s;' % table_name
    cur.execute(sql)
    if sql.strip()[:6].upper() == 'SELECT':
        res = cur.fetchall()
    cur.close()
    coon.close()
    return res


# collection = MongoClient().db_python.test
# collection.insert_one({'name': '王有鋆', 'passwd': '123456'})
# str_one = collection.find_one()
# print(str_one)
# for item in collection.find():
#     print(item)

if __name__ == '__main__':
    print('作业3：')
    collection = MongoClient().db_python

    print('转移student:')
    allrow = my_db('student')
    for myuser in allrow:
        collection.student.insert_one(myuser)
        print(type(myuser))

    print('转移course:')
    allrow = my_db('course')
    for myuser in allrow:
        collection.course.insert_one(myuser)
        print(type(myuser))

    print('转移sc:')
    allrow = my_db('sc')
    for myuser in allrow:
        collection.sc.insert_one(myuser)
        print(type(myuser))
