n = int(input())
a = list(map(int, input().split()))

def func(x):
    ans = 0
    while x % 2 == 0:
        x //= 2
        ans += 1
    return ans
ans = min(map(func, a))
print(ans)
