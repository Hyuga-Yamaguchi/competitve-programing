a, b, c ,d = map(int, input().split())

if a <= b < c <= d or c <= d < a <= b:
    print("No")
else:
    print("Yes")
