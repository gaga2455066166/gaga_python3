# 新增
# connect.zadd('key',{'value1':'score1','value2':'scote2',.....})
# 在name对应的有序集合中添加元素
# 如：
import redis
import time

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

# r.zadd("zset1", 'n1'=11, 'n2'=22)
r.zadd('grade', {'bob': 100, 'mike': 99, 'lucy': 87})
r.zadd("zset1", {'m3': 22, 'm4': 44})
r.zadd("zset2", {'m3': 221, 'm4': 144})
print(r.zcard("zset1"))  # 集合长度
print(r.zcard("zset2"))  # 集合长度
print(r.zrange("zset1", 0, -1))  # 获取有序集合中所有元素
print(r.zrange("zset2", 0, -1, withscores=True))  # 获取有序集合中所有元素和分数2
