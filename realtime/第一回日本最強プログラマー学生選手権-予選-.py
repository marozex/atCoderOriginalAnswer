#A1完
m, d = map(int, input().split())
count = 0
for mi in range(1,m+1):
    for di in range(1,d+1):
        if di > 10 and (di//10)*(di%10) == mi and di//10>1 and di%10>1:
            count += 1
print(count)