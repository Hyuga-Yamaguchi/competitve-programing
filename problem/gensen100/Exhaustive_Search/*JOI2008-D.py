m = int(input())
a = []
for i in range(m):
    A_X, A_Y = map(int, input().split())
    a.append([A_X, A_Y])
n = int(input())
b = []
for i in range(n):
    B_X, B_Y = map(int, input().split())
    b.append([B_X, B_Y])

for i in b:
    dx = i[0] - a[0][0]
    dy = i[1] - a[0][1]
    """リスト内の対象が全て探索用リストに存在するかどうか"""
    """flag = True にして、対象が探索用リストになければflag = Falseにしてbreak"""
    flag = True
    for j in range(1, m):
        if not [a[j][0] + dx, a[j][1] + dy] in b:
            flag = False
            break
    if flag:
        print(dx, dy)
        exit()
