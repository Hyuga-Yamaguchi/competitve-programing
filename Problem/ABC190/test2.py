n, x = map(int, input().split())
lis = [None] * n
for i in range(n):
    lis[i] = int(input())

INF = 10 ** 10
u = [INF] * (n + 1)
for bit in range(1 << n):
    lis2 = [0] * n
    for i in range(n):
        if (bit >> i) & 1:
            lis2[i] += 1
    #print(lis2)
    for i in range(n + 1):
        if sum(lis2) == i:
            cost = 0
            for j in range(n):
                cost += lis[j] * lis2[j]
            if x - cost >= 0:
                u[i] = min(u[i], x - cost)

for i in range(n + 1):
    if u[-1 - i] < INF:
        print(u[-1 - i])
        exit()
