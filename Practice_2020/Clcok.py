# coding=utf-8

import turtle
from datetime import *


# 抬起画笔，向前运动一段距离放下
def Skip(step):
    turtle.penup()  #抬起画笔
    turtle.forward(step) #画笔沿当前方向前进step
    turtle.pendown()  #放下画笔


def MakePoint(name, length):
    # 注册Turtle形状，建立表针Turtle
    turtle.reset() #清空窗口，重置turtle状态为起始状态

    Skip(-length * 0.1)  #退回一小步，指针头多出中心点一小段

    turtle.begin_poly()  # 开始绘制。开始记录多边形的顶点。当前的乌龟位置是多边形的第一个顶点。
    turtle.forward(length * 1.1) #0.1与1的比例（以中心点为准）

    turtle.end_poly() # 结束绘制。停止记录多边形的顶点。当前的乌龟位置是多边形的最后一个顶点。将与第一个顶点相连。

    handForm = turtle.get_poly()   # 获取绘制（多边形）。
    turtle.register_shape(name, handForm)  # 注册一个名为'name'的shape（ handForm ）


def Init():
    global secPoint, minPoint, hurPoint, printer
    # 重置Turtle指向北
    turtle.mode("logo")    # 重置Turtle指向北，顺时针；standard的向右（东）逆时针
    #设置乌龟模式（“standard”，“logo”或“world”）并执行重置。  logo:向上（北）,顺时针
    # 建立三个表针Turtle并初始化
    MakePoint("SecPoint", 180)  #建立三个Turtle形状
    MakePoint("MinPoint", 160)
    MakePoint("HurPoint", 130)

    # .shape("name)；name是指形状系统自带：“arrow”, “turtle”,
    # “circle”, “square”, “triangle”, “classic”，也可以自定义图形如本例中SecPoint
    secPoint = turtle.Turtle()  # 创建一个 Turtle 对象
    secPoint.shape("SecPoint")  #改变海龟secPoint的形状为刚才建立的secPoint图形
    secPoint.shapesize(1, 1,3)
    secPoint.speed(0)

    minPoint = turtle.Turtle()
    minPoint.shape("MinPoint")
    minPoint.shapesize(1, 1, 5)
    minPoint.pencolor("green")
    minPoint.speed(0)


    hurPoint = turtle.Turtle()
    hurPoint.shape("HurPoint")
    hurPoint.shapesize(1, 1, 7)
    hurPoint.pencolor("red")
    hurPoint.speed(0)

    '''
            turtle.shapesize(stretch_wid=None, stretch_len=None, outline=None)
            返回或者设置形状拉伸大小和轮廓线。stretch_wid是垂直方向拉伸，
            stretch_len水平方向拉伸，outline轮廓的宽度。
    '''

    printer = turtle.Turtle()  # 创建一个输出文字Turtle对象
    printer.pencolor("orange")
    printer.hideturtle()  # 隐藏画笔的turtle形状
    printer.penup()


def SetupClock(radius):# 建立表的外框
    turtle.reset()    #这个指令可以清除窗口,并且让turtle回到起点。
    turtle.setup(600,600)
    turtle.pensize(7)
    turtle.pencolor("blue")
    for i in range(60):
        Skip(radius)
        if i % 5 == 0:  #5分钟整数倍的地方比其他地方长20
            turtle.forward(20)
            if i == 0:
                turtle.write(int(12), align="center", font=("Courier", 18, "bold"))
            elif i == 30:
                Skip(25)
                turtle.write(int(6), align="center", font=("Courier", 18, "bold"))
                Skip(-25)
            elif (i == 25 or i == 35):
                Skip(22)
                turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
                Skip(-22)
            else:
                turtle.write(int(i / 5), align="center", font=("Courier", 18, "bold"))
            Skip(-radius - 20)  #退回到表盘中心
        else:
            turtle.dot(5)  # 其他的在半径为radius的地方花直径为5的圆点
            Skip(-radius)  #退回到表盘中心
        turtle.right(6)  #右转6度，合计画60个点


def Week(t):
    week = ["星期一", "星期二", "星期三",
            "星期四", "星期五", "星期六", "星期日"]
    return week[t.weekday()]


def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s年%d月%d日" % (y, m, d)


def Tick():
    # 绘制表针的动态显示
    #turtle.reset()    #这个指令可以清除窗口,并且让turtle回到起点。
    t = datetime.today()
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60.0
    hour = t.hour + minute / 60.0
    # setheading(angle);#海龟朝向为angle角度，三个指针海龟形状为上面建立的图形

    secPoint.setheading(6 * second)  #60秒，每一秒一次整个圆为360度
    minPoint.setheading(6 * minute)  #60分钟，整个圆为360，角度位置为分钟*6+秒针/10
    hurPoint.setheading(30 * hour)  #12小时，整个圆为360，角度位置为小时*30+分针/10


    turtle.tracer(False)
    printer.forward(65)
    printer.write(Week(t), align="center",
                  font=("Courier", 20, "bold"))
    printer.back(130)
    printer.write(Date(t), align="center",
                  font=("Courier", 28, "bold"))
    printer.home()  #画笔回到原点
    turtle.tracer(True)

    # 100ms后继续调用tick
    turtle.ontimer(Tick, 100)


def main():
    # 打开/关闭龟动画，并为更新图纸设置延迟。
    turtle.tracer(False)   #图形将一次性画好
    Init()
    SetupClock(220)  #画半径为250的外表框

    turtle.tracer(True)   #图形正常速度画
    Tick()
    turtle.mainloop()  #启动事件循环 -调用Tkinter的mainloop函数
 #   turtle.done()

if __name__ == "__main__":
    main()


