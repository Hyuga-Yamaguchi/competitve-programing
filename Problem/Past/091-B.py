from collections import Counter

ans = 0

n = int(input())
s = list(input() for _ in range(n))
m = int(input())
t = list(input() for _ in range(m))

s = list(Counter(s).items())
t = list(Counter(t).items())

print(s, t)
