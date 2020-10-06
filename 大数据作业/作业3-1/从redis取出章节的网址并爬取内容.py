import requests
import pymongo
import redis
from lxml import html

connection = pymongo.MongoClient()
db = connection.Chapter6  # 数据库名字
handler = db.white  # 集合名字

client = redis.StrictRedis()

content_list = []  # 批量导入
while client.llen('url_queue') > 0:  # 当数据库中数据的长度大于0，执行
    url = client.lpop('url_queue').decode()
    source = requests.get(url).content

    selector = html.fromstring(source)
    chapter_name = selector.xpath('//div[@class="h1title"]/h1/text()')[0]
    # print(chapter_name) # 章节的标题
    content = selector.xpath('//div[@id="htmlContent"]/p/text()')
    # print(content) # 章节的内容
    content_list.append({'title': chapter_name, 'content': '\n'.join(content)})

handler.insert_many(content_list)  # 获取文本 批量导入


'''
mongo
use Chapter6
db.white.find()
'''
