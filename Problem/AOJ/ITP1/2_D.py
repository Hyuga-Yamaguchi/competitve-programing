w, h, x, y, r = map(int, input().split())
if 0 <= x - r and x + r <= w:
    if 0 <= y - r and y + r <= h:
        print("Yes")
        exit()
print("No")
