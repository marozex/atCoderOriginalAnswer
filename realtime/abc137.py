# ab2完
# a
a, b = map(int, input().split())
print(max(a+b,a-b,a*b))

# b
k,x = map(int, input().split())
mi = x - k + 1
ma = x + k - 1
t_min = max(mi, -1000000)
t_max = min(ma, 1000000)
L = list(range(t_min, t_max+1))
arr = [str(i) for i in L]
arr=' '.join(arr)
print(arr)

##### 追記
#c(解説見てから書いた)
from math import factorial
n = int(input())
src = [''.join(sorted(input())) for _ in range(n)]
dic = {}
for s in src:
    # 辞書にキーが存在しなければキー追加
    if s not in dic:
        dic[s] = 1
    else:
        dic[s] += 1
count = 0
# 辞書から値だけ取り出す
for d in dic.values():
    # dまでの値の組み合わせを合計する
    if d > 2:
        # factorial(n)でnの階乗を求める
        count += factorial(d) // 2 // factorial(d - 2)
    elif d == 2:
        count += 1
print(count)
