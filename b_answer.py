# AtCoder B問題の自作解答

# abc044

input = input()
import string
al = string.ascii_lowercase
for a in al:
    tmp = ""
    for i in input:
        if i==a:
            tmp+=i
    if(len(tmp)%2 == 1):
        print("No")
        exit()
print("Yes")


# abc046
N, K = map(int, input().split())
print(K * (K-1)**(N-1))

# abc047
x, y, n = map(int, input().split())
input = [list(map(int, input().split())) for _ in range(n)] 
xmax = x
xmin = 0
ymax = y
ymin = 0
for i in input:
    type = i[2]
    if type == 1 and (i[0] > xmin):
        xmin = i[0]
    elif type == 2 and (i[0] < xmax):
        xmax = i[0]
    elif type == 3 and (i[1] > ymin):
        ymin = i[1]
    elif type == 4 and (i[1] < ymax):
        ymax = i[1]
if (xmax > xmin) and (ymax > ymin):
    print((xmax - xmin)*(ymax - ymin))
else:
    print(0)

# abc048
a, b, x = map(int, input().split())

if a != b:
    base = (b // x) - (a //x)
    if a % x == 0:
        base += 1
    print(base)
else:
    if a % x == 0:
        print(1)
    else:
        print(0)

# abc049

h, w = map(int, input().split())
org_list = [input() for _ in range(h)]
new_list = []
for i in org_list:
    new_list.append(i)
    new_list.append(i)
for n in new_list:
    print(n)

# abc50

n = int(input())
time_list = list(map(int,input().split()))
m = int(input())
drink_list = [list(map(int,input().split())) for _ in range(m)]
sum_time = sum(time_list)

for d in drink_list:
    effect_index = d[0] - 1
    effect_time = d[1]
    print(sum_time - time_list[effect_index] + effect_time)

# abc051

k, s = map(int, input().split())
count = 0
for kx in range(0, k+1):
    for ky in range(0, k+1):
        kz = s - kx -ky
        if 0 <= kz <= k: # if 0 <= kz <= k and kx + ky + kz == s:　だとTLEになる
            count += 1
print(count)

# abc052

n = int(input())
s = input()
tmp_list = [0]
x = 0
for _ in s:
    if _ == 'I':
        x += 1
    else:
        x -= 1
    tmp_list.append(x)
print(max(tmp_list))

# abc053b
st =input()
ai = st.find('A')
zi = st.rfind('Z')
print(zi - ai + 1)

# abc054b
import sys
n, m = map(int, input().split())
a_list = [input() for _ in range(n)]
b_list = [input() for _ in range(m)]

for i in range(n-m+1):
    for j in range(n-m+1):
        new_list = [a_list[k][j:j+m] for k in range(i,i+m)]
        if(new_list == b_list):
            print('Yes')
            sys.exit()
print('No')

# abc055b
import math
n = int(input())
print(math.factorial(n)%(10**9+7))

# abc056b
w, a, b = map(int, input().split())
a_list = [a, a+w]
b_list = [b, b+w]
if a_list[0]>b_list[1]:
    print(a_list[0]-b_list[1])
elif a_list[1]<b_list[0]:
    print(b_list[0]-a_list[1])
else:
    print(0)

# abc057b
n, m = map(int,input().split())
student_list = [list(map(int,input().split())) for _ in range(n)]
check_list = [list(map(int,input().split())) for _ in range(m)]
for s in student_list:
    tmp = []
    for c in check_list:
        tmp.append(abs(s[0]-c[0]) + abs(s[1]-c[1]))
    print(tmp.index(min(tmp))+1)

# abc058b
o = input()
e = input()

s = ""
if len(o) == len(e):
    for i in range(len(o)):
        s += o[i]+e[i]
else:
    for i in range(len(o)-1):
        s += o[i]+e[i]
    s += o[-1]
print(s)

# abc059b
a = int(input())
b = int(input())
if a>b:
    print("GREATER")
elif a<b:
    print("LESS")
else:
    print("EQUAL")

# abc060b
a, b, c = map(int, input().split())
tmp = []
for i in range(b):
    tmp.append(a*(i+1)%b)
if c in tmp:
    print('YES')
else:
    print('NO')

# abc061b
n, m = map(int, input().split())
double_dimension = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    double_dimension[a-1][b-1] += 1
tmp = []
for i in range(n):
    row = sum(double_dimension[i])
    column = 0
    for d in double_dimension:
        column += d[i]
    print(row + column)
# ↑無駄が多すぎた。↓改良版
n, m = map(int, input().split())
double_dimension = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    double_dimension[a-1][b-1] += 1
    double_dimension[b-1][a-1] += 1
for i in range(n):
    print(sum(double_dimension[i]))

# abc062b
h, w = map(int, input().split())
matrix = [input() for _ in range(h)]
print('#'*(w+2))
for m in matrix:
    print('#'+m+'#')
print('#'*(w+2))

# abc063b
st = input()
tmp = []
for s in st:
    tmp.append(s)
if len(tmp) == len(set(tmp)):
    print('yes')
else:
    print('no')

# abc064b
n = int(input())
l = list(map(int, input().split()))
s = set(l)
print(max(s) - min(s))

# abc065b
# 再帰回数の上限を開放する必要がある
import sys
sys.setrecursionlimit(1000000)
n = int(input())
a_list = [int(input()) for _ in range(n)]
def calc_ans(start_num, count, max_count, all_list):
    ans = all_list[start_num-1]
    if ans == 2:
        print(count)
    elif count == max_count:
        print('-1')
    else:
        calc_ans(ans, count+1, max_count, all_list)
calc_ans(1, 1, n, a_list)

# abc066b
import sys
s = input()
l = len(s)
del_len_max = l-2
del_len_min = 1 if l%2 == 1 else 2
if del_len_min == del_len_max:
    print(del_len_max)
    sys.exit()
for i in range(del_len_min, del_len_max+2, 2):
    before = s[0:(l-i)//2]
    after = s[(l-i)//2:l-i]
    if before == after:
        print(l-i)
        sys.exit()

# abc067b
n, k = map(int, input().split())
l_list = list(map(int, input().split()))
new_list = []
for i in range(k):
    max_value = l_list.pop(l_list.index(max(l_list)))
    new_list.append(max_value)
print(sum(new_list))

# abc068b
n = int(input())
result = 2
while result <= n:
    result = result*2
print(result//2)

# abc069b
s = input()
l = len(s)
print(s[0]+str(l-2)+s[-1])

# abc070b
a, b, c, d = map(int, input().split())
if a<=c and d<=b:
    print(d-c)
elif c<=a and b<=d:
    print(b-a)
elif c<=a and a<=d<=b:
    print(d-a)
elif a<=c<=b and b<=d:
    print(b-c)
else:
    print(0)

# abc071b
import sys
s = input()
s_set = set(s)
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in alpha:
    if i not in s_set:
        print(i)
        sys.exit()
print('None')

# abc072b
s = input()
tmp = ''
for i,j in enumerate(s):
    if i%2 == 0:
        tmp += j
print(tmp)

# abc073b
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
sum = 0
for l in li:
    sum += (l[1] - l[0] + 1)
print(sum)

# abc074b
n = int(input())
k = int(input())
li = list(map(int, input().split()))
center = k//2
sum = 0
for i in li:
    if i <= center:
        sum += i*2
    else:
        sum += (k-i)*2
print(sum)

# abc075b
h, w = map(int, input().split())
matrix = [[x for x in input()] for y in range(h)]

def check_surround(matrix, x, y):
    if matrix[x][y] == '#':
        return '#'
    else:
        tmp = []
        tmp += check_index(matrix, x-1, y-1)
        tmp += check_index(matrix, x, y-1)
        tmp += check_index(matrix, x+1, y-1)
        tmp += check_index(matrix, x-1, y)
        tmp += check_index(matrix, x+1, y)
        tmp += check_index(matrix, x-1, y+1)
        tmp += check_index(matrix, x, y+1)
        tmp += check_index(matrix, x+1, y+1)
        return str(str(tmp).count('#'))

def check_index(matrix, x, y):
    if x > -1 and y > -1:
        try:
            return matrix[x][y]
        except:
            return str(0)
    else:
        return str(0)

for ri in range(h):
    s = ''
    for ni in range(w):
        s += check_surround(matrix, ri, ni)
    print(s)

# abc076b
import math
n = int(input())
k = int(input())
l = int(math.log2(k))
a_count = min(n, l+1)
b_count = max(0, n-a_count)
print(2**a_count + k*b_count)

# abc077b
import math
import sys
n = int(input())
for i in range(n, 0, -1):
    s = math.sqrt(i)
    if s == int(s):
        print(i)
        sys.exit()

# abc078b
x, y, z = map(int, input().split())
space = x - y - 2*z
a = space // (y+z)
print(a+1)

# abc079b
n = int(input())
def cal(a,b,count):
    tmp = 0
    while count > 1:
        count -= 1
        su = a+b
        a = b
        b = su
        tmp = su
    return tmp
if n == 1:
    print(1)
else:
    print(cal(2, 1, n))

## 別解(再帰関数)
n = int(input())
def cal(a,b,count):
    if count == 2:
        return a+b
    else:
        return cal(b, a+b, count-1)
if n == 1:
    print(1)
else:
    print(cal(2, 1, n))

## 別解(配列要素追加)
n = int(input())
if n == 1:
    print(1)
li = [2,1]
for i in range(2,n+1):
    li.append(li[i-2]+li[i-1])
print(li[n])

# abc080b
n = input()
li = [int(_) for _ in n]
if int(n)%sum(li) == 0:
    print('Yes')
else:
    print('No')

# abc081b
import math
import sys
n = int(input())
li = list(map(int, input().split()))
tmp = []
for i in li:
    count = 0
    while i%2 == 0:
        count += 1
        i = i/2
    tmp.append(count)
print(min(tmp))

# abc082b
# 下記は解説見て記述
s = input()
t = input()
s_sorted = ''.join(sorted(s))
t_sorted = ''.join(sorted(t, reverse=True))
if s_sorted < t_sorted:
    print('Yes')
else:
    print('No')

# abc083b
n, a, b = map(int,input().split())
all_sum = 0
for i in range(1,n+1):
    i_li = list(str(i))
    #print(i_li)
    sum = 0
    for i_li_element in i_li:
        sum += int(i_li_element)
    if a<=sum<=b:
        all_sum += i
print(all_sum)

# abc084b
import sys
a, b = map(int, input().split())
s = input()
if len(s) != a+b+1:
    print('No')
    sys.exit()

def check_hi(index,str):
    tmp = []
    for i,st in enumerate(str):
        if st == '-':
            tmp.append(i)
    if len(tmp)==1 and tmp[0]==index:
        return True
    else:
        return False

def check_int(i):
    if i == '-' or int(i) in [0,1,2,3,4,5,6,7,8,9]:
        return True
    else:
        return False

if check_hi(a,s) == False:
    print('No')
    sys.exit()

for si in s:
    if check_int(si) == False:
        print('No')
        sys.exit()
else:
    print('Yes')
# ↑Sは0以上9以下の数字、およびハイフン-からなる、という条件を無視していた

# abc085b
n = int(input())
li = [int(input()) for _ in range(n)]
se = set(li)
print(len(se))

# abc086b
import math
src = input().split()
new = int(''.join(src))
if int(math.sqrt(new)) == math.sqrt(new):
    print('Yes')
else:
    print('No')

# abc087b
a = int(input())
b = int(input())
c = int(input())
x = int(input())
count = 0
for ai in range(a+1):
    for bi in range(b+1):
        for ci in range(c+1):
            if 500*ai+100*bi+50*ci == x:
                count += 1
print(count)

# abc088b
n = int(input())
src = list(map(int, input().split()))
a = 0
b = 0
srt = sorted(src, reverse=True)
for i,s in enumerate(srt):
    if i%2 == 0:
        a += s
    else:
        b += s
print(a-b)

# abc089b
n = int(input())
src = list(input().split())
kind = set(src)
if len(kind) == 3:
    print('Three')
else:
    print('Four')

# abc090b
a, b = map(int, input().split())
count = 0
for i in range(a,b+1):
    if i == int(''.join(list(reversed(str(i))))):
        count += 1
print(count)

# abc091b
n = int(input())
s_li = [input() for i in range(n)]
m = int(input())
t_li = [input() for i in range(m)]
tmp_map = {}
for s in s_li:
    if s not in tmp_map:
        tmp_map[s] = 1
    else:
        tmp_map[s] +=1
for m in t_li:
    if m not in tmp_map:
        tmp_map[m] = -1
    else:
        tmp_map[m] -=1
print(max(tmp_map.values()) if max(tmp_map.values())>0 else 0)

# abc092b
n = int(input())
d, x = map(int, input().split())
src = [int(input()) for _ in range(n)]
count = 0
for s in src:
    count += (d - 1)//s + 1
print(count+x)

# abc093b
a,b,k = map(int,input().split())
if k > b-a+1:
    k = b-a+1
li = set()
for i in range(k):
    li.add(a+i)
    li.add(b-i)
for l in sorted(li):
    print(l)

# abc094b
k, m, x = map(int, input().split())
src = list(map(int, input().split()))
big = len(list(filter(lambda l: l>x, src)))
small = len(list(filter(lambda l: l<x, src)))
print(min(big,small))

# abc095b
n, x = map(int, input().split())
src = [int(input()) for _ in range(n)]
print((x - sum(src))//min(src) + n)

# abc096b
a,b,c = map(int,input().split())
k = int(input())
src_sum = a+b+c
src_max = max(a,b,c)
print(src_max*(2**k)+src_sum-src_max)

# abc097b
import math
import sys
x = int(input())
for i in range(x,0,-1):
    for j in range(x,0,-1):
        for k in range(10,1,-1):
            if i == j**k:
                print(i)
                sys.exit()

# abc098b
n = int(input())
s = input()
newlist = []
for ni in range(n):
    newlist.append([s[0:ni+1],s[ni+1:n]])
count = 0
for n in newlist:
    if len(set(n[0]) & set(n[1]))>count:
        count = len(set(n[0]) & set(n[1]))
print(count)

# abc099b
a, b = map(int,input().split())
a_len = sum([_ for _ in range(b-a)])
print(a_len-a)

# abc100b
d,n = map(int,input().split())
if d == 0:
    if n == 100:
        print(101)
    else:
        print(n)
elif d == 1:
    if n == 100:
        print(10100)
    else:
        print(n*100)
elif d == 2:
    if n == 100:
        print(1010000)
    else:
        print(n*10000)

# abc101b
n = input()
src = list(n)
count = 0
for s in src:
    count += int(s)
if int(n) % count == 0:
    print('Yes')
else:
    print('No')

# abc102b
n = int(input())
src = list(map(int, input().split()))
print(max(src)-min(src))

# abc103b
import sys
s = list(input())
t = list(input())
if s == t:
    print('Yes')
    sys.exit()
for si in range(len(s)+1):
    before = s[0:si+1]
    after = s[si+1:len(s)+1]
    if after + before == t:
        print('Yes')
        sys.exit()
print('No')

# abc104b
import sys
def check_small(string):
    if string in 'abcdefghijklmnopqrstuvwxyz':
        return True
    else:
        return False

s = input()
if s[0] != 'A':
    print('WA')
    sys.exit()
if check_small(s[-1]) == False:
    print('WA')
    sys.exit()
count = 0
for si in s[3:]:
        if si == 'C':
            count += 1
        elif check_small(si) == False:
            print('WA')
            sys.exit()
print('AC' if count == 1 else 'WA')

# abc105b
import math
import sys
n = int(input())
max7 = math.ceil(n / 7)
for m in range(max7+1):
    if (n-7*m) >= 0 and (n-7*m)%4 == 0:
        print('Yes')
        sys.exit()
print('No')

# abc106b
n = int(input())
count = 0
for ni in range(1,n+1):
    if ni%2 == 1:
        nj_count = 0
        for nj in range(1,ni+1):
            if ni%nj == 0:
                nj_count += 1
        if nj_count == 8:
            count += 1
print(count)

# abc107b
h,w = map(int,input().split())
src = [input() for _ in range(h)]
li = []
for i,z in enumerate(src[0]):
    if z == '.':
        li.append(i)
eliminate_column_index = []
for l in li:
    tmp = True
    for s in src:
        if s[l] == '#':
            tmp = False
            break
    if tmp == True:
        eliminate_column_index.append(l)
eliminate_row_index = []
for si,sr in enumerate(src):
    if sr == '.'*w:
        eliminate_row_index.append(si)
for s_row,ss in enumerate(src):
    if s_row in eliminate_row_index:
        continue
    tmp = ''
    for i,s in enumerate(ss):
        if i not in eliminate_column_index:
            tmp += s
    if tmp != '':
        print(tmp)

# abc109b
import sys
n = int(input())
src = [input() for _ in range(n)]
tmp = ''
for i,s in enumerate(src):
    if i == 0:
        tmp = s[-1]
    else:
        if s[0] != tmp:
            print('No')
            sys.exit()
        tmp = s[-1]
if len(src) != len(set(src)):
    print('No')
    sys.exit()
print('Yes')

# abc110b
import sys
n,m,x,y = map(int,input().split())
x_li = list(map(int,input().split()))
y_li = list(map(int,input().split()))
for z in range(x+1,y+1):
    if z>x and z>max(x_li) and z<=y and z<=min(y_li):
        print('No War')
        sys.exit()
else:
    print('War')

# abc111b
n = input()
li = list(n)
same = li[0]*len(li)
if int(n) <= int(same):
    print(same)
else:
    print(str(int(li[0])+1)*len(li))

# abc112b
import sys
n, t = map(int,input().split())
src = [list(map(int,input().split())) for _ in range(n)]
new = []
for s in src:
    if s[1] <= t:
        new.append(s[0])
if len(new) == 0:
    print('TLE')
    sys.exit()
print(min(new))

# abc113b
import math
n = int(input())
t, a = map(int,input().split())
src = list(map(int,input().split()))
new = []
for s in src:
    new.append(math.fabs(t-s*0.006-a))
print(new.index(min(new))+1)

# abc114b
import math
s = input()
li = []
for i in range(len(s)-2):
    tmp = int(s[i:i+3])
    li.append(math.fabs(tmp-753))
print(int(min(li)))

# abc115b
n = int(input())
src = [int(input()) for _ in range(n)]
sorted_src = sorted(src)
sorted_src[-1] = sorted_src[-1]/2
print(int(sum(sorted_src)))

# abc116b
import sys
n = int(input())
def calc(x):
    if x%2 == 0:
        return int(x/2)
    else:
        return 3*x+1
li = [n]
flg = 0
ans = n
count = 1
while flg == 0:
    ans = calc(ans)
    if ans in li:
        print(count+1)
        flg += 1
        sys.exit()
    else:
        li.append(ans)
        count += 1

# abc117b
n = int(input())
src = list(map(int,input().split()))
m = max(src)
if m < sum(src)-m:
    print('Yes')
else:
    print('No')

# abc118b
n, m = map(int, input().split())
src_all = [input().split() for _ in range(n)]
# src = [['2', '1', '3'], ['3', '1', '2', '3'], ['2', '3', '2']]
tmp = {}
for src in src_all:
    for i,s in enumerate(src):
        if i != 0:
            if s in tmp:
                tmp[s] += 1
            else:
                tmp[s] = 1
count = 0
for t in tmp.values():
    if t == n:
        count +=1
print(count)

# abc119b
n = int(input())
src = [input().split() for _ in range(n)]
count = 0
for s in src:
    if s[1] == 'JPY':
        count += float(s[0])
    else:
        count += float(s[0])*380000
print(count)

# abc120b
import math
a,b,k = map(int,input().split())
m = min(a,b)
li = []
for mi in range(1,m+1):
    if a%mi == 0 and b%mi == 0:
        li.append(mi)
print(li[-k])

# abc121b
n,m,c = map(int,input().split())
b_li = list(map(int, input().split()))
a_li = [list(map(int,input().split())) for _ in range(n)]
count = 0
for each in a_li:
    su = c
    for a,b in zip(each,b_li):
        su += a*b
    if su > 0:
        count += 1
print(count)

# abc122b
s = input()
l = len(s)
li = [0]
for i in range(l):
    for j in range(l-i):
        if all([k in ['A','C','G','T'] for k in list(s[i:i+j+1])]):
            li.append(len(s[i:i+j+1]))
print(max(li))

# abc123b
import math
src = [input() for _ in range(5)]
k_li = []
v_li = []
sum = 0
for s in src:
    if int(s[-1]) != 0:
        k_li.append(int(s[-1]))
        v_li.append(int(s))
    else:
        sum += int(s)
flag = False
if len(k_li)>0:
    m = min(k_li)
    for k,v in zip(k_li,v_li):
        if k == m and flag == False:
            sum += v
            flag = True
        else:
            sum += math.ceil(v/10)*10
print(sum)

# abc124b
n = int(input())
src = list(map(int, input().split()))
m = src[0]
count = 0
for s in src:
    if s >= m:
        count += 1
        m = s
print(count)

# abc125b
n = int(input())
v_src = list(map(int, input().split()))
c_src = list(map(int, input().split()))
count = 0
for v,c in zip(v_src,c_src):
    if v-c>0:
        count += v-c
print(count)

# abc126b
s = input()
before = s[0:2]
after = s[2:4]

b = 0<int(before)<13
a = 0<int(after)<13

if a and b:
    print('AMBIGUOUS')
elif a and not b:
    print('YYMM')
elif b and not a:
    print('MMYY')
else:
    print('NA')

# abc127b
r,d,x = map(int,input().split())
for _ in range(10):
    print(r*x - d)
    x = r*x - d

# abc128b
n = int(input())
li = [input().split() for _ in range(n)]
#print(src)
#[['khabarovsk', '20'], ['moscow', '10'], ['kazan', '50'], ['kazan', '35'], ['moscow', '60'], ['khabarovsk', '40']]
key_li = []
for l in li:
    if l[0] not in key_li:
        key_li.append(l[0])
dict = {}
sorted_ki = sorted(key_li)
for i,s in enumerate(sorted_ki):
    dict[i] = []
    for j,l in enumerate(li):
        if s == l[0]:
            dict[i].append([int(l[1]),j])
fin_li = []
for k in range(len(dict)):
    each_li = []
    for d in dict[k]:
        if d not in each_li:
            each_li.append(d[0])
    s_e_li = sorted(each_li, reverse=True)
    for s_e in s_e_li:
        for d in dict[k]:
            if s_e == d[0]:
                fin_li.append(d[1]+1)
for f in fin_li:
    print(f)

# abc129b
n = int(input())
src = list(map(int,input().split()))
sum_src = sum(src)
li = []
left = 0
for i,s in enumerate(src):
    if i != len(src)-1:
        left += s
        li.append(abs(sum_src - left*2))
print(min(li))

# abc130b
n, x = map(int, input().split())
src = list(map(int, input().split()))
li = [0]
h = 0
for s in src:
    h += s
    if h <= x:
        li.append(h)
print(len(li))

#abc131b
import math
n, l = map(int, input().split())
fabs_lis = []
true_lis = []
for i in range(n):
    fabs_lis.append(math.fabs(i+l))
    true_lis.append(i+l)
index = fabs_lis.index(min(fabs_lis))
print(sum(true_lis)-true_lis[index])

# abc132b
n = input()
src = list(map(int, input().split()))
count = 0
for i in range(len(src)-2):
    if src[i]<src[i+1]<src[i+2]:
        count += 1
new_li = list(reversed(src))
for n in range(len(new_li)-2):
    if new_li[n]<new_li[n+1]<new_li[n+2]:
        count += 1
print(count)

# abc108b
a,b,c,d = map(int,input().split())
x = c - a
y = d - b
x3 = c - y
y3 = d + x
x4 = a - y
y4 = b + x
print(x3,y3,x4,y4)

### 以下はABC200点相当なのでB問題とする
# AGC001a
import heapq
n = int(input())
src = list(map(int, input().split()))
sorted_src = sorted(src)
heapq.heapify(sorted_src)
count = 0
for i in range(n):
    a = heapq.heappop(sorted_src)
    heapq.heappop(sorted_src)
    count += a
print(count)

# AGC002a
a,b = map(int,input().split())
if a > 0:
    print('Positive')
    sys.exit()
if b >= 0:
    print('Zero')
    sys.exit()
if (b-a+1)%2 == 1:
    print('Negative')
else:
    print('Positive')

# AGC003a
src = input()
a = False
b = False
c = False
d = False
for s in src:
    if s == 'N':
        a = True
    elif s == 'W':
        b = True
    elif s == 'S':
        c = True
    elif s == 'E':
        d = True
if a != c or b != d:
    print('No')
else:
    print('Yes')
    
# AGC004a
a,b,c = map(int,input().split())
if a*b*c%2 == 0:
    print(0)
else:
    sorted_src = sorted([a,b,c])
    print(sorted_src[0]*sorted_src[1])

# AGC006a
import sys
n = int(input())
s = input()
t = input()
same_count = 0
for i in range(n):
    if s[n-1-i:] == t[:i+1]:
        same_count = i+1
print(2*n-same_count)

# AGC015a
import sys
n, a, b = map(int,input().split())
if a == b and n == 1:
    print(1)
    sys.exit()
elif a > b or n == 1:
    print(0)
    sys.exit()
print((b - a)*(n - 2) + 1)

# AGC017a
n, p = map(int,input().split())
src = list(map(int, input().split()))
even_count = 0 #偶数
odd_count = 0 #奇数
for s in src:
    if s%2 == 0:
        even_count += 1
    else:
        odd_count += 1
if p == 1 and odd_count == 0:
    print(0)
elif odd_count == 0:
    print(2**even_count)
else:
    print(2**even_count*2**(odd_count-1))
    