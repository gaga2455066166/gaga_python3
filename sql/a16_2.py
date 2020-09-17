# from mysql import connector
import pymysql
import random

src = 'abcdefghijklmnopqrstuvwxyz'


def get_str(x, y):
    str_sum = random.randint(x, y)
    astr = ''
    for i in range(str_sum):
        astr += random.choice(src)
    return astr


def output():
    cur.execute('select * from mytab')
    for sid, name, ps in cur:
        print(sid, ' ', name, ' ', ps)


def output_all():
    cur.execute('select * from mytab')
    for item in cur.fetchall():
        print(item)


def get_data_list(n):
    res = []
    for i in range(n):
        res.append((get_str(2, 4), get_str(8, 12)))
    return res


if __name__ == '__main__':
    print("建立连接...")
    import pymysql

    con = pymysql.connect(user='root', passwd="123456", db='db_python')
    # con = pymysql.connect(host='127.0.0.1', user='root', passwd="123456", db='mysql')
    # con = connector.connect(user='root',password='123456',database='test')
    print("建立游标...")
    cur = con.cursor()
    print('创建一张表mytab...')
    cur.execute('create table mytab(id int primary key auto_increment not null,name text,passwd text)')
    print('插入一条记录...')
    cur.execute('insert into mytab (name,passwd)values(%s,%s)', (get_str(2, 4), get_str(8, 12),))
    print('显示所有记录...')
    output()
    print('批量插入多条记录...')
    cur.executemany('insert into mytab (name,passwd)values(%s,%s)', get_data_list(3))
    print("显示所有记录...")
    output_all()
    print('更新一条记录...')
    cur.execute('update mytab set name=%s where id=%s', ('aaa', 1))
    print('显示所有记录...')
    output()
    print('删除一条记录...')
    cur.execute('delete from  mytab where id=%s', (3,))
    con.commit()
    print('显示所有记录：')
    output()
    cur.close()
    con.close()
