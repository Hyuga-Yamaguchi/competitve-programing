h, w = map(int, input().split())
s = [[None] * w for _ in range(h)]
for i in range(h):
    S = input()
    for j in range(w):
        s[i][j] = S[j]
#print(s)

cnt = 0
for i in range(h - 1):
    for j in range(w - 1):
        lis = [s[i][j], s[i + 1][j], s[i][j + 1], s[i + 1][j + 1]]
        if lis.count("#") == 3 and lis.count(".") == 1:
            cnt += 1
        if lis.count("#") == 1 and lis.count(".") == 3:
            cnt += 1
print(cnt)
