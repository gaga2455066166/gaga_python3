import pymysql


def output_all_student():
    cur.execute('select * from student')
    for item in cur.fetchall():
        print(item)


if __name__ == '__main__':
    print("建立连接...")
    con = pymysql.connect(user='root', passwd="123456", db='db_python')

    print("建立游标...")
    cur = con.cursor()

    # 学生表：
    # print('创建一张Student表,并插入数据:')
    cur.execute('create table student(s_no varchar(7) primary key not null,'
                's_name text,s_sex text,s_age int)')
    # print("插入数据")
    print(cur.execute("insert into student(s_no, s_name, s_sex, s_age)"
                      "values (2015001,'Zhangsan','male',23)"))
    print(cur.execute("insert into student(s_no, s_name, s_sex, s_age)"
                      "values (2015003,'Mary','female',22)"))
    print(cur.execute("insert into student(s_no, s_name, s_sex, s_age)"
                      "values (2015004,'Lisi','male',24)"))

    # 课程表：
    cur.execute('create table course(c_no varchar(6) primary key not null,'
                'c_name text,c_credit double)')
    print(cur.execute("insert into course(c_no, c_name, c_credit)"
                      "values (123001,'Math',2.0)"))
    print(cur.execute("insert into course(c_no, c_name, c_credit)"
                      "values (123002,'Computer Science',5.0)"))
    print(cur.execute("insert into course(c_no, c_name, c_credit)"
                      "values (123003,'English',3.0)"))

    # 学生课程表：
    cur.execute('create table sc(sc_sno varchar(7) not null,'
                'sc_cno varchar(6) not null,sc_score double)')
    print(cur.execute("insert into sc(sc_sno, sc_cno, sc_score)"
                      "values (2015001,123001,86)"))
    print(cur.execute("insert into sc(sc_sno, sc_cno, sc_score)"
                      "values (2015001,123003,69)"))
    print(cur.execute("insert into sc(sc_sno, sc_cno, sc_score)"
                      "values (2015002,123002,77)"))
    print(cur.execute("insert into sc(sc_sno, sc_cno, sc_score)"
                      "values (2015002,123003,99)"))
    print(cur.execute("insert into sc(sc_sno, sc_cno, sc_score)"
                      "values (2015003,123001,98)"))
    print(cur.execute("insert into sc(sc_sno, sc_cno, sc_score)"
                      "values (2015003,123002,95)"))

    con.commit()
    cur.close()
    con.close()
