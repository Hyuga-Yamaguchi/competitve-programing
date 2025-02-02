h, w = map(int, input().split())
in_s = list(input() for _ in range(h))

s = []
for i in range(h):
    s2 = []
    for j in range(w):
        s2.append(in_s[i][j])
    s.append(s2)
#print(s)

#横方向
cnt = 0
for i in range(h):
    for j in range(w - 1):
        if s[i][j] == "." and s[i][j + 1] == ".":
            cnt += 1
#print(cnt)
#縦方向
for i in range(h - 1):
    for j in range(w):
        if s[i][j] == "." and s[i + 1][j] == ".":
            cnt += 1
print(cnt)
