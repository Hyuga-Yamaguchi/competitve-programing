n = int(input())
a = int(input())

for i in range(a + 1):
    if (n - i) % 500 == 0:
        print("Yes")
        exit(0)
print("No")
