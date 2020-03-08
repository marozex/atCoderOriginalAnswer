#ab2完
#a
s = input()
x = len(s)//2
if s == 'hi' * x:
    print('Yes')
else:
    print('No')
#b
a,b,m = map(int, input().split())
a_lis = list(map(int, input().split()))
b_lis = list(map(int, input().split()))
ans_lis = [min(a_lis)+min(b_lis)]
for _ in range(m):
    x,y,z = map(int, input().split())
    tmp = a_lis[x-1]+b_lis[y-1]-z
    ans_lis.append(tmp)
print(min(ans_lis))
