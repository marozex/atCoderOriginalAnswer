#abc3完 dはTLE
#a
n, r = map(int,input().split())
if n >= 10:
    print(r)
else:
    print(r+100*(10-n))

#b
n, k = map(int,input().split())
bi=''
while n!=0:
    bi+=str(n%abs(k))
    if k<0:n=-(-n//k)
    else:n=n//k
print(len(bi[::-1]))

#c
n = int(input())
lis = list(map(int,input().split()))
a = min(lis)
b = max(lis)
all_lis = []

for i in range(a,b+1):
    tmp = 0
    for l in lis:
        tmp += (l-i)**2
    all_lis.append(tmp)
print(min(all_lis))

#d TLE
n,a,b = map(int,input().split())

#組み合わせ
from math import factorial
def combinations_count(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))
#print(combinations_count(5, 2))
# 10

'''
count = 0
for i in range(1,n+1):
    count += combinations_count(n, i)
count -= combinations_count(n, a)
count -= combinations_count(n, b)
print(count%1000000007)
'''

'''
count = 0
if n%2 == 0:
    tmp = 0
    for i in range(1,n//2+1):
        tmp += combinations_count(n, i)
    count += 1
    count += tmp*2
    tmp -= combinations_count(n, n/2)
else:
    tmp = 0
    for i in range(1,(n-1)//2+1):
        tmp += combinations_count(n, i)
    count += tmp*2
print(count%1000000007)
'''

'''
動いてはいる
count = 0
if n%2 == 0:
    tmp = 0
    ma = combinations_count(n, n//2)
    tmp = ((n + ma)*(n//2))//2
    #print(tmp)
    count += 1
    count += tmp*2
    count -= combinations_count(n, n//2)
else:
    tmp = 0
    ma = combinations_count(n, (n-1)//2)
    tmp = ((n + ma)*((n-1)//2))//2
    count += tmp*2
#print(count)
count -= combinations_count(n, a)
count -= combinations_count(n, b)
print(count%1000000007)
'''

count = 0
n = n%1000000007
if n%2 == 0:
    tmp = 0
    ma = combinations_count(n, n//2)
    tmp = ((n + ma)*(n//2))//2
    #print(tmp)
    count += 1
    count += tmp*2
    count -= combinations_count(n, n//2)
else:
    tmp = 0
    ma = combinations_count(n, (n-1)//2)
    tmp = ((n + ma)*((n-1)//2))//2
    count += tmp*2
#print(count)
count -= combinations_count(n, a)
count -= combinations_count(n, b)
print(count)
#↑TLE