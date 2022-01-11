s = input()
n = len(s) - 1

ans = 0
for bit in range(1 << n):
    sum = 0
    for i in range(n):
        if bit & (1 << i):
            ns = s[:i + 1] + "+" + s[i + 1:]
            print(ns)
    ans += sum
print(ans)
