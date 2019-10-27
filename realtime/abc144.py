# abc3完 dは最後のテストだけ通らず
# a
a,b = map(int, input().split())
if a <= 9 and b <= 9:
    print(a*b)
else:
    print('-1')

# b
li = [
    1,2,3,4,5,6,7,8,9,
    4,6,8,10,12,14,16,18,
    9,12,15,18,21,24,27,
    16,20,24,28,32,36,
    25,30,35,40,45,
    36,42,48,54,
    49,56,63,
    64,72,
    81]
n = int(input())
if n in li:
    print('Yes')
else:
    print('No')

# c
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    #divisors.sort()
    return divisors

n = int(input())
lis = make_divisors(n)
print(lis[-1]+n//lis[-1]-2)

#参考 d WA。通ってない
import math
a,b,x = map(int,input().split())
if x / a > (a*b/2):
    print(math.degrees(math.atan((2*b/a)-2*x/(a**3))))
else:
    if a <= b:
        print(math.degrees(math.atan(a*b*b/(2*x))))
    else:
        print(math.degrees(math.atan(2*x/(a*b*b))))

