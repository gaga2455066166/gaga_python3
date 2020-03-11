# 使用函数 range()
for i in range(1, 9):
    print(i)
print(i)

# 使用 range()创建数字列表
# list() 方法用于将元组转换为列表。
# 注：元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中。
print('使用 range()创建数字列表')
numbers = list(range(1, 6))
print(numbers)

# 使用函数range()时，还可指定步长。
print('指定步长2')
even_numbers = list(range(1, 23, 2))
print(even_numbers)

print('指定步长6')
even_numbers = list(range(1, 100, 6))
print(even_numbers)

# 下面的代码演示了
# 如何将前10个整数的平方加入到一个列表中：
squares = []  # 首先，我们创建了一个空列表
for j in range(1, 101):
    square = j ** 2
    squares.append(square)
    # squares.append(j ** 2)
print(squares)

# 对数字列表执行简单的统计计算
print('min:')
print(min(squares))
print('max:')
print(max(squares))
print('sum:')
print(sum(squares))

# 列表解析
# 要使用这种语法，首先指定一个描述性的列表名，如squares；然后，指定一个左方括号，
# 并定义一个表达式，用于生成你要存储到列表中的值。在这个示例中，表达式为value**2，它计
# 算平方值。接下来，编写一个for循环，用于给表达式提供值，再加上右方括号。
print('列表解析:')
phones = [apple*2 for apple in range(900,1000)]
for phone in phones:
    print(phone)

