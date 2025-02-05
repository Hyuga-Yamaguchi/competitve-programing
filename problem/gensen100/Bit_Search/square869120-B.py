import copy

n, k = map(int, input().split())
a = list(map(int, input().split()))
INF = 10 ** 12

ans = INF
lis = [False] * n
for bit in range(1 << n):
    for i in range(1, n):
        if (bit >> i) & 1:
            lis[i] = True
        else:
            lis[i] = False
    #print(lis)
    cur = 0
    b = copy.copy(a)
    for i in range(n):
        if lis[i] == True:
            if max(b[:i]) >= b[i]:
                cur += max(b[:i]) + 1 - b[i]
                b[i] = max(b[:i]) + 1
            #print(cur)
    cnt = 1
    #print(b)
    for j in range(1, n):
        if b[j] > max(b[:j]):
            cnt += 1
    if cnt >= k:
        ans = min(ans, cur)

print(ans)
