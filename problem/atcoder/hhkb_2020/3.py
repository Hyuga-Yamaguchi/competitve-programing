n = int(input())
p = list(map(int, input().split()))

u = [0] * (210000)
at = 0
for i in range(n):
    u[p[i]] += 1
    while u[at]:
        at += 1
    print(at)
