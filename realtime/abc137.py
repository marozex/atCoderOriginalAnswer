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