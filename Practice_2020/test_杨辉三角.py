def NumList_to_StrList(data):
    """将一个数字列表转换成字符串"""
    new_data = []
    for i in range(len(data)):  # 先将数字列表编程每个元素都是字符的列表
        new_data.append(str(data[i]))

    string = ' '.join(new_data)  # 将字符列表的每个元素连接起来，中间分隔符为空格
    return string


# center() 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格。
# width -- 字符串的总宽度。
def YangHui(n):
    #    print([1])
    width = n * 6  # 设置字符串的宽度
    print('1'.center(width))
    line = [1, 1]
    print('1 1'.center(width))

    for i in range(2, n):
        r = []
        for j in range(0, len(line) - 1):
            r.append(line[j] + line[j + 1])
        line = [1] + r + [1]
        print(NumList_to_StrList(line).center(width))




if __name__ == '__main__':
    YangHui(11)
