n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

#print(n, a, q, m)

sum_lis = []
for i in range(1 << n):
    sum = 0
    for j in range(n):
        mask = 1 << j
        if i & mask:
            sum += a[j]
    sum_lis.append(sum)
#print(sum_lis)
#print(len(sum_lis))
for i in range(q):
    if m[i] in sum_lis:
        print("yes")
    else:
        print("no")
