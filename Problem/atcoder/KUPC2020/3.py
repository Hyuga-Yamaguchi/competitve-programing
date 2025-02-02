n = int(input())
x = list(list(input().split()) for _ in range(n))

#print(x)

lis = []
for i in range(n):
    for j in range(n - 1):
        string = ""
        for p in range(j, n):
            string += x[i][p]
        lis.append(string)
for j in range(n):
    for i in range(n - 1):
        string_2 = ""
        for p in range(i, n):
            string_2 += x[p][j]
        lis.append(string_2)

#print(lis)

lis_2 = set(lis)
if len(lis_2) == len(lis):
    print("AC")
else:
    print("WA")
