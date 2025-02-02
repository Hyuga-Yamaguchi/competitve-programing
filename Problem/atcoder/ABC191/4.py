from decimal import Decimal
import math

x, y, r = map(Decimal, input().split())
#print(x, y, r)

x_min = math.ceil(x - r)
x_max = math.floor(x + r)
#print(x_min, x_max)
#print(type(x_min))

cnt = 0
for i in range(x_min, x_max + 1):
    l = r ** 2 - (i - x) ** 2
    l = l.sqrt()
    y_max = math.floor(y + l)
    if (i - x) ** 2 + (y_max - y) ** 2 > r ** 2:
        y_max -= 1
    y_min = math.ceil(y - l)
    if (i - x) ** 2 + (y_min - y) ** 2 > r ** 2:
        y_min -= 1
    cnt += y_max - y_min + 1
print(cnt)
