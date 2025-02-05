import math

ans = 0
for m in range(1, 90):
    if math.gcd(m, 90 - m) == 1:
        ans = max(m * (90 - m), ans)
print(ans)
