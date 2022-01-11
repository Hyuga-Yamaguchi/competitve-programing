n = int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

lis = factorization(n)

print(str(n) + ":", end ="")
for i in range(len(lis) - 1):
    print((" " + str(lis[i][0])) * lis[i][1], end = "")
print(" " + str(lis[len(lis) - 1][0]) * lis[len(lis) - 1][1])
