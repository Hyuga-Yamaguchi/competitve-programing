n = int(input())

n = str(n)
ans = 0
for i in range(len(n)):
    ans += int(n[i])

#print(ans)

if ans % 9 == 0:
    print("Yes")
else:
    print("No")
