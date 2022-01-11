n = int(input())
import time
t1 = time.time()
res = n
for i in range(n):
    cur, t = 0, i
    while t > 0:
        cur += t % 6
        t //= 6
    t = n - i
    while t > 0:
        cur += t % 9
        t //= 9
    if res > cur:
        res = cur
t2 = time.time()
print(res)
print(t2 - t1)
