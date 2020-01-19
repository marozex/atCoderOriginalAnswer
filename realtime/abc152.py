# abc e4完
#a
n,m = map(int,input().split())
if n == m:
    print('Yes')
else:
    print('No')

#b
a,b = map(int,input().split())
aa = str(a) * b
bb = str(b) * a
if aa < bb:
    print(aa)
else:
    print(bb)

#c
import sys
n = int(input())
lis = list(map(int,input().split()))
count = 0
mi = 0
for i,l in enumerate(lis):
    if i == 0:
        mi = l
        count += 1
    else:
        if l < mi:
            mi = l
        if mi >= l:
            count += 1
print(count)

#e
import fractions
n = int(input())
a = list(map(int, input().split()))
ans = a[0]
for i in range(1, n):
    ans = ans * a[i] // fractions.gcd(ans, a[i])

count = 0
for ai in a:
    count += ans//ai
print(count%1000000007)
