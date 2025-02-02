n = int(input())

list = []
for i in range(1, n + 1):
    if "7" in str(i) or "7" in str(oct(i)):
        list.append(i)
print(n - len(list))
