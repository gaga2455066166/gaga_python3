import json

import pymysql
import redis


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


if __name__ == '__main__':
    print('redis作业：')
    redis_conn = redis.Redis(host='127.0.0.1', port=6379)

    print('转移student:')
    allrow = my_db('student')
    for myuser in allrow:
        key = myuser.get('s_no')
        value = json.dumps(myuser)
        redis_conn.hset('student', key, value)

    print('转移course:')
    allrow = my_db('course')
    for myuser in allrow:
        key = myuser.get('c_no')
        value = json.dumps(myuser)
        redis_conn.hset('course', key, value)

    print('转移sc:')
    allrow = my_db('sc')
    for myuser in allrow:
        key = myuser.get('sc_sno')
        value = json.dumps(myuser)
        redis_conn.hset('sc', key, value)

pass
