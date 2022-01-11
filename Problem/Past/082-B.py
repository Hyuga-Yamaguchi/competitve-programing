s = input()
t = input()

s = sorted(s)
t = sorted(t, reverse = True)

ns, nt = "", ""
for i in range(len(s)):
    ns += s[i]
for i in range(len(t)):
    nt += t[i]
#print(ns, nt)

if ns < nt:
    print("Yes")
else:
    print("No")
