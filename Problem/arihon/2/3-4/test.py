cnt = 0
for i in range(1, 50):
    for j in range(1, 50):
        for k in range(1, 50):
            if i <= j <= k and i ** 2 + j ** 2 + k ** 2 == 2022:
                print(i, j, k)
                cnt += 1
print(cnt)
