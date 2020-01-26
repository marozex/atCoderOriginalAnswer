#abcd4完
#a
import math
h,a = map(int,input().split())
count = math.ceil(h / a)
print(count)

#b
h,n = map(int,input().split())
lis = list(map(int,input().split()))
if sum(lis)>= h:
    print('Yes')
else:
    print('No')

#c
import sys
n,k = map(int,input().split())
lis = list(map(int,input().split()))
if k >=n:
    print(0)
    sys.exit()
s_lis = sorted(lis,reverse=True)
print(sum(s_lis[k:]))

#d
import math
h = int(input())
x = int(math.log2(h))
print(2**(x+1)-1)

