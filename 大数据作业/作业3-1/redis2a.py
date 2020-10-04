import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
info = {"Sname": "李勇", "Sex": "male", "Age": "23"}
r.hmset("Student:95001", info)
r.hmset("Course:123001", {"Cname": "Math", "CCredit": 2.0})
r.hmset("SC:2015001:123001", {"Score": 86})


# r.hset("hash1", "k2", "v2")
# print(r.hkeys("hash1")) # 取hash中所有的key
# print(r.hget("hash1", "k1"))    # 单个取hash的key对应的值
# print(r.hmget("hash1", "k1", "k2")) # 多个取hash的key对应的值

def main():
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
    r = redis.StrictRedis(connection_pool=pool)
    r.set('Student:95001:Sname', '李勇')
    r.set('Course:8:Cname', '数据库')
    r.set('SC:95001:1:Grade', 92)
    r.set('Course:8:Cname', '算法')
    r.set('Course:8:Ccredit', 4)
    # set SC:95001:1:Grade 92 set Course:8:Cname 算法 set Course:8:Ccredit 4
    print(r.get("Course:8:Cname").decode())
    r.delete('Course:8:Cname')
    print(r.get("Course:8:Cname"))

    r.set('李勇', '95001')
    r.set('数学', '1')
    sid = r.get("李勇").decode()
    cid = r.get("数学").decode()
    print('aa:', r.get('SC:95001:1:Grade').decode())
    score = r.get(f'SC:{sid}:{cid}:Grade').decode()
    print(score)


if __name__ == '__main__':
    main()
