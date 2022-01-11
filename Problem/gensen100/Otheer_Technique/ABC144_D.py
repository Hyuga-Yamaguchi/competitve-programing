import math
from decimal import Decimal
a, b, x = map(int, input().split())
if a ** 2 * b >= 2 * x:
    ans = Decimal(str(math.degrees(Decimal(math.atan(a * (b ** 2) / (2 * x))))))
else:
    ans = Decimal(str(math.degrees(Decimal(math.atan((2 * (a ** 2 * b - x) / (a ** 3)))))))

print(ans)
