import collections

n = int(input())
s = list(input() for _ in range(n))

c1 = collections.Counter(s)

s2 = []
for i in range(n):
    if s[i][0] == "!":
        s2.append(s[i][1:])
    else:
        s2.append(s[i])
c2 = collections.Counter(s2)

inter_key = c1.keys() & c2.keys()
lis = list(inter_key)

for i in range(len(lis)):
    if c2[lis[i]] - c1[lis[i]] >= 1:
        print(lis[i])
        exit()
print("satisfiable")

"""////////////////////////////"""

n = int(input())
s = set(input() for _ in range(n))

for i in s:
    if "!" + i in s:
        print(i)
        exit()
print("satisfiable")
