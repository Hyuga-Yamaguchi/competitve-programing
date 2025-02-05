def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n = int(input())
lis = make_divisors(n)

ans = 0
for i in range(len(lis)):
    if lis[i] % 2 == 1:
        ans += 1
print(2 * ans)
