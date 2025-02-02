x, k ,d = map(int, input().split())

x = abs(x)
y = k * d
ans = x + d
if(x > y):
    ans = min(ans , x - y)
else:
    mar = x % d
    if (x // d) % 2 == (k % 2):
        ans = min(ans , mar)
    else:
        ans = min(ans , abs(d - mar))
print(ans)
