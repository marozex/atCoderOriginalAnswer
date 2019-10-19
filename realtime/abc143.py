# abc3完
# a
a,b = map(int,input().split())
diff = a - b*2
print(diff if diff > 0 else 0)

# b
n = int(input())
src = list(map(int, input().split()))
def calc_sum(tmp_list):
    score = 0
    while len(tmp_list)>1:
        tmp = tmp_list.pop(0)
        for l in tmp_list:
            score += tmp * l
    return score
print(calc_sum(src))

# c
n = int(input())
src = list(input())
count = 0
for i,s in enumerate(src):
    if i == len(src)-1:
        break
    if src[i] == src[i+1]:
        count += 1
print(n - count)
