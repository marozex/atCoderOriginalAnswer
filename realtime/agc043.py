# a 1完
h,w = map(int,input().split())

road_count = 0
lis = [list('#'*(w+2))]
for _ in range(h):
    li = input()
    for i in li:
        if i == '.':
            road_count += 1
    li = '#' + li + '#'
    lis.append(list(li))
lis.append(list('#'*(w+2)))

#print(lis)
dp = [[999]*(w+2) for _ in range(h+2)]

if lis[1][1] == '#':
    dp[1][1]=1
else:
    dp[1][1]=0

#print(dp)
#(開始x,開始y)
step = [[1,1]]
while len(step)>0:
    x,y = step.pop(0)
    if x > h:
        continue
    if y > w:
        continue
    #print(x,y)
    if dp[x+1][y] == 999:
        step.append([x+1,y])
        if lis[x+1][y] != '#':
            dp[x+1][y] = min(dp[x][y],dp[x+1][y-1])
        else:
            if lis[x][y] == '#' and lis[x+1][y-1] == '#':
                dp[x+1][y] = min(dp[x][y],dp[x+1][y-1])
            elif lis[x][y] == '#':
                dp[x+1][y] = min(dp[x][y],dp[x+1][y-1]+1)
            elif lis[x+1][y-1] == '#':
                dp[x+1][y] = min(dp[x][y]+1,dp[x+1][y-1])
            else:
                dp[x+1][y] = min(dp[x][y],dp[x+1][y-1])+1
    if dp[x][y+1] == 999:
        step.append([x,y+1])
        if lis[x][y+1] != '#':
            dp[x][y+1] = min(dp[x][y],dp[x-1][y+1])
        else:
            if lis[x][y] == '#' and lis[x-1][y+1] == '#':
                dp[x][y+1] = min(dp[x][y],dp[x-1][y+1])
            elif lis[x][y] == '#':
                dp[x][y+1] = min(dp[x][y],dp[x-1][y+1]+1)
            elif lis[x-1][y+1] == '#':
                dp[x][y+1] = min(dp[x][y]+1,dp[x-1][y+1])
            else:
                dp[x][y+1] = min(dp[x][y],dp[x-1][y+1])+1
#print(lis)
#print(dp)
print(dp[h][w])
