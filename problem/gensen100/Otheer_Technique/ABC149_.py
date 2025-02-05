a, b, k = map(int, input().split())

if a >= k:
    print(a - k, b)
else:
    c = k - a
    print(0, max(b - c, 0))
