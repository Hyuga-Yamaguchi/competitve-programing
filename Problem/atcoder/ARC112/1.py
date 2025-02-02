t = int(input())
for i in range(t):
    l, r = map(int, input().split())
    if r - 2 * l >= 0:
        print((r - l * 2 + 2) * (r - l * 2 + 1) // 2)
    else:
        print(0)
