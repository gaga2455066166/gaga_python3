import json
import redis
import pymysql


def my_db(table_name):
    coon = pymysql.connect(
        user='root', passwd='123456', host='127.0.0.1', port=3306,
        db='db_python', charset='utf8'
    )
    cur = coon.cursor(cursor=pymysql.cursors.DictCursor)  # 建立游标，指定cursor类型返回的是字典
    # cur = coon.cursor()
    sql = 'select * from %s;' % table_name
    cur.execute(sql)
    if sql.strip()[:6].upper() == 'SELECT':
        res = cur.fetchall()
    cur.close()
    coon.close()
    return res


def output_all(name):
    print(r.hgetall('mytab'))
    for rows in r.hscan_iter('mytab'):
        print(json.loads(rows[0]))
        print(json.loads(rows[1]))


# 取出所有的键值对
# hgetall(name)
# 获取name对应hash的所有键值
r = redis.Redis()  # 端口号默认6379

allrow = my_db('mytab')
# 关系数据库表插入redis
for myuser in allrow:
    # print(date)
    key = myuser.get('id')
    # print(key)
    value = json.dumps(myuser)
    # print(value)
    r.hset('mytab', key, value)

output_all('mytab')
# 查询 输出id为2的name和password
id = 2
jrow = r.hget('mytab', id)
row = json.loads(jrow)
print(row['id'], row['name'], row['passwd'])

# 修改 id为2的name和password
id = 2
jrow = r.hget('mytab', id)
row = json.loads(jrow)
row['name'] = 'changehere'
r.hset('mytab', id, json.dumps(row))
output_all('mytab')

# 删除 key id为2的这项
id = 2
r.hdel('mytab', id)  # 删除一个键值对
output_all('mytab')
