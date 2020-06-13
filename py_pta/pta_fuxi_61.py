# 字典翻转输出
# {"A": 569, "B": 78}
dictionary = eval(input())
new_dict = {value: key for (key, value) in dictionary.items()}
print(new_dict)
