n = int(input())
a = list(map(int, input().split()))


ans = 0
for i in range(10 ** 5 + 1):
    a = sorted(a)
    if a[-1] != a[0]:
        a[-1] = a[-1] - a[0]
    elif a[-1] == a[0]:
        ans = a[-1]
        break
print(ans)
