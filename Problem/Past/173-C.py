h, w, k = map(int, input().split())

#print(c)
#行を全て塗る
for i in range(1 << h):
    c = list(list(input()) for _ in range(h))
    for j in range(h):
        if (i >> j) & 1:
            for k in range(w):
                c[j][k] = "-"
    print(c, i, j)
