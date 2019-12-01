# abc3完。dはTLE
# a
m1, d1 = map(int, input().split())
m2, d2 = map(int, input().split())
if m1 == m2:
    print(0)
else:
    print(1)

# b
import sys
n = int(input())
start = int(n//1.1)
lis = []
for i in range(start,n+1):
    lis.append(i)
new_lis = []
for l in lis:
    new_lis.append(int(l*1.08))
if n in new_lis:
    for li in lis:
        if int(li*1.08) == n:
            print(li)
            sys.exit()
else:
    print(":(")

# c
import sys
x = int(input())
n = x//100
a = x%100
if a <= 5*n:
    print(1)
else:
    print(0)

# d(参考。TLE)
import sys
n = int(input())
s = input()
se = set()
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            se.add(s[i]+s[j]+s[k])
print(len(se))
