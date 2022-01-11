import math

R, B = map(int, input().split())
x, y = map(int, input().split())

ng = 10 ** 18
ok = 0
while ng - ok > 1:
    k = (ng + ok)//2
    if R - k >= 0 and B - k >= 0 and math.floor((R - k) / (x - 1)) + math.floor((B - k) / (y - 1)) >= k:
        ok = k
    else:
        ng = k

print(ok)
