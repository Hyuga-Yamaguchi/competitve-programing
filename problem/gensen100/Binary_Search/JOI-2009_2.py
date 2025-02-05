import bisect

d = int(input()) #環状線の全長
n = int(input()) #店舗の個数
m = int(input()) #注文数
a = [0]
for i in range(n - 1):
    A = int(input())
    a.append(A)
a.append(d)
a = sorted(a)
b = list(int(input()) for i in range(m)) #注文先の場所
b = sorted(b)

#print(a, b)

ans = 0
for i in range(m):
    tenpo = bisect.bisect_left(a, b[i])
    #print(tenpo)
    ans += min(abs(b[i] - a[tenpo]), abs(b[i] - a[tenpo - 1]))
print(ans)
