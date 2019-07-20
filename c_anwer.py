# abc051c

sx, sy, tx, ty = map(int, input().split())
up = "U" * (ty - sy)
right = "R" * (tx - sx)
down = up.replace("U", "D")
left = right.replace("R", "L")
first = up + right + down + left
second = "LU" + up + right + "RDRD" + down + left + "LU"
print(first+second)