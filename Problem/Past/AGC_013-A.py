n = int(input())
a = list(map(int, input().split()))

num = 1
flag = 0

for i in range(n - 1):
    if flag == 0:
        if a[i + 1] < a[i]:
            flag = -1
        elif a[i + 1] > a[i]:
            flag = 1
    elif flag == 1:
        if a[i + 1] < a[i]:
            flag = 0
            num += 1
    else:
        if a[i + 1] > a[i]:
            flag = 0
            num += 1
print(num)
