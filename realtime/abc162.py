#ab2完
#a
n = list(input())
if '7' in n:
    print('Yes')
else:
    print('No')

#b
n = int(input())
#print(li)
tmp = []
for l in range(1,n+1):
    if l%3 != 0 and l%5 != 0:
        #print(l)
        tmp.append(l)
print(sum(tmp))

#c
import math
k = int(input())
count = 0
for i in range(1,k+1):
    for j in range(1,k+1):
        for k in range(1,k+1):
            tmp = math.gcd(i,j)
            count += math.gcd(tmp,k)
print(count)

#d
n = int(input())
s = list(input())
a_li = []
b_li = []
c_li = []
for i,ss in enumerate(s):
    if ss == 'R':
        a_li.append(i+1)
    elif ss == 'G':
        b_li.append(i+1)
    else:
        c_li.append(i+1)
count = 0
for i in range(1,n+1):
    for d in range(1,n):
        if i + 2*d > n:
            break
        if s[i-1] != s[i+d-1] and s[i+d-1] != s[i+2*d-1] and s[i-1] != s[i+2*d-1]:
            count += 1
#print(len(a_li),len(b_li),len(c_li),count)
#print(count)
print(len(a_li)*len(b_li)*len(c_li)-count)
