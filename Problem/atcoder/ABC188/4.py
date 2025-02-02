import operator

n, C = map(int, input().split())

event = []
for i in range(n):
    a, b, c = map(int, input().split())
    event.append([a, c])
    event.append([b + 1, -c])
#print(event)

event = sorted(event, key = operator.itemgetter(0))
#print(event)

crr = 0
ans = 0
for i in range(len(event) - 1):
    crr += event[i][1]
    #print("crr =" + str(crr))
    if crr <= C:
        ans += (event[i + 1][0] - event[i][0]) * crr
        #print("flag")
    else:
        ans += C * (event[i + 1][0] - event[i][0])
print(ans)
