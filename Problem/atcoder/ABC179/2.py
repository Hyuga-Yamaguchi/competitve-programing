n = int(input())
d = list(list(map(int, input().split())) for _ in range(n))

for i in range(2):
    for j in range(n - 2):
        if d[j][0] == d[j][1] and d[j + 1][0] == d[j + 1][1] and d[j + 2][0] == d[j + 2][1]:
            print("Yes")
            exit()
print("No")
