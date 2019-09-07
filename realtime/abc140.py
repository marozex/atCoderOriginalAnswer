# abc3完
# a
n = int(input())
print(n**3)

# b
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
last = -1
sum = 0
for ai in a:
    sum += b[ai-1]
    if ai - last == 1:
        sum += c[ai-2]
    last = ai
print(sum)

# c
n = int(input())
b = list(map(int,input().split()))
src = []
for ni in range(n):
    if ni == 0:
        src.append(b[0])
    elif ni == n-1:
        src.append(b[ni-1])
    else:
        src.append(min(b[ni],b[ni-1]))
print(sum(src))
