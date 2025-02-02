t = int(input())
nab = list(list(map(int, input().split()))for _ in range(t))

e = 10 ** 9 + 7
#print(nab)

for i in range(t):
    n = nab[i][0]
    a = nab[i][1]
    b = nab[i][2]
    if n - a - b >= 0:
        x4 = (n - a - b + 2) * (n - a - b + 1) // 2
    else:
        x4 = 0
    x3 = 2 * x4
    x2 = (n - a + 1) * (n - b + 1) - x3
    x1 = x2 ** 2
    ans = ((n - a + 1) ** 2) * ((n - b + 1) ** 2) - x1
    print(ans % e)
