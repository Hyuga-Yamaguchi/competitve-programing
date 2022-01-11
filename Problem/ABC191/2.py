n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
    if a[i] == x:
        a[i] = -1
for i in range(n):
    if a[i] != -1:
        print(str(a[i]) + " ", end = "")
print("")
