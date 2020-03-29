# abcd4完
# a
s = input()
l = list(s)
if l[2] == l[3] and l[4] == l[5]:
    print('Yes')
else:
    print('No')

# b
x = int(input())
a = x // 500
y = x - a*500
b = y // 5
print(a*1000+b*5)

# c
k,n = map(int,input().split())
ll = list(map(int,input().split()))
tmp = [k-ll[-1]+ll[0]]
#print(tmp)
for i,l in enumerate(ll):
    if i == 0:
        continue
    tmp.append(ll[i]-ll[i-1])
#print(tmp)
m = max(tmp)
print(k-m)

# d
n,x,y = map(int,input().split())
l = [0]*(n-1)
for i in range(1,n):
    for j in range(i+1,n+1):
        #print(i,j)
        '''
        1 2,1 3,1 4
        2 3,2 4
        3 4
        '''
        if i<=x and j>=y:
            dis = min(j-i,x-i +1+ j-y)
            l[dis-1] += 1
            #print(i,j,dis-1)
        elif i>=x and j<=y:
            dis = min(j-i,i-x+y-j+1)
            l[dis-1] += 1
        elif i<=x and x<=j<=y:
            dis = min(j-i,x-i+y-j+1)
            l[dis-1] += 1
        elif x<=i<=y and j>=y:
            dis = min(j-i,i-x+j-y+1)
            l[dis-1] += 1
        elif i<=x and j<=x:
            dis = j-i
            l[dis-1] += 1
        elif i>=y and j>=y:
            dis = j-i
            l[dis-1] += 1
for kkk in l:
    print(kkk)
