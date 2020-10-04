import redis
import time

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

r.hset("hash1", "k1", "v1")
r.hset("hash1", "k2", "v2")
print(r.hkeys("hash1"))  # 取hash中所有的key
print(r.hget("hash1", "k1"))  # 单个取hash的key对应的值
print(r.hmget("hash1", "k1", "k2"))  # 多个取hash的key对应的值

#  批量增加（取出）
#
# hmset(name, mapping)
# 在name对应的hash中批量设置键值对
# 参数：
# name，redis的name
# mapping，字典，如：{‘k1’:’v1’, ‘k2’: ‘v2’}
# 如：
r.hmset("hash2", {"k2": "v2", "k3": "v3"})

print(r.hget("hash2", "k2"))  # 单个取出"hash2"的key-k2对应的value
print(r.hmget("hash2", "k2", "k3"))  # 批量取出"hash2"的key-k2 k3对应的value --方式1
print(r.hmget("hash2", ["k2", "k3"]))  # 批量取出"hash2"的key-k2 k3对应的value

# hlen(name)
# 获取name对应的hash中键值对的个数
print(r.hlen("hash1"))

# 获取name对应的hash中所有的key的值
print(r.hkeys("hash1"))

# 获取name对应的hash中所有的value的值
print(r.hvals("hash1"))
# 判断成员是否存在（类似字典的in）
# hexists(name, key)
# 检查name对应的hash是否存在当前传入的key
print(r.hexists("hash1", "k4"))  # False 不存在
print(r.hexists("hash1", "k1"))  # True 存在

# 删除键值对
# hdel(name,*keys)
# 将name对应的hash中指定key的键值对删除
print(r.hgetall("hash1"))
r.hset("hash1", "k2", "v222")  # 修改已有的key k2
r.hset("hash1", "k11", "v1")  # 新增键值对 k11
r.hdel("hash1", "k1")  # 删除一个键值对
print(r.hgetall("hash1"))

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
# Hash
# mset
# 批量设置值
# 如：
r.mset({'k1': 'v1', 'k2': 'v2'})
# r.mset(k1="v1", k2="v2") # 这里k1 和k2 不能带引号 一次设置对个键值对
print(r.mget("k1", "k2"))  # 一次取出多个键对应的值
print(r.mget("k1"))
# mget
# mget(keys, *args)
# 批量获取
# 如：
print(r.mget('k1', 'k2'))
print(r.mget(['k1', 'k2']))
print(r.mget("fruit", "fruit1", "fruit2", "k1", "k2"))  # 将目前redis缓存中的键对应的值批量取出来
# 列表
r.lpush("list1", 11, 22, 33)
print(r.lrange('list1', 0, -1))
# 保存顺序为: 33,22,11
# 扩展：
r.rpush("list2", 11, 22, 33)  # 表示从右向左操作
print(r.lrange('list2', 0, -1))
print(r.llen("list2"))  # 列表长度
print(r.lrange("list2", 0, 3))  # 切片取出值，范围是索引号0-3

# 删除并返回
# lpop(name)
# 在name对应的列表的左侧获取第一个元素并在列表中移除，返回值则是第一个元素
# 更多：
# rpop(name) 表示从右向左操作
r.lpop("list2")  # 删除列表最左边的元素，并且返回删除的元素
print(r.lrange("list2", 0, -1))
r.rpop("list2")  # 删除列表最右边的元素，并且返回删除的元素
print(r.lrange("list2", 0, -1))

# 集合set操作
#
# sadd
#
# 复制代码
# 新增
# sadd(name, values)
# name对应的集合中添加元素
r.sadd("set1", 33, 44, 55, 66)  # 往集合中添加元素
print(r.scard("set1"))  # 集合的长度是4
print(r.smembers("set1"))  # 获取集合中所有的成员
