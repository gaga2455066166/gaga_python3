# 基本统计值
# 1,2,3,4,5,6,7,8,9,0


def average(lists):
    sum_list = 0
    for j in lists:
        sum_list += j
    return sum_list / len(lists)


def standard_deviation(lists):
    nums_average = average(lists)
    nums_temp = 0
    for k in lists:
        nums_temp = nums_temp + (nums_average - k) ** 2
    nums_temp = nums_temp / len(nums_list)
    return nums_temp


def median(lists):
    lists = sorted(lists)
    if len(lists) % 2 == 0:
        return (lists[len(lists) // 2] + lists[len(lists) // 2 - 1]) / 2
    else:
        return lists[len(lists) // 2]


nums_str_list = (input().split(','))
nums_list = []
for i in nums_str_list:
    nums_list.append(int(i))
print('{:.2f}'.format(average(nums_list)))
print('{:.2f}'.format(standard_deviation(nums_list)))
print(median(nums_list))
