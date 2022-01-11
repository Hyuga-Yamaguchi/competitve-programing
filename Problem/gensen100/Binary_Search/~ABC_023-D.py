n = int(input())
hs = list(list(map(int, input().split())) for _ in range(n))
h, s = [], []
for i in range(n):
    h.append(hs[i][0]); s.append(hs[i][1])

INF = 10 ** 18
left = 0; right = INF
while right - left > 1:
    mid = left + (right - left) // 2

    flag = True
    t = [0] * n #各風船を割るまでの制限時間
    for i in range(n):
        if mid < h[i]:
            flag = False #そもそも風船の初期位置がその高度を超えていたらダメ
        else:
            t[i] = (mid - h[i]) // s[i]
    t = sorted(t) #制限時間が差し迫っている順にソート
    print(mid, t)
    for i in range(n):
        if t[i] < i:
            flag = False
    if flag:
        right = mid
    else:
        left = mid
print(right)
