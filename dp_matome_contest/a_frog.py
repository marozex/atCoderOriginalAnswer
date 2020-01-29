n = int(input())
lis = list(map(int, input().split()))
dp = [0 for _ in range(n)]
for i,d in enumerate(dp):
    if i == 0:
        continue
    if i == 1:
        dp[1] = abs(lis[1]-lis[0])
        continue
    dp[i] = min((dp[i-2]+abs(lis[i-2]-lis[i])),(dp[i-1]+abs(lis[i-1]-lis[i])))
#print(dp)
print(dp[-1])