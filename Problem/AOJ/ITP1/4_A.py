from fractions import Fraction

a, b = map(int, input().split())
c = a / b
print(a // b, a % b, f"{c:.15f}")
