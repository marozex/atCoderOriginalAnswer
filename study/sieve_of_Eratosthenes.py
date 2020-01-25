lis = [_ for _ in range(1,201)]
print(lis)

import math
def furui(n):
    if n <= 1:
        return []
    prime = [2] #素数の配列を用意する
    limit = math.sqrt(n) #平方根までを調べれば十分

    data = [i+1 for i in range(2,n+1,2)] #探索する奇数の配列
    while limit > data[0]:
        prime.append(data[0])
        data = [j for j in data if j%data[0] != 0]
    
    return prime + data
    
print(furui(200))