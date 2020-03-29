# トリボナッチ数列
# abc006b
# https://atcoder.jp/contests/abc006/tasks/abc006_2

# 下記のように再起だとTLEする
import sys
sys.setrecursionlimit(200000000)
n = int(input())
def Fib(n):    
    if n == 1:
        return 0
    elif n == 2:
        return 0
    elif n == 3:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)+Fib(n-3)
print(Fib(n)%10007)

# 下記のようにすればTLE回避できる
n = int(input())
def Fib(n):
    a, b, c = 0, 0, 1
    if n == 1:
        return a
    elif n == 2:
        return b
    elif n == 3:
        return c
    else:
        for _ in range(n-2):
            a, b, c = b, c, (a + b + c)%10007
        return b
print(Fib(n))
