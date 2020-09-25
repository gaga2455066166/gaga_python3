from pymongo import MongoClient
import random

src = 'abcdefghijklmnopqrstuvwxyz'


def get_str(x, y):
    str_sum = random.randint(x, y)
    astr = ''
    for i in range(str_sum):
        astr += random.choice(src)
    return astr


def get_data_list(n):
    res = []
    for i in range(n):
        res.append({'name': get_str(2, 4), 'passwd': get_str(8, 12)})
    return res


if __name__ == '__main__':
    print("建立连接...")
    stus = MongoClient().test.stu
    print('插入一条记录...')
    stus.insert({'name': get_str(2, 4), 'passwd': get_str(8, 12)})
    print("显示一条记录...")
    stu = stus.find_one()
    print(stu)
    print('批量插入多条记录...')
    stus.insert(get_data_list(3))
    print('显示所有记录...')
    for stu in stus.find():
        print(stu)
    print('更新一条记录...')
    name = input('请输入记录的name:')
    stus.update({'name': name}, {'$set': {'name': 'aaaa'}})
    print('显示所有记录...')
    for stu in stus.find():
        print(stu)
    print('删除一条记录...')
    name = input('请输入记录的name:')
    stus.remove({'name': name})
    print('显示所有记录...')
    for stu in stus.find():
        print(stu)
