import redis
from redis import StrictRedis


def main():
    # r = redis.StrictRedis(host='127.0.0.1', port=6379)
    # r = redis.StrictRedis()
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
    r = redis.StrictRedis(connection_pool=pool)
    r.set('mykey', 'nihao张')
    print(r.get('mykey').decode())
    r.set('mykey', 'nihao张刘')
    print(r.get('mykey').decode())
    print(r.get('foo'))  # 不存在返回None

    r.set("name", "zhangsan")
    r.setrange("name", 1, "z")
    print(r.get("name"))  # 输出:zzangsan
    r.setrange("name", 6, "zzzzzzz")
    print(r.get("name"))  # 输出:zzangszzzzzzz

    r.set("name", "zhangsan")
    print(r.getrange("name", 0, 3))  # 输出:zhan

    try:
        # 添加键name，值为itheima
        result = r.set('name', 'xiaoming')

        # 输出响应结果，如果添加成功则返回True，否则返回False
        print(result)
    except Exception as e:
        print(e)

    try:
        # 创建StrictRedis对象，与redis服务器建⽴连接
        sr = StrictRedis()

        # 设置键name的值，如果键已经存在则进⾏修改，如果键不存在则进⾏添加
        result = sr.delete('name')

        # 输出响应结果，如果删除成功则返回受影响的键数，否则则返回0
        print(result)

    except Exception as e:
        print(e)
    try:
        # 创建StrictRedis对象，与redis服务器建⽴连接
        sr = redis.StrictRedis()

        # 获取键name的值
        result = sr.get('name')

        # 输出键的值，如果键不存在则返回None
        print(result)

    except Exception as e:
        print(e)

    try:
        # 创建StrictRedis对象，与redis服务器建⽴连接
        sr = redis.StrictRedis()

        # 设置键name的值，如果键已经存在则进⾏修改，如果键不存在则进⾏添加
        # 在客户端执行config set stop-writes-on-bgsave-error no
        result = sr.set('name', 'xiaoming')

        # 输出响应结果，如果操作成功则返回True，否则返回False
        print(result)

    except Exception as e:
        print(e)

    try:
        # 创建StrictRedis对象，与redis服务器建⽴连接
        sr = redis.StrictRedis()

        # 获取所有的键
        result = sr.keys()

        # 输出响应结果，所有的键构成⼀个列表，如果没有键则返回空列表
        print(result)

    except Exception as e:
        print(e)
    r.lpush('list_name', 2)
    r.lpush('list_name', 3, 4, 5)
    print(r.lrange('list_name', 0, -1))  # 输出：['5', '4', '3', '2']


# delete(*names)，根据name删除任意redis数据类型
# exists(name)，检测name是否存在，返回True或False
# keys(pattern='*')，根据* ？等通配符匹配获取redis的name
# r.delete('mykey')

if __name__ == '__main__':
    main()
