# abc141d 
# heapq
import heapq
import math
n, m = map(int, input().split())
src = list(map(int, input().split()))
new_src = []
for s in src:
    new_src.append(s*-1)
heapq.heapify(new_src)

def waru(heap):
    tmp = heapq.heappop(heap)
    heapq.heappush(heap, math.ceil(tmp / 2))
    return heap
for _ in range(m):
    new_src = waru(new_src)
print(sum(new_src)*-1)

# abc103d TLE
#↓TLE
import sys
n,m = map(int,input().split())
lis = [list(map(int,input().split())) for _ in range(m)]
fin_count = 0
flag = True
while flag == True:
    counter = [0]*(n-1)
    for l in lis:
        for i in range(l[0]-1,l[1]-1):
            counter[i] += 1
    #print(counter)
    #print('↑counter')
    #print(counter.index(max(counter)))
    mi = counter.index(max(counter))
    #print(mi)
    #print('入る前')
    fin_count += 1
    tmp = []
    for li,l in enumerate(lis):
        #print(lis)
        #print('↑lis')
        #print(l[0]-1,mi,l[1]-1,l)
        #print('↑l[0]-1,mi,l[1]-1,l)')
        if l[0]-1 > mi or mi >= l[1]-1:
            tmp.append(l)
            #print(lis)
            #print('↑削除後')
    if len(tmp) == 0:
        print(fin_count)
        sys.exit()
    lis = tmp
#↑TLE