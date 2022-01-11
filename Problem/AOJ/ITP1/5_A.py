while True:
    h, w = map(int, input().split())
    if (h, w) == (0, 0):
        break
    for i in range(h):
        print("#" * w)
    print("")
