N = int(input())

div = []
for i in range(1, int(N ** 0.5) + 1):
    if N % i == 0:
        div.append([i, N // i])
#print(div)

l = len(div)
flist = []
for i in range(l):
    fx = max([len(str(div[i][0])), len(str(div[i][1]))])
    flist.append(fx)

print(min(flist))
