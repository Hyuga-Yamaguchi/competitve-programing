lis = []
for i in range(1, 11):
    max_x = int(i ** (1 / 2)) + 1
    min_x = int(i ** (1 / 2))
    if i == 1 or i == 4 or i == 9:
        lis.append([(max_x) ** 2 - i, (min_x - 1) ** 2 - i])
    else:
        lis.append([max_x ** 2 - i, min_x ** 2 - i])
print(lis)

for bit in range(1 << 2):
    for i in range(2):
        cnt = 1
        if (bit >> i) & 1:
            for j in range(len(lis)):
                cnt *= lis[j][0]
        else:
            for j in range(len(lis)):
                cnt *= lis[j][~i]
        print(cnt)
