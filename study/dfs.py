# atcoder_typical_contest_001
# https://atc001.contest.atcoder.jp/tasks/dfs_a
# pythonは再帰の上限を再設定する必要がある
import sys
sys.setrecursionlimit(1000000)

h,w = map(int,input().split())
lis = [list(input()) for _ in range(h)]
#print(lis)
start = [0,0]
end = [0,0]
for i,l in enumerate(lis):
    for j,ll in enumerate(l):
        if ll == 's':
            start = [i,j]
        elif ll == 'g':
            end = [i,j]
#print(start,end)
ma = [[0]*w for _ in range(h)]
#print(ma)

def dfs(x,y):
    if x<0 or y<0 or x>h-1 or y>w-1:
        return
    elif lis[x][y] == '#' or ma[x][y] == 1:
        return
    else:
        ma[x][y]=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)

dfs(start[0],start[1])
if (ma[end[0]][end[1]]) == 1:
    print('Yes')
else:
    print('No')
