while True:
    h, w = map(int, input().split())
    if (h, w) == (0, 0):
        break
    print("#" * w)
    for i in range(1, h - 1):
        print("#" + str(".") * (w - 2) + "#")
    print("#" * w)
    print("")
