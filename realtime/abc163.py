#abcd4完
#a
r = int(input())
import math
print(math.pi*2*r)

#b
n,m = map(int,input().split())
li = list(map(int,input().split()))

s = sum(li)
if s>n:
    print('-1')
else:
    print(n-s)

#c
n = int(input())
li = list(map(int,input().split()))
all_li = [0 for _ in range(n)]
for i,l in enumerate(li):
    all_li[l-1] += 1
for a in all_li:
    print(a)

#d
n,k = map(int,input().split())
li = [i for i in range(0,n+1)]
#print(li)
#[0,1, 2, 3]
tmp = 0
def exc(n):
    return (n)*(n+1)//2

for i in range(k,n+2):
    #print(i,li[n-i+1:],li[:i],sum(li[n-i+1:]) - sum(li[:i]))
    #tmp += sum(li[n-i+1:]) - sum(li[:i]) + 1
    mi = exc(i-1)
    ma = exc(n) - exc(n-i)
    #print(i,mi,ma,ma - mi + 1)
    tmp += ma - mi + 1
print(tmp%(10**9+7))
