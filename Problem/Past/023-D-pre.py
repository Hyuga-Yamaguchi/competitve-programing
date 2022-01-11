n = int(input())
hs = list(list(map(int, input().split())) for i in range(n))

h = []
s = []
for i in range(n):
    h.append(hs[i][0])
    s.append(hs[i][1])

INF = 10 ** 18

t = [INF] * n
for i in range(n):
    for x in range(1, 200001):
        if x < h[i]:
            pass
        elif t[i] >= (x - h[i]) // s[i]:
            t[i] = (x - h[i]) // s[i]
print(t)
