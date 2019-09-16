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