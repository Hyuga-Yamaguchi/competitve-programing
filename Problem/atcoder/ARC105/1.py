a, b ,c ,d = map(int, input().split())
#
# = list(list(map(int, input.split()))for _ in range())
if a == b + c + d or b == a + c + d or c == a + b + d or d == a + b + c:
    print("Yes")
elif a + b == c + d or a + c == b + d or a + d == b + c:
    print("Yes")
else:
    print("No")
