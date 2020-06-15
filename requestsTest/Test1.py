import requests

url = 'https://item.taobao.com/item.htm?spm=a217h.9580640.831236.14.1f9025aaK8vV8W&id=16361721549&scm=1007.12144.81309.69881_0_0&pvid=841df27c-aa45-4398-be30-088f4de07b9b&utparam=%7B%22x_hestia_source%22%3A%2269881%22%2C%22x_object_type%22%3A%22item%22%2C%22x_mt%22%3A9%2C%22x_src%22%3A%2269881%22%2C%22x_pos%22%3A8%2C%22x_pvid%22%3A%22841df27c-aa45-4398-be30-088f4de07b9b%22%2C%22x_object_id%22%3A16361721549%7D'
try:
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print('产生异常')
