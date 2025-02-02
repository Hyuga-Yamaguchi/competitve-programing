s = input()

t = s[::-1]

u = ""
for i in range(len(t)):
    if t[i] == "A":
        u[i] += "T"
    elif t[i] == "T":
        u[i] += "A"
    elif t[i] == "C":
        u[i] += "G"
    elif
