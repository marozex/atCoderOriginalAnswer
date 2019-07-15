# AtCoder B問題の自作解答

# abc044

input = input()
import string
al = string.ascii_lowercase
for a in al:
    tmp = ""
    for i in input:
        if i==a:
            tmp+=i
    if(len(tmp)%2 == 1):
        print("No")
        exit()
print("Yes")


# abc046
N, K = map(int, input().split())
print(K * (K-1)**(N-1))

# abc047
x, y, n = map(int, input().split())
input = [list(map(int, input().split())) for _ in range(n)] 
xmax = x
xmin = 0
ymax = y
ymin = 0
for i in input:
    type = i[2]
    if type == 1 and (i[0] > xmin):
        xmin = i[0]
    elif type == 2 and (i[0] < xmax):
        xmax = i[0]
    elif type == 3 and (i[1] > ymin):
        ymin = i[1]
    elif type == 4 and (i[1] < ymax):
        ymax = i[1]
if (xmax > xmin) and (ymax > ymin):
    print((xmax - xmin)*(ymax - ymin))
else:
    print(0)