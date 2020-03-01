#ab2完
#a
n = int(input())
import math
print(math.ceil(n / 2))

#b
import sys
lis1 = list(map(int,input().split()))
lis2 = list(map(int,input().split()))
lis3 = list(map(int,input().split()))
n = int(input())
b_lis = [int(input()) for _ in range(n)]
for i,l1 in enumerate(lis1):   
    if l1 in b_lis:
        lis1[i] = 0
for j,l2 in enumerate(lis2):   
    if l2 in b_lis:
        lis2[j] = 0
for k,l3 in enumerate(lis3):   
    if l3 in b_lis:
        lis3[k] = 0
if lis1 == [0,0,0]:
    print('Yes')
    sys.exit()
if lis2 == [0,0,0]:
    print('Yes')
    sys.exit()
if lis3 == [0,0,0]:
    print('Yes')
    sys.exit()
if lis1[0] == 0 and lis2[0] == 0 and lis3[0] == 0:
    print('Yes')
    sys.exit()
if lis1[1] == 0 and lis2[1] == 0 and lis3[1] == 0:
    print('Yes')
    sys.exit()
if lis1[2] == 0 and lis2[2] == 0 and lis3[2] == 0:
    print('Yes')
    sys.exit()
if lis1[0] == 0 and lis2[1] == 0 and lis3[2] == 0:
    print('Yes')
    sys.exit()
if lis1[2] == 0 and lis2[1] == 0 and lis3[0] == 0:
    print('Yes')
    sys.exit()
#print(b_lis)
#print(lis1,lis2,lis3)
print('No')

#c waだけど
import sys
n,m = map(int,input().split())
tmp = [0] * n
for _ in range(m):
    lis = list(map(int,input().split()))
    if lis[0] > n:
        print('-1')
        sys.exit()
    if tmp[lis[0]-1] != 0 and tmp[lis[0]-1] != lis[1]:
        #print(tmp)
        #print(int(lis[0])-1],lis[1])
        print('-1')
        sys.exit()
    tmp[lis[0]-1] = lis[1]
#print(tmp)
if n ==1 and tmp[0] == 0 :
    print('0')
elif tmp[0] == '0' or tmp[0] == 0:
    print('-1')
else:
    #print(tmp)
    #print(tmp) [7, '0', 2]
    tt = []
    for t in tmp:
        if type(t) is int:
            tt.append(str(t))
        else:
            tt.append(t)
    print(str("".join(tt)))
