import math
n = int(input())

num = int(math.log(1000000000000001, 26))
#print(num)

#余り
y, z = n, n
y_lis = []
#商
for i in range(100):
    if z >= 1:
        y_lis.append(z % 26)
        z = z // 26
    elif z == 0:
            break
#print(y_lis)

for i in range(len(y_lis) - 1):
    if y_lis[i] <= 0:
        y_lis[i] = y_lis[i] + 26
        y_lis[i + 1] -= 1

if y_lis[-1] == 0:
    y_lis.remove(y_lis[-1])
#print(y_lis)

y_lis = list(reversed(y_lis))
ans = ""
for i in range(len(y_lis)):
    y_lis[i] = chr(y_lis[i] + 96)
    ans += y_lis[i]
print(ans)
