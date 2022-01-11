n = int(input())

ans = 0
for i in range(1, n + 1):
    cnt = 0
    while i % 2 != 0:
        i = i // 2
        cnt += 1
    if ans >= cnt:
        ans = cnt
print(2 ** ans)
