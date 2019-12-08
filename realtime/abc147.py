## ab2完
# a
a1, a2, a3 = map(int,input().split())
if a1+a2+a3 >= 22:
    print('bust')
else:
    print('win')

# b
s = input()
re_s = reversed(s)
count = 0
for si,re_si in zip(s,re_s):
    if si != re_si:
        count += 1
if count == 0:
    print(0)
else:
    print(count//2)

# c途中メモ
n = int(input())
all_lis = []
for i in range(n):
    tmp_lis = []
    for j in range(n):
        tmp_lis.append(None)
    all_lis.append(tmp_lis)
for i in range(n):
    roop = int(input())
    for r in range(roop):
        x, y = map(int,input().split())
        print([i,x,y])
        all_lis[i][x-1] = y
print(all_lis)

import itertools
l = [0,1]
for v in itertools.product(l, repeat=n):
#   print(v) (0, 0)(0, 1)(1, 0)(1, 1)
    for vi in v: