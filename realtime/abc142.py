# abcd4完
# a
n = int(input())
li = []
for i in range(1,n+1):
    if i%2 != 0:
        li.append(i)
print(len(li)/n)

# b
n, k = map(int,input().split())
src = list(map(int,input().split()))
count = 0
for s in src:
    if s>= k:
        count += 1
print(count)

# c
n = int(input())
src = list(map(int, input().split()))
ma = {}
for i,s in enumerate(src):
    ma[s-1] = i+1
print(*(list(ma.values())))

# d
import sys
import math
from fractions import gcd

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

a, b = map(int, input().split())
g = gcd(a, b) # gは最大公約数
if g == 1:
    print(1)
    sys.exit()

li = [1]
true_li = make_divisors(g)
#print(true_li)

for i in true_li:
    if i == 1:
        continue
    count = 0
    for l in li:
        if gcd(l,i) != 1:
            count += 1
    if count == 0:
        li.append(i)
print(len(li))
