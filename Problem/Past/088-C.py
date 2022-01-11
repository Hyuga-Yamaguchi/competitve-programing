c = list(list(map(int, input().split())) for _ in range(3))

for a1 in range(101):
    for a2 in range(101):
        for a3 in range(101):
            b1 = c[0][0] - a1
            b2 = c[0][1] - a1
            b3 = c[0][2] - a1
            if a2 + b1 == c[1][0] and a2 + b2 == c[1][1] and a2 + b3 == c[1][2]:
                if a3 + b1 == c[2][0] and a3 + b2 == c[2][1] and a3 + b3 == c[2][2]:
                    print("Yes")
                    exit(0)
print("No")
