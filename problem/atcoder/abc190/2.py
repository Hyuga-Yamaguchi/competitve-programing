n ,s, d = map(int, input().split())
x = [None] * n; y = [None] * n
for i in range(n):
    X, Y = map(int, input().split())
    x[i] = X; y[i] = Y

flag = False
for i in range(n):
    if x[i] < s and y[i] > d:
        flag = True
        break
if flag:
    print("Yes")
else:
    print("No")
