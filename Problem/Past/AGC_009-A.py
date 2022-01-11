n = int(input())
a, b = [], []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai); b.append(bi);
a, b = a[::-1], b[::-1]
print(a, b)

sum = 0
for i in range(n):
    #前回までの操作回数を足す
    a[i] += sum
    amari = a[i] % b[i]
    d = 0
    if amari != 0:
        d = b[i] - amari
    sum += d
print(sum)
