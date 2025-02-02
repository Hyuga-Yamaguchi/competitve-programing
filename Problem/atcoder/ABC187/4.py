n = int(input())
a, b = [], []
for i in range(n):
    A, B = map(int, input().split())
    a.append(A); b.append(B)

c = []; tmp = 0
for i in range(n):
    c.append(2 * a[i] + b[i])
    tmp += a[i]
c = sorted(c, reverse = True)

cnt = 1
for i in range(n):
    if tmp - c[i] >= 0:
        cnt += 1
    tmp -= c[i]
print(cnt)
