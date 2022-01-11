from decimal import Decimal
a, b = map(float, input().split())

a = Decimal(str(a))
b = Decimal(str(b))

print(int(a * b))
