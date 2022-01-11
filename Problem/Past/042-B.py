n, l = map(int, input().split())
s = list(input() for _ in range(n))

s = sorted(s)
ans = ""
for i in range(len(s)):
    ans += s[i]
print(ans)
