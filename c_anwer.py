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
