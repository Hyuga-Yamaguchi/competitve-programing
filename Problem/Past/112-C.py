n = int(input())
xyh = list(list(map(int, input().split())) for _ in range(n))

for cx in range(0, 101):
    for cy in range(0, 101):
        flag = True

        for x, y, h in xyh:
            if h == 0:
                continue
            else:
                H = h + abs(x - cx) + abs(y - cy)
                break
        for x, y, h in xyh:
            if h != max(H - abs(x - cx) - abs(y - cy), 0):
                flag = False
                break
        if flag:
            print(cx, cy, H)
