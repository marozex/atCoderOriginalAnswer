#abc3完 dはTLE
#a
a,b,c = map(int,input().split())
if (a == b and a != c) or (a == c and a != b) or (b == c and a != b):
    print('Yes')
else:
    print('No')

#b
n = int(input())
lis = list(map(int,input().split()))
flag = True
for l in lis:
    if l%2 == 0:
        if l%3 != 0 and l%5 != 0:
            flag = False
if flag:
    print('APPROVED')
else:
    print('DENIED')

#c
import collections
n = int(input())
lis = []
for _ in range(n):
    lis.append(input())
c = collections.Counter(lis)
most = c.most_common()
most_counter = c.most_common()[0][1]
#print(most)
#print(most_counter)
tmp_lis = []
for m in most:
    if m[1] == most_counter:
        tmp_lis.append(m[0])
    else:
        break
for t in sorted(tmp_lis):
    print(t)

#d TLE
import itertools
n, k  = map(int,input().split())
lis = list(map(int,input().split()))
tmp = list(itertools.combinations(lis, 2))
new = []
for t in tmp:
    new.append(t[0]*t[1])
#print(sorted(new))
print(sorted(new)[k-1])
