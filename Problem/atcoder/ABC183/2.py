sg = list(map(int, input().split()))

s, g = [], []
for i in range(4):
    if i == 0 or i == 1:
        s.append(sg[i])
    else:
        g.append(sg[i])
#print(s, g)

g[1] = (-1) * g[1]

x = - s[1] * (s[0] - g[0]) / (s[1] - g[1]) + s[0]
print(x)
