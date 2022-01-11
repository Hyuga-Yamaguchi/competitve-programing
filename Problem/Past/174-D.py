n = int(input())
c = input()
W_all = c.count("W")
R_all = c.count("R")
W_0 = c[0 : 0].count("W")
R_0 = c[0 : n].count("R")

tmp = n
W = W_0
R = R_0
for i in range(n):
    if c[i] == "W":
        W += 1
        R = R
    elif c[i] == "R":
        W = W
        R -= 1
    print(W, R)
    if tmp >= max([W ,R]):
        tmp = max([W, R])

print(tmp)
