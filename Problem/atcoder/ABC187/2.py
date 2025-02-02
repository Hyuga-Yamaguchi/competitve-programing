n = int(input())
x, y = [], []
for i in range(n):
    X, Y = map(int, input().split())
    x.append(X); y.append(Y)

cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if abs(x[i] - x[j]) >= abs(y[j] - y[i]):
            cnt += 1
print(cnt)
