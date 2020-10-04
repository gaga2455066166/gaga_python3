import redis
import time

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)


def dayMusic():
    r.zadd('rank：20191101', {'停格': 98000, '绿色': 54000, '你的酒馆对我打了烊': 20000, '最好的朋友': 15000})
    r.zadd('rank：20191102', {'停格': 98000, '绿色': 54000, '你的酒馆对我打了烊': 20000, '9420': 45000})
    r.zadd('rank：20191103', {'隐形的翅膀': 30000, '阴天快乐': 58000, '9420': 79000, '该死的温柔': 46000})
    r.zadd('rank：20191104', {'阴天快乐': 12321, '停格': 98000, '绿色': 54000, '你的酒馆对我打了烊': 20000, '红豆': 78200})
    r.zadd('rank：20191105', {'最好的朋友': 15000, '停格': 98000, '绿色': 54000, '你的酒馆对我打了烊': 20000, '七友': 78900})
    r.zadd('rank：20191106', {'停格': 45000, '绿色': 56000, '你的酒馆对我打了烊': 96000})
    r.zadd('rank：20191107', {'隐形的翅膀': 28000, '阴天快乐': 68000, '9420': 78500})


# AGGREGATE

# 使用 AGGREGATE 选项，你可以指定并集的结果集的聚合方式。
# 默认使用的参数 SUM ，可以将所有集合中某个成员的 score 值之 和 作为结果集中该成员的 score 值；使用参数 MIN ，
# 可以将所有集合中某个成员的 最小 score 值作为结果集中该成员的 score 值；而参数 MAX 则是将所有集合中某个成员的
# 最大 score 值作为结果集中该成员的 score 值。
def weekMusic():
    r.zunionstore("weekmusic:weekmusic01", (
        "rank：20191101", "rank：20191102", "rank：20191103", "rank：20191104", "rank：20191105", "rank：20191106",
        "rank：20191107"))  # ,aggregate="MIN"


if __name__ == '__main__':
    dayMusic()
    weekMusic()
    print(r.zrevrange("weekmusic:weekmusic01", 0, -1, withscores=True))
