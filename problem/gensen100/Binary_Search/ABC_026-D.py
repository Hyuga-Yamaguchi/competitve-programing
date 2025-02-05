import math

a, b, c = map(int, input().split())

def func(t):
    return a * t + b * math.sin(c * t * math.pi)

INF = 10 ** 18
left = 0; right = INF
result = 10 ** 18
while abs(result - 100) > 10 ** (-10):
    mid = (left + right) / 2
    result = func(mid)
    if result > 100:
        right = mid
    else:
        left = mid
print(right)
