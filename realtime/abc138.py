#abc3完。dを飛ばしてeを着手したが半分WAで通らず。
# a
a = int(input())
s = input()
if a >= 3200:
    print(s)
else:
    print('red')

# b
n = int(input())
li = list(map(int,input().split()))
gyaku = sum([1/_ for _ in li])
print(1/gyaku)

# c
n = int(input())
li = list(map(int,input().split()))
sorted_li = sorted(li)
new_li = []
for i in range(n):
    if i == 0:
        new_li.append(sorted_li[0]/(2**(n-1)))
    else:
        new_li.append(sorted_li[i]/(2**(n-i)))
print(sum(new_li))

######################
# e(メモ用。正解ではない)
######################
import sys
s = input()
s_li = [_ for _ in s]
t = input()
for ti in t:
    if ti not in s:
        print(-1)
        sys.exit()
new_li = []
for ti in t:
    tmp_li = []
    new_li.append([i for i, s in enumerate(s_li) if s == ti])
# print(new_li)
# nnsgton son
# [[2], [5], [0, 1, 6]]
 
real_li = []
for i,ni in enumerate(new_li):
    if i == 0:
        real_li.append(min(ni))
    else:
        filtered = list(filter(lambda x: x > real_li[i-1], ni))
        if len(filtered)>0:
            real_li.append(min(filtered))
        else:
            real_li.append(min(ni))
 
count = 0
for ni,n in enumerate(real_li[:len(real_li)-1]):
    if real_li[ni]>real_li[ni+1]:
        count += 1
score = count*len(s)+real_li[-1]+1
print(score)
import sys
s = input()
s_li = [_ for _ in s]
t = input()
for ti in t:
    if ti not in s:
        print(-1)
        sys.exit()
new_li = []
for ti in t:
    tmp_li = []
    new_li.append([i for i, s in enumerate(s_li) if s == ti])
# print(new_li)
# nnsgton son
# [[2], [5], [0, 1, 6]]

real_li = []
for i,ni in enumerate(new_li):
    if i == 0:
        real_li.append(min(ni))
    else:
        filtered = list(filter(lambda x: x > real_li[i-1], ni))
        if len(filtered)>0:
            real_li.append(min(filtered))
        else:
            real_li.append(min(ni))

count = 0
for ni,n in enumerate(real_li[:len(real_li)-1]):
    if real_li[ni]>real_li[ni+1]:
        count += 1
score = count*len(s)+real_li[-1]+1
print(score)
