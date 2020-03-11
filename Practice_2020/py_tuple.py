# 元组
# 元组看起来犹如列表，但使用圆括号而不是方括号来标识。定义元组后，就可以使用索引来
# 访问其元素，就像访问列表元素一样。
# 例如，如果有一个大小不应改变的矩形，可将其长度和宽度存储在一个元组中，从而确保它
# 们是不能修改的：
phones = ('apple', 'xiaomi', 'oppo', 'huawei')
print(phones[2])
for phone in phones:
    print(phone)
# 由于试图修改元组的操作是被禁止的，因此Python指出不能给元组的元素赋值
# 虽然不能修改元组的元素，但可以给存储元组的变量赋值。因此，如果要修改前述矩形的尺
# 寸，可重新定义整个元组：
phones = ['vivo', 'oppo', 'one_plus']
print(phones)
