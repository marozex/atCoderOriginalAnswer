# 2完
#a
a,b,c =map(int,input().split())
r = c-(a-b)
if r<0:
    print(0)
else:
    print(r)

#b
import math
n = int(input())
keta = math.floor(math.log10(n))
sum = 0
for i in range(0,keta,2):
    sum += 10**(i+1)-10**(i)
if keta%2 == 0:
    sum += n - (10**keta)+1
print(sum)