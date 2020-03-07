#abcd4完 dでTLE連発したがなんとか通した
#a
s = input()
if (s == 'AAA') or (s == 'BBB'):
    print('No')
else:
    print('Yes')

#b
n,a,b = map(int,input().split())
x = n//(a+b)
y = n%(a+b)
ans = (x*a)+min(y,a)
print(ans)

#c
import math
# print(math.ceil(float_var)) 切り上げ
# print(math.floor(float_var)) 切り捨て
a,b = map(int,input().split())
a_st = math.ceil(a /0.08) 
a_ed = math.ceil((a+1) /0.08) #含まない
b_st = 10*b
b_ed = 10*(b+1) #含まない
a_lis = list(range(a_st,a_ed))
b_lis = list(range(b_st,b_ed))
aandb = list(set(a_lis) & set(b_lis))
if len(aandb) == 0:
    print('-1')
else:
    print(min(aandb))

#d
s = input()
q = int(input())
rev_flag = False
x_lis = []
y_lis = []
for _ in range(q):
    i = input()
    if i == '1':
        rev_flag = not rev_flag
    else:
        a,b,c = i.split()
        if rev_flag:
            if b == '1':
                #s = s + c
                y_lis.append(c)
            else:
                #s = c + s
                x_lis.append(c)
        else:
            if b == '1':
                #s = c + s
                x_lis.append(c)
            else:
                #s = s + c
                y_lis.append(c)
x = ''.join(reversed(x_lis))
y = ''.join(y_lis)
if rev_flag:
    print(''.join(list(reversed(x+s+y))))
else:
    print(x+s+y)
