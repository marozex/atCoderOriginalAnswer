#abc3完
# a
s = input()
if s == 'Sunny':
    print('Cloudy')
elif s == 'Cloudy':
    print('Rainy')
else:
    print('Sunny')

# b
s = input()
count = 0
for si,ss in enumerate(s):
    if si%2 == 1 and ss not in ['L','U','D']:
        count += 1
    if si%2 == 0 and ss not in ['R','U','D']:
        count += 1
if count == 0:
    print('Yes')
else:
    print('No')

# c
n, k, q = map(int, input().split())
src = [int(input()) for _ in range(q)]
base = k-q
lis = [base]*n
#print(lis)
#[0, 0, 0, 0, 0, 0]
for s in src:
    lis[s-1] += 1
for l in lis:
    print('Yes' if l>0 else 'No')
