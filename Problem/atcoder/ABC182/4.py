n = int(input())
a = list(map(int, input().split()))

sum_lis = []
sum_lis.append(a[0])
for i in range(1, n):
    sum_lis.append(sum_lis[i - 1] + a[i])
#print(sum_lis)

cur_lis = []
cur_lis.append(a[0])
for i in range(1, n):
    cur_lis.append(cur_lis[i - 1] + sum_lis[i])
#print(cur_lis)

max_lis = []
max_lis.append(a[0])
for i in range(1, n):
    if max_lis[i - 1] <= sum_lis[i - 1] + a[i]:
        max_lis.append(sum_lis[i - 1] + a[i])
    else:
        max_lis.append(max_lis[i - 1])
#print(max_lis)

if n > 1:
    ans = 0
    for i in range(1, n):
        if ans <= cur_lis[i - 1] + max_lis[i]:
            ans = cur_lis[i - 1] + max_lis[i]
    print(ans)
elif n == 1:
    if a[0] > 0:
        print(a[0])
    else:
        print(0)
