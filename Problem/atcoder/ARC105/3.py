n, m = map(int, input().split())
w = list(map(int, input().split()))
lv = list(list(map(int, input().split())) for _ in range(m))

w = sorted(w)

l = []
v = []
for i in range(m):
    l.append(lv[i][0])
    v.append(lv[i][1])

min_v = min(v)
min_w = min(w)
max_w = max(w)
max_l = max(l)

if min_v < max_w:
    print(-1)
else:
    ans = 0
    weight = 0
    zero_rakuda = 0
    #距離が０で良いラクダの最後尾
    for i in range(n):
        if weight <= min_v:
            weight += w[i]
            zero_rakuda = i - 1
            #print(i, weight ,w[i])
        else:
            break
    #print(zero_rakuda)
    #距離がmaxのラクダの最前
    weight2 = w[-1] + w[-2]
    max_rakuda = 0
    for i in range(n - 2):
        if weight2 >= min_v:
            weight2 -= w[-(i + 1)]
            weight2 += w[-(i + 3)]
            max_rakuda = n - i - 1
    #print(max_rakuda)
    mid_length = 0
    for j in range(zero_rakuda, max_rakuda):
        min_length = 0
        for k in range(m):
            if v[k] < w[j] + w[j + 1]:
                min_length = l[k]
                if min_length >= l[k]:
                    min_length = l[k]
        mid_length += min_length
    ans += mid_length + max_l * (n - max_rakuda - 1)

    print(ans)
