# abc051c

sx, sy, tx, ty = map(int, input().split())
up = "U" * (ty - sy)
right = "R" * (tx - sx)
down = up.replace("U", "D")
left = right.replace("R", "L")
first = up + right + down + left
second = "LU" + up + right + "RDRD" + down + left + "LU"
print(first+second)

# abc054cは保留

# abc057c
import math
n = int(input())
s = math.ceil(math.sqrt(n))
tmp = []
for i in range(2,s+1):
    if n%i == 0:
        m = max(i, n//i)
        tmp.append(int(math.log10(m))+1)
if len(tmp) == 0:
    print(int(math.log10(n))+1)
else:
    print(min(tmp))

# abc061c
import sys
n, k = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
tmp = {}
for l in li:
    if l[0] in tmp:
        tmp[l[0]] += l[1]
    else:
        tmp[l[0]] = l[1]
sorted_tmp = sorted(tmp.items())
for s in sorted_tmp:
    if k > s[1]:
        k = k -s[1]
    else:
        print(s[0])
        sys.exit()

# abc064c
n = int(input())
li = list(map(int, input().split()))
co_li = [0]*8
any_col = 0
for s in li:
    if s < 400:
        co_li[0] += 1
    elif 400 <= s < 800:
        co_li[1] += 1
    elif 800 <= s < 1200:
        co_li[2] += 1
    elif 1200 <= s < 1600:
        co_li[3] += 1
    elif 1600 <= s < 2000:
        co_li[4] += 1
    elif 2000 <= s < 2400:
        co_li[5] += 1
    elif 2400 <= s < 2800:
        co_li[6] += 1
    elif 2800 <= s < 3200:
        co_li[7] += 1
    elif 3200 <= s:
        any_col += 1
color_kind = sum(x>0 for x in co_li)
is_all_any_color = sum(co_li) == 0
min_sum = color_kind + (1 if is_all_any_color is True else 0)
max_sum = color_kind + any_col
print(min_sum,max_sum)

# abc070c
# 解説放送及び先人のコード参考にして記述
# ユークリッドの互除法
import sys
n = int(input())
src = [int(input()) for _ in range(n)]
if n == 1:
    print(src[0])
    sys.exit()
def check(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b
tmp = src[0]
for i in range(n-1):
    tmp = tmp//check(tmp, src[i+1])*src[i+1]
print(tmp)

# abc073c
n = int(input())
li = [int(input()) for _ in range(n)]
li.sort()
tmp = 0
new_li = []
for l in li:
    if l != tmp:
        tmp = l
        new_li.append(1)
    elif l == tmp:
        new_li[-1] += 1
count = 0
for n in new_li:
    if n%2 != 0:
        count += 1
print(count)

# abc076c
import sys
s = input()
t = input()
if len(t) > len(s):
    print('UNRESTORABLE')
    sys.exit()
elif len(t) == len(s):
    print(t)
    sys.exit()
diff = len(s)-len(t)
for i in range(diff,-1,-1):
    target = s[i:len(t)+i]
    for ta,te in zip(target,t):
        if ta != '?' and ta != te:
            break
    else:
        tmp = list(s)
        tmp[i:len(t)+i] = t
        print(''.join(tmp).replace('?','a'))
        sys.exit()
print('UNRESTORABLE')