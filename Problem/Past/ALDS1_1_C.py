n = int(input())
lis = list(int(input()) for _ in range(n))

#引数nが素数かどうかを判定
def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return True

ans = 0
for i in range (n):
    if is_prime(lis[i]):
        ans += 1

print(ans)
