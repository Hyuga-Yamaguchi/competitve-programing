a, b, c = map(int, input().split())

c_lis = []
for i in range(1, int(c ** (1 / 2) + 1)):
    if c % i == 0:
        c_lis.append(i)
        c_lis.append(c // i)
c_lis = sorted(set(c_lis))
#print(c_lis)
cnt = 0
for i in range(len(c_lis)):
    if a <= c_lis[i] <= b:
        cnt += 1
print(cnt)
