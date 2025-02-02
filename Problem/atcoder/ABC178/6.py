n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_lis = []
b_lis = []
for i in range(1, n + 1):
    a_lis.append(a.count(i))
    b_lis.append(b.count(i))

for j in range (n):
    if a_lis[j] > sum(b_lis) - b_lis[j]:
        print("No")
        exit()
print("Yes")

new_b = []
for j in range(n):
    b[a_lis[j] : a_lis]
