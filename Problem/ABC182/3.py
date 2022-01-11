from collections import Counter

n = input()
k = len(n)

lis = []
for i in range(k):
    lis.append(int(n[i]) % 3)
#print(lis)

lis2 = [0] * 3
for i in range(len(lis)):
    if lis[i] == 0:
        lis2[0] += 1
    elif lis[i] == 1:
        lis2[1] += 1
    else:
        lis2[2] += 1

#print(lis2)
sum_lis = sum(lis) % 3

if sum_lis == 0:
    print(0)
elif sum_lis == 1:
    if lis2[1] > 1:
        print(1)
    elif lis2[1] == 1 and (lis2[0] != 0 or lis2[2] != 0):
        print(1)
    else:
        if lis2[2] > 2:
            print(2)
        elif lis2[2] == 2 and (lis2[0] != 0 or lis2[1] != 0):
            print(2)
        else:
            print(-1)
else:
    if lis2[2] > 1:
        print(1)
    elif lis2[2] == 1 and (lis2[0] != 0 or lis2[1] != 0):
        print(1)
    else:
        if lis2[1] > 2:
            print(2)
        elif lis2[1] == 2 and (lis2[0] != 0 or lis2[2] != 0):
            print(2)
        else:
            print(-1)
