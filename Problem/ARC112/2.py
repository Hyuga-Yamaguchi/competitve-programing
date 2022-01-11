b, c = map(int, input().split())

if c >= 2:
    plus_min = b - c // 2
    plus_max = b + c // 2 - 1
    minus_min = - b - (c + 1) // 2 + 1
    minus_max = - b + (c + 1) // 2 - 1
elif c == 1:
    plus_min = b
    plus_max = b
    minus_min = - b
    minus_max = - b
#print(plus_min, plus_max, minus_min, minus_max)
lis = [plus_min, plus_max, minus_min, minus_max]
lis.sort()

ans = 0
if minus_max < plus_min:
    ans += minus_max - minus_min + 1
    ans += plus_max - plus_min + 1
else:
    ans += max(lis) - min(lis) + 1
print(ans)
