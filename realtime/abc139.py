# abcd4完
# a
s = input()
t = input()
count = 0
for si,ti in zip(s,t):
    if si == ti:
        count += 1
print(count)

# b
import sys
import math
a, b = map(int, input().split())
if b == 1:
    print(0)
    sys.exit()
if a >= b:
    print(1)
    sys.exit()
print(math.ceil((b - a) / (a - 1))+1)

# c
n = int(input())
src = list(map(int, input().split()))
count = [0]
for i in range(len(src)-1):
    if src[i]>=src[i+1]:
        count[-1] = count[-1]+1
    else:
        count.append(0)
print(max(count))

# d
import sys
n = int(input())
if n == 1:
    print(0)
    sys.exit()
else:
    print((n-1)*n//2)

### メモ用
#Eはスルー、FはWA
import math
n = int(input())
src = [list(map(int, input().split())) for _ in range(n)]
a = []
b = []
c = []
d = []
for s in src:
    x = s[0]
    y = s[1]
    if x != 0 or y != 0:
        if x >= 0 and y >= 0:
            a.append(s)
        if x > 0 and y < 0:
            b.append(s)
        if x < 0 and y > 0:
            c.append(s)
        if x <= 0 and y <= 0:
            d.append(s)
abcd = a+b+c+d
bcd = b+c+d
acd = a+c+d
abd = a+b+d
abc = a+b+c
ab = a+b
ac = a+c
bd = b+d
cd = c+d
ad = a+d
bc = b+c
def kyori(list):
    if len(list) == 0:
        return 0
    xsum = 0
    ysum = 0
    for l in list:
        xsum += l[0]
        ysum += l[1]
    return math.sqrt(xsum**2+ysum**2)
print(max(kyori(abcd),kyori(bcd),kyori(acd),kyori(abd)
,kyori(abc),kyori(ab),kyori(ac),kyori(bd),kyori(cd),
kyori(ad),kyori(bc),kyori(a),kyori(b),kyori(c),kyori(d)))
