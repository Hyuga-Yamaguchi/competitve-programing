n = int(input())
hs = list(list(map(int, input().split())) for i in range(n))

h = []
s = []
for i in range(n):
    h.append(hs[i][0])
    s.append(hs[i][1])

INF = 10 ** 18
#二分探索
left, right = 0, INF
while right - left > 1:
    mid = (left + right) // 2

    #判定
    ok = True
    t = [0] * n #各風船を割るまでの制限時間

    for i in range(n):
        #そもそもmidが初期高度より低かったらfalse
        if mid < h[i]:
            ok = False
        else:
            t[i] = (mid - h[i]) // s[i]
    #時間制限が差し迫っている順にソート
    t = sorted(t)
    #print("t = " + str(t))
    for i in range(n):
        if t[i] < i:
            ok = False #時間切れ発生
    if ok:
        right = mid
    else:
        left = mid
print(right)
