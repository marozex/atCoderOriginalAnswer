#abcd4完
# a
a = int(input())
b = int(input())
li = [1,2,3]
for i in li:
    if i != a and i != b:
        print(i)

# b
n = int(input())
s,t = input().split()
#print(s)
#print(t)
target = ''
for si,ti in zip(s,t):
    target += si
    target += ti
print(target)

# c
a,b = map(int, input().split())
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b // gcd (a, b)
print(lcm(a,b))

# d
n = int(input())
lis = list(map(int, input().split()))
search_target = 1
founded = 0
for li in lis:
    #search_target = 1
    if li == search_target:
        search_target += 1
        founded = li
        continue
    else:
        continue
if founded == 0:
    print(-1)
else:
    print(n-founded)
