x = input()

for i in range(1 << 3):
    start = ["+", "+", "+"]
    for j in range(3):
        if (i >> j) & 1:
            start[j] = "-"
    #print(start, i)
    ans = int(x[0])
    for k in range(3):
        if start[k] == "+":
            ans += int(x[k + 1])
        else:
            ans -= int(x[k + 1])
    #print(ans)
    if ans == 7:
        print(x[0] + str(start[0]) + x[1] + str(start[1]) + x[2] + str(start[2]) + x[3] + "=7")
        break
