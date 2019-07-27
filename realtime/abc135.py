# 結果：３完
# a
a, b = map(int, input().split())
sum = a + b
if sum%2 == 0:
    print(sum//2)
else:
    print("IMPOSSIBLE")

# b
n = int(input())
p_list = list(map(int, input().split()))
p_sorted = sorted(p_list)
count = 0
for i in range(n):
    if p_list[i] != p_sorted[i]:
        count += 1
if count in [0,2]:
    print('YES')
else:
    print('NO')

# c
n = int(input())-1
a = list(map(int, input().split()))
b = list(map(int, input().split()))
count = 0
next = a[n+1]
for i in range(n,-1,-1):
    if b[i]>=(a[i] + next):
        count += a[i]+next
        next = 0
    else:
        if b[i]>= next:
            next = a[i]+next-b[i]
            count += b[i]
        else:
            next = a[i]
            count += b[i]
print(count)
