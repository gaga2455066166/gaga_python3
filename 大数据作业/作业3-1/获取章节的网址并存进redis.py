import requests
from lxml import html
import redis

client = redis.StrictRedis()
source = requests.get('http://dongyeguiwu.zuopinj.com/5525').content
# source_text = requests.get('http://dongyeguiwu.zuopinj.com/5525').text
# print(source)
# print(source_text)


selector = html.fromstring(source)

# print(selector)


url_list = selector.xpath('//div[@class="book_list"]/ul/li/a/@href')
for url in url_list:
    print(url)
    client.lpush('url_queue', url)
