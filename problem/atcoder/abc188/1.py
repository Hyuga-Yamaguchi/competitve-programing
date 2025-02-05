x, y = map(int, input().split())

if (x < y and x + 3 > y) or (x > y and x < y + 3):
    print("Yes")
else:
    print("No")
