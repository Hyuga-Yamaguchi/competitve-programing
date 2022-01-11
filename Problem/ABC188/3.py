import copy

n = int(input())
a = list(map(int, input().split()))

b = copy.copy(a)
for j in range(n - 1):
    for i in range(0, len(b) - 1, 2):
        if b[i] > b[i + 1]:
            b[i + 1] = 0
        elif b[i] < b[i + 1]:
            b[i] = 0
    b = [i for i in b if i > 0]
    #print(b)

if b[0] > b[1]:
    print(a.index(b[1]) + 1)
elif b[1] > b[0]:
    print(a.index(b[0]) + 1)
