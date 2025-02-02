n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(1, len(a)):
    if a[i] <= a[i - 1]:
        ans += abs(a[i] - a[i - 1])
        a[i] = a[i - 1]
    else:
        ans += 0

print(ans)
