#abc3完
# a
a,b,c = map(int,input().split())
print(c,a,b)

# b
n,m = map(int,input().split())
lis = list(map(int,input().split()))
s = sum(lis)
s_lis = sorted(lis,reverse=True)[:m]
if min(s_lis) < s /(4*m):
    print('No')
else:
    print('Yes')

# c
n,k = map(int,input().split())
a = n%k
b = abs(a-k)
print(min(a,b))
