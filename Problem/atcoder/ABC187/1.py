a, b = map(int, input().split())

a, b = str(a), str(b)

ansa, ansb = 0, 0
for i in range(3):
    ansa += int(a[i])
    ansb += int(b[i])

print(max(ansa, ansb))
