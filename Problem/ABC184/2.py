n, x = map(int, input().split())
s = input()

scr = x
for i in range(n):
    if scr == 0:
        if s[i] == "o":
            scr += 1
    else:
        if s[i] == "o":
            scr += 1
        else:
            scr -= 1
print(scr)
