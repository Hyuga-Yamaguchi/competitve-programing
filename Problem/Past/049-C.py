import re
s = input()
d = ["dreamer", "dream", "erase", "eraser"]
#print(s, d)
s = re.sub(d[3], "", s)
s = re.sub(d[2], "", s)
s = re.sub(d[0], "", s)
s = re.sub(d[1], "", s)

print(s)
print("YES") if s == "" else print("NO")
