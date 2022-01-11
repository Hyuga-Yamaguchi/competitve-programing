import bisect

n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))

ans = 0
for i in range(n):
    a_kosu = bisect.bisect_left(a, b[i])
    c_kosu = n - bisect.bisect_right(c, b[i])
    #print(a_kosu, c_kosu)
    ans += a_kosu * c_kosu
print(ans)
