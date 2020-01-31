n = int(input())
lis = [list(map(int,input().split())) for _ in range(n)]
# print(lis)
# [[10, 40, 70], [20, 50, 80], [30, 60, 90]]
#dp = [lis[0]+[0,0,0]*(n-1)]
#dp[0]=lis[0]
#dp = [lis[0][0]+[0]*(n-2),lis[0][1]+[0]*(n-2),lis[0][2+[0]*(n-2)]
dp = [[lis[0][0]]+[0]*(n-1),[lis[0][1]]+[0]*(n-1),[lis[0][2]]+[0]*(n-1)]
#print(dp)

for j in range(n):
    if j == 0:
        continue
    for i in range(3):
        if i == 0:
            dp[i][j] = max(dp[1][j-1],dp[2][j-1])+lis[j][i]
        if i == 1:
            dp[i][j] = max(dp[0][j-1],dp[2][j-1])+lis[j][i]
        if i == 2:
            dp[i][j] = max(dp[0][j-1],dp[1][j-1])+lis[j][i]

#print(dp)

print(max(dp[0][n-1],dp[1][n-1],dp[2][n-1]))
