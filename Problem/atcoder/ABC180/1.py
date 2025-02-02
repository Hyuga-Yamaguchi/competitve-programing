t = int(input())
for i in range(t):
    x, y, z = map(int, input().split())

    if y + z > x:
        print(0)
    else:
        x1 = ((x - y + 1) ** 2) * ((x - z + 1) ** 2)
        x2 = (y + z - 1) * x
        x3 = (y + z) ** 2
        x4 = 2 * (y + z) + y * z - 1
        print((x1 - (x2 - x3 + x4) ** 2) % (10 ** 9 + 7))
