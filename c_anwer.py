# abc051c

sx, sy, tx, ty = map(int, input().split())
up = "U" * (ty - sy)
right = "R" * (tx - sx)
down = up.replace("U", "D")
left = right.replace("R", "L")
first = up + right + down + left
second = "LU" + up + right + "RDRD" + down + left + "LU"
print(first+second)

# abc054cは保留

# abc057c
import math
n = int(input())
s = math.ceil(math.sqrt(n))
tmp = []
for i in range(2,s+1):
    if n%i == 0:
        m = max(i, n//i)
        tmp.append(int(math.log10(m))+1)
if len(tmp) == 0:
    print(int(math.log10(n))+1)
else:
    print(min(tmp))

# abc061c
import sys
n, k = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
tmp = {}
for l in li:
    if l[0] in tmp:
        tmp[l[0]] += l[1]
    else:
        tmp[l[0]] = l[1]
sorted_tmp = sorted(tmp.items())
for s in sorted_tmp:
    if k > s[1]:
        k = k -s[1]
    else:
        print(s[0])
        sys.exit()

# abc064c
n = int(input())
li = list(map(int, input().split()))
co_li = [0]*8
any_col = 0
for s in li:
    if s < 400:
        co_li[0] += 1
    elif 400 <= s < 800:
        co_li[1] += 1
    elif 800 <= s < 1200:
        co_li[2] += 1
    elif 1200 <= s < 1600:
        co_li[3] += 1
    elif 1600 <= s < 2000:
        co_li[4] += 1
    elif 2000 <= s < 2400:
        co_li[5] += 1
    elif 2400 <= s < 2800:
        co_li[6] += 1
    elif 2800 <= s < 3200:
        co_li[7] += 1
    elif 3200 <= s:
        any_col += 1
color_kind = sum(x>0 for x in co_li)
is_all_any_color = sum(co_li) == 0
min_sum = color_kind + (1 if is_all_any_color is True else 0)
max_sum = color_kind + any_col
print(min_sum,max_sum)

# abc070c
# 解説放送及び先人のコード参考にして記述
# ユークリッドの互除法
import sys
n = int(input())
src = [int(input()) for _ in range(n)]
if n == 1:
    print(src[0])
    sys.exit()
def check(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b
tmp = src[0]
for i in range(n-1):
    tmp = tmp//check(tmp, src[i+1])*src[i+1]
print(tmp)

# abc073c
n = int(input())
li = [int(input()) for _ in range(n)]
li.sort()
tmp = 0
new_li = []
for l in li:
    if l != tmp:
        tmp = l
        new_li.append(1)
    elif l == tmp:
        new_li[-1] += 1
count = 0
for n in new_li:
    if n%2 != 0:
        count += 1
print(count)

# abc076c
import sys
s = input()
t = input()
if len(t) > len(s):
    print('UNRESTORABLE')
    sys.exit()
elif len(t) == len(s):
    print(t)
    sys.exit()
diff = len(s)-len(t)
for i in range(diff,-1,-1):
    target = s[i:len(t)+i]
    for ta,te in zip(target,t):
        if ta != '?' and ta != te:
            break
    else:
        tmp = list(s)
        tmp[i:len(t)+i] = t
        print(''.join(tmp).replace('?','a'))
        sys.exit()
print('UNRESTORABLE')

# abc079c
import sys
a,b,c,d = map(int,input())
ans = 7 - a
li = ['+','-']
for i in li:
    for j in li:
        for k in li:
            bb = b if i=='+' else -b
            cc = c if j=='+' else -c
            dd = d if k=='+' else -d
            if bb+cc+dd == ans:
                print(str(a)+i+str(b)+j+str(c)+k+str(d)+'=7')
                sys.exit()
                
#abc104c
import itertools
import math
d,g = map(int,input().split())
lis = [list(map(int,input().split())) for _ in range(d)]
# print(list(itertools.product([0,1], repeat=d))) [(0, 0), (0, 1), (1, 0), (1, 1)]
count_list = []
for flag in itertools.product([0,1], repeat=d):
    tmp = g
    count = 0
    score_list = []
    kosuu_list = []
    for i,f in enumerate(flag):
        if f==1:
            count += lis[i][0]
            #print(lis[i][1],100*(i+1),lis[i][0],tmp)
            tmp -= (lis[i][1]+100*(i+1)*lis[i][0])
        else:
            score_list.insert(0,100*(i+1))
            kosuu_list.insert(0,lis[i][0]-1)
    #print(score_list)
    #print(kosuu_list)
    #print(lis[i][1],100*(i+1),lis[i][0],tmp)
    if tmp <= 0:
        count_list.append(count)
    else:
        for sss,kkk in zip(score_list,kosuu_list):
            if tmp <= 0:
                break
            elif sss*kkk >= tmp:
                count += math.ceil(tmp/sss)
                tmp -= sss*math.ceil(tmp/sss)
                break
            elif sss*kkk < tmp:
                count += kkk
                tmp -= sss*kkk
        if tmp <= 0:
            count_list.append(count)
    #print(flag)
#print(count_list)
print(min(count_list))

#abc103c
import fractions
N = int(input())
a = list(map(int, input().split()))
ans = a[0]
for i in range(1, N):
    ans = ans * a[i] // fractions.gcd(ans, a[i])
target = ans - 1
sum = 0
for aa in a:
    sum += target%aa
print(sum)

#abc100c
def warizan(n):
    flag = True
    count = 0
    while flag == True:
        if n/2 == n//2:
            count += 1
            n = n/2
        else:
            flag = False
    return count

import math
n = int(input())
lis = list(map(int, input().split()))
new_lis = [warizan(l) for l in lis if l%2 == 0]
print(sum(new_lis))

#abc096c
import sys
h,w = map(int,input().split())
matrix = [[0]*(w+2) for _ in range(h+2)]
for hi in range(h):
    all_inp = input()
    for i,a in enumerate(all_inp):
        matrix[hi+1][i+1]= 1 if a == '#' else 0
#print(matrix)
for ri,row in enumerate(matrix):
    for ci,column in enumerate(row):
        if column == 1:
            if row[ci-1] == 0 and row[ci+1] == 0 and matrix[ri-1][ci] == 0 and matrix[ri+1][ci] == 0:
                print('No')
                sys.exit()
print('Yes')

#abc088c
import sys
lis = [list(map(int,input().split())) for _ in range(3)]
d1 = lis[0][0] - lis[0][1]
d2 = lis[0][1] - lis[0][2]
flag = 'No'
for l in lis:
    if l[0] - l[1] != d1 or l[1] - l[2] != d2:
        print('No')
        sys.exit()
else:
    flag = 'Yes'
print(flag)

#abc085c
n, y = map(int,input().split())
for i in range(n+1):
    for j in range(n-i+1):
        if y-10000*i-5000*j-1000*(n-i-j) == 0:
            print(i,j,n-i-j)
            exit()
print(-1,-1,-1)

#abc105c
n = int(input())
if n == 0:
    print(0)
    exit()
flag = True
ans_str = ''
while True:
    if n == 1:
        ans_str = '1' + ans_str
        print(int(ans_str))
        exit()
    if n < 0 and (-n)%2 == 1:
        ans_str = '1' + ans_str
        n = -(n-1)//2
    elif n < 0 and (-n)%2 == 0:
        ans_str = '0' + ans_str
        n = -n//2
    elif n > 0 and n%2 ==1:
        ans_str = '1' + ans_str
        n = -(n//2)
    elif n > 0 and n%2 ==0:
        ans_str = '0' + ans_str
        n = -(n//2)
        