import math

p = float(input())

def cal(x):
    return 1 - (2 / 3) * p * math.log(2) * 2 ** ((-2 / 3) * x)
def cal2(x):
    return x + p / (2 ** (x / 1.5))

f_0 = cal(0)
INF = 10 ** 18
left = 0; right = INF
result = 10 ** 18
while abs(result) > 10 ** (-8):
    mid = (left + right) / 2
    result = cal(mid)
    if result > 0:
        right = mid
    else:
        left = mid
    if abs(result - f_0) < 10 ** (-8):
        result = f_0
        break
print(min(cal2(right), cal2(0)))
