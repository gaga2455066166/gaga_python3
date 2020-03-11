lists = ['陈', 'lin', 'huang', 'wang']
print(lists)
print(lists[0])
print(lists[1].title())
print(lists[-1])

print("我姓" + lists[0])

lists.append('liu')
print(lists)
lists[2] = 'Ling'
print(lists)
lists.append("刘")
print(lists)
lists.insert(0, '赵')
print('*******************')
print(lists)

print(lists[0], end="")
del lists[0]

print(lists[0])

person = lists.pop()
print(person)

print(lists)

person = lists.pop(2)
print(person)
print('***********************')

# 方法remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要
# 使用循环来判断是否删除了所有这样的值。
print(lists)
lists.remove('陈')
print(lists)

print('**********************')
# sort
strings = ['ass', 'dse', 'asc', 'rty', 'oiu']
strings.sort()
print(strings)

strings.sort(reverse=True)
print(strings)

# 使用函数 sorted()对列表进行临时排序
print("使用函数 sorted()对列表进行临时排序")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
print(cars)
print(sorted(cars, reverse=True))

# 倒着打印列表，注意，reverse()不是指按与字母顺序相反的顺序排列列表元素，
# 而只是反转列表元素的排列顺序：
print('倒着打印列表')
cars.reverse()
print(cars)

# 确定列表的长度
print('确定列表的长度')
print(len(cars))

# 切片
print('切片')
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:3])
print(len(players))

# 遍历切片
print('遍历切片')
for player in players[1:3]:
    print(player.title())

# 分数排序
print('分数排序：')
scores = [12, 34, 56, 78, 3, 54, 90, 23, 77, 90]
scores.sort(reverse=True)
for score in scores[:3]:
    print(score)
print('分数排序：')
scores.sort(reverse=False)
for score in scores[:3]:
    print(score)

# 复制列表
print('复制列表')
my_foods = ['pizza', 'milk', 'carrot cake']
friend_foods = my_foods[:]
print(friend_foods)
print(my_foods)

# 与上面的不同
# 这里将my_foods赋给friend_foods，而不是将my_foods的副本存储到friend_foods。
# 这种语法实际上是让Python将新变量friend_foods关联到包含在my_foods中的列表，因此这两个
# 变量都指向同一个列表。鉴于此，当我们将'cannoli'添加到my_foods中时，它也将出现在
# friend_foods中；同样，虽然'ice cream'好像只被加入到了friend_foods中，但它也将出现在这
# 两个列表中。
print('与上面的不同')
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods  # 有点类似指针，指向同一个列表
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
print('ice cream' in friend_foods)
print('cream' in friend_foods)
