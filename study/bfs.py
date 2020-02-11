# abc088 D 
# https://atcoder.jp/contests/abc088/tasks/abc088_d

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
dp = [[0]*(w+2) for _ in range(h+2)]

#(開始x,開始y)
step = [[1,1]]
while len(step)>0:
    x,y = step.pop(0)

    if x == h and y == w:
        print(road_count-dp[x][y]-1)
        exit()

    #探索済みのところは、#にする
    lis[x][y] = '#'

    '''
    and以下の条件がないと、すでにキューに追加済みの宛先に重複してたどり着く
    例えばlis[3][3]はlis[3][2]とlis[2][3]どちらからも行けてしまう。
    lis[2][3]から行こうとしたとき、lis[3][3]は'.'だが、
    dp[3][3]にはすでに4がセットされている
    '''
    if lis[x-1][y] != '#' and dp[x-1][y] == 0:
        step.append([x-1,y])
        dp[x-1][y] = dp[x][y]+1
    if lis[x+1][y] != '#' and dp[x+1][y] == 0:
        step.append([x+1,y])
        dp[x+1][y] = dp[x][y]+1
    if lis[x][y-1] != '#' and dp[x][y-1] == 0:
        step.append([x,y-1])
        dp[x][y-1] = dp[x][y]+1
    if lis[x][y+1] != '#' and dp[x][y+1] == 0:
        step.append([x,y+1])
        dp[x][y+1] = dp[x][y]+1
print(-1)