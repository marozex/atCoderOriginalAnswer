# abcd 4完
# a
n,m = map(int,input().split())
a=n+m
print(int(a*((a-1)/2)-n*m))

# b
s = input()
flag = True
l = len(s)
if s != s[::-1]:
    flag = False
    #print('a')
#print(s,s[::-1])
if s[:(l-1)//2] != s[:(l-1)//2][::-1]:
    flag = False
    #print('b')
#print(s[:(l-1)//2],s[:(l-1)//2][::-1])
if s[(l+3)//2-1:] != s[(l+3)//2-1:][::-1]:
    flag = False
    #print('c')
#print(s[(l+3)//2-1:],s[(l+3)//2-1:][::-1])
if flag:
    print('Yes')
else:
    print('No')

# c
l = int(input())
print((l/3)**3)

# d
n = int(input())
li = list(map(int,input().split()))
ma = {}
for l in li:
    if l in ma:
        ma[l] += 1
    else:
        ma[l] = 1
all_sum = 0
for m in ma.values():
    if all_sum == 0 and m >= 2:
        all_sum = m*(m-1)//2
    elif m >= 2:
        all_sum = all_sum + m*(m-1)//2
for l in li:
    if ma[l] >=2:
        tmp_sum = all_sum - (ma[l]*(ma[l]-1)//2)
        if ma[l] >=3:
            tmp_sum += ((ma[l]-1)*(ma[l]-2)//2)
        print(tmp_sum)
    else:
        print(all_sum)
