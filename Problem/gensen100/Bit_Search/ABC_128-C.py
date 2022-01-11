n, m = map(int, input().split())
s = list(list(map(int, input().split())) for _ in range(m))
k = []
for i in range(m):
    k.append(s[i][0])
    s[i].pop(0)
p = list(map(int, input().split()))

ans = 0
for bit in range(1 << n):
    bulb = 0 #点灯している電球の数
    for i in range(m):
        switch = 0 #onしているスイッチの数
        for j in range(k[i]):
            if (bit >> s[i][j] - 1) & 1:
                switch += 1
                #print("bit >> s[i][j] - 1 = " + str(bit & (s[i][j] - 1)))
        #print("switch, i = " + str(switch) + str(i))
        if switch % 2 == p[i]:
            bulb += 1
    #print("cur = " + str(cur))
    if bulb == m:
        ans += 1
print(ans)
