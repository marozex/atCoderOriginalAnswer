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
