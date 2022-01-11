#エラトステネスの篩
MAX = 101010
is_prime = [1] * MAX
is_prime[0] = 0; is_prime[1] = 0
for i in range(2, MAX):
    if not is_prime:
        continue
    for j in range(i * 2, MAX, i):
        is_prime[j] = 0

#2017-like数かどうか
a = [0] * MAX
for i in range(MAX):
    if i % 2 == 0:
        continue
    if is_prime[i] == 1 and is_prime[(i + 1) // 2] == 1:
        a[i] = 1

#累積和
s = [0] * (MAX + 1)
for i in range(MAX):
    s[i + 1] = s[i] + a[i]

#処理
q = int(input())
for i in range(q):
    l, r = map(int, input().split())

    print(s[r + 1] - s[l])
