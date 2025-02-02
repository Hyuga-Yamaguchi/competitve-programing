import math

n = int(input())
x = list(map(int, input().split()))

m = 0
for i in range(n):
    m += abs(x[i])
print(m)
y = 0
for i in range(n):
    y += x[i] ** 2
print(math.sqrt(y))

c = 0
for i in range(n):
    if abs(x[i]) >= c:
        c = abs(x[i])
print(c)
