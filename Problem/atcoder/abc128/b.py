n = int(input())
sp = []
for i in range(n):
    S, P = input().split()
    sp.append([S, P, i + 1])
print(sp)
sp.sort()
print(sp)
