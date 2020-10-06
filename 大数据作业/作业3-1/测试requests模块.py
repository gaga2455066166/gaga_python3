# import requests
#
# baseurl = 'http://tieba.baidu.com/f?'
# params = {
#     'kw': '赵丽颖吧',
#     'pn': '50'
# }
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; '
#                   '.NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}
# # 自动对params进行编码,然后自动和url进行拼接,去发请求
# res = requests.get(baseurl, params=params, headers=headers)
# res.encoding = 'utf-8'
# print(res.text)


import requests

url = 'http://www.baidu.com/'  # 爬取百度网页
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 \
    (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}

# res = requests.get(url, headers=headers)
# print(res.encoding)


# text属性获取响应内容（字符串）网站源码
# res = requests.get(url, headers=headers)
# res.encoding = 'utf-8'
# html = res.text
# print(html)


# content属性获取响应内容（字节串 bytes）网站源码
# res = requests.get(url, headers=headers)
# html = res.content.decode('utf-8')
# print(html)

# print(res.status_code)  # 查看响应码 200
# print(res.url)  # 查看访问的URL地址 https://www.baidu.com/
