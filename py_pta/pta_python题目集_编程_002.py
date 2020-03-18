def remove_max(lists):
    max_re = max(scores)
    max_index = scores.index(max_re)
    del scores[max_index]


def remove_min(lists):
    min_re = min(scores)
    min_index = scores.index(min_re)
    del scores[min_index]


n = int(input())
m = (input().split())
aver = 0
scores = [float(score) for score in m]
remove_max(scores)
remove_max(scores)
remove_min(scores)
remove_min(scores)


for i in scores:
    aver = aver + i
    i += 1
print("aver={:.2f}".format(aver / (n - 4)))
