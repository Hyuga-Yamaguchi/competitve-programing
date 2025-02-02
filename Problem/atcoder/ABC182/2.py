n = int(input())
a = list(map(int, input().split()))

lis = [0] * 1001
for i in range(2, 1001):
    for j in range(n):
        if a[j] % i == 0:
            lis[i] += 1

print(lis)
print(lis.index(max(lis)))
