s = input()
n = len(s)

lis = [0] * 26
for i in range(n):
    #print(ord(s[i]))
    lis[ord(s[i]) - 97] += 1
for i in range(26):
    if lis[i] == 0:
        print(chr(i + 97))
        exit()
print("None")
