n = int(input())

n_lis = []
for i in range(1, int(n ** (1 / 2)) + 1):
    if n % i == 0:
        n_lis.append(i)
        n_lis.append(n // i)
n_lis = sorted(set(n_lis))
#print(n_lis)

if n == sum(n_lis) - n:
    print("Perfect")
elif n < sum(n_lis) - n:
    print("Abundant")
else:
    print("Deficient")
