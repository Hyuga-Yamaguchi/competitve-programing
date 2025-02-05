import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

ans = 0
for l in range(n):
    x = a[l]
    for r in range(l, n):
        if x >= a[r]:
            x = a[r]
        if ans <= x * (r - l + 1):
            ans = x * (r - l + 1)
print(ans)
