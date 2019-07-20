# a
r = int(input())
print(3 * r ** 2)

# b
import math
n, d = map(int,input().split())
print(math.ceil(n / (d*2+1)))

# c
import copy
n = int(input())
all_list = [int(input()) for _ in range(n)]
max_value = max(all_list)
max_value_count = all_list.count(max_value)
for i in range(n):
    if all_list[i] == max_value:
        if max_value_count > 2:
            print(max_value)
        else:
            tmp = copy.copy(all_list)
            tmp.pop(i)
            print(max(tmp))
    else:
        print(max_value)