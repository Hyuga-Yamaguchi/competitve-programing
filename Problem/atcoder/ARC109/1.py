a, b, x, y = map(int, input().split())

a_lis = [0] * 100
b_lis = [0] * 100
if a <= b:
    for i in range(100):
        if i <= a - 2:
            continue
        if i == a - 1:
            a_lis[i] = 0
            b_lis[i] = x
        else:
            a_lis[i] = min(a_lis[i - 1] + 2 * x, a_lis[i - 1] + y, b_lis[i - 1] + x)
            b_lis[i] = min(a_lis[i - 1] + x + y, b_lis[i - 1] + 2 * x, b_lis[i - 1] + y)
else:
    for i in reversed(range(100)):
        if i >= a:
            continue
        if i == a - 1:
            a_lis[i] = 0
            b_lis[i] = x
        else:
            a_lis[i] = min(a_lis[i + 1] + 2 * x, a_lis[i + 1] + y, b_lis[i + 1] + x + y)
            b_lis[i] = min(a_lis[i + 1] + x, b_lis[i + 1] + 2 * x, b_lis[i + 1] + y)
#print(a_lis, b_lis)
print(b_lis[b - 1] - a_lis[a - 1])
