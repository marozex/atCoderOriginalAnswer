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