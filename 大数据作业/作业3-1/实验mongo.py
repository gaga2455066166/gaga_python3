import random
import pymongo
from mongoengine import *

connect('test')  # 连接本地blog数据库


# connect('test', host='localhost', username='admin', password='123')
def my_db(table_name):
    import pymysql
    coon = pymysql.connect(
        user='root', passwd='1234', host='127.0.0.1', port=3306,
        db='testdb', charset='utf8'
    )
    cur = coon.cursor(cursor=pymysql.cursors.DictCursor)  # 建立游标，指定cursor类型返回的是字典
    # cur = coon.cursor()
    sql = 'select * from %s;' % table_name
    cur.execute(sql)
    if sql.strip()[:6].upper() == 'SELECT':
        res = cur.fetchall()
    cur.close()
    coon.close()
    return res


def output_all():
    for post in Mytab.objects:
        post.introduce()


class Mytab(Document):
    sid = IntField()
    name = StringField()
    passwd = StringField()

    def introduce(self):
        print('序号:', self.sid, end=" ")
        print('姓名:', self.name, end=' ')
        print('密码:', self.passwd)

    def set_pw(self, pw):
        if pw:
            self.passwd = pw
            self.save()


allrow = my_db('mytab')
# 关系数据库表插入redis
for myuser in allrow:
    # print(date)
    stu = Mytab(sid=myuser['id'], name=myuser['name'], passwd=myuser['passwd'])
    stu.save()
# 输出Mytab所有数据
output_all()

print('修改一个文档')
stu = Mytab.objects(name='aaa').first()
if stu:
    stu.name = 'aaaa'
    stu.save()
    stu.set_pw('bbbbbbbb')
    stu.introduce()

print('删除一个文档')
stu = Mytab.objects(name='aaa').first()
stu.delete()

stus = Mytab.objects()
for stu in stus:
    stu.introduce()
'''
mongo
use test
db.stu.find()
'''
