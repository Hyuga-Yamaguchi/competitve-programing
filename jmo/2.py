import math
from decimal import Decimal

x = 2 * math.sqrt(7)
y = 2 * (math.sqrt(x ** 2) - 1) + math.sqrt(25 + (5 * math.sqrt(x ** 2 - 1) - 2 * x) ** 2 - 4)
z = 5 * x
print(x, y, z)
