# abcd4完
# a
s, t = input().split()
print(t+s)

# b
a,b,k = map(int,input().split())
a_after = 0
b_after = 0
if a >= k:
    a_after = a - k
    b_after = b
else:
    b_after = b - (k-a) if b - (k-a) >=0 else 0
print(a_after, b_after)

# c
import sys
x = int(input())
def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for xi in range(x,10000000):
    if is_prime(xi):
        print(xi)
        sys.exit()
    else:
        continue

# d
n,k = map(int,input().split())
r,s,p = map(int,input().split())
t = input()
best = ''
for ti in t:
    if ti == 's':
        best += 'r'
    elif ti == 'p':
        best += 's'
    else:
        best += 'p'
lis = [[] for _ in range(k)]
# print(lis)
final_st = ''
for bi,b in enumerate(best):
    lis[bi%k].append(b)
for each_lis in lis:
    each_st = ''
    for e_i,e_lis in enumerate(each_lis):
        if e_i == len(each_lis) - 1:
            if e_i == 0:
                each_st += each_lis[e_i]
            else:
                if each_lis[e_i] != each_lis[e_i - 1]:
                    each_st += each_lis[e_i]
            break
        else:
            if each_lis[e_i] != each_lis[e_i + 1]:
                each_st += each_lis[e_i]
            else:
                each_st += each_lis[e_i]
                each_lis[e_i + 1] = 'x'
    #print(each_st)
    final_st += each_st
#print(lis)
#print(final_st)
final_sum = 0
for f in final_st:
    if f == 'r':
        final_sum += r
    elif f == 's':
        final_sum += s
    elif f == 'p':
        final_sum += p
print(final_sum)
