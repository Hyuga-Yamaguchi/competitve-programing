from collections import Counter

s = input()
#下３桁が８の倍数

if len(s) <= 2:
    if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
        print("Yes")
    else:
        print("No")
    exit()

cnt = Counter(s)
#print("cnt = " + str(cnt))

for i in range(112, 1000, 8):
    #print("i = " + str(i) + str(Counter(str(i))))
    if not Counter(str(i)) - cnt:
        print("Yes")
        exit(0)
print("No")
