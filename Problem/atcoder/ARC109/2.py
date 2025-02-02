from decimal import Decimal
n = int(input())

D = Decimal(str(1 + 4 * 2 * (n + 1))) ** Decimal(str(1 / 2))
y = Decimal(str(-1 - D)) / Decimal(2)
x = Decimal(str(-(n + 1) * 2 / y))
#print(x, y)
print(n - int(x) + 1)
