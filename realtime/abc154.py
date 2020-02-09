#abc3完 dは一生TLE
#a
s,t = input().split()
a,b = map(int,input().split())
u = input()
if s == u:
    print(a-1,b)
else:
    print(a,b-1)

#b
s = input()
print('x'*len(s))

#c
n = int(input())
lis = list(map(int,input().split()))
se = set(lis)
if len(lis) == len(se):
    print('YES')
else:
    print('NO')
