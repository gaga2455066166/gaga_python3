numbers_list = map(int, input().split())
numbers_list = sorted(numbers_list)
print('Max={}'.format(numbers_list[len(numbers_list)-1]))
print('Min={}'.format(numbers_list[0]))
