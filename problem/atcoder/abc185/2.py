n, m, t = map(int, input().split())
lis = [0]
for i in range(m):
    A, B = map(int, input().split())
    lis.append(A); lis.append(B)
lis.append(t)
#print(lis)

lis2 = []
for i in range(1, len(lis)):
    lis2.append(lis[i] - lis[i - 1])
#print(lis2)
for i in range(len(lis) - 1):
    if i % 2 == 0:
        lis2[i] = -lis2[i]
#print(lis2)
rest = n
for i in range(len(lis2)):
    if rest + lis2[i] <= n:
        rest += lis2[i]
    else:
        rest = n
    #print(rest)
    if rest <= 0:
        print("No")
        exit()
print("Yes")
