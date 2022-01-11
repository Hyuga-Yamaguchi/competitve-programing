import itertools as it
import math

n = int(input())
x = list(list(map(int, input().split())) for i in range(n))

print(n, x)

#街の辿る順番を出力
lis = [z for z in range(n)]
permutations_lis = it.permutations(lis)

num_lis = []
for one_case in permutations_lis:
    num2_lis = []
    for num in one_case:
        print(num, end = "")
        for k in range(n):
            num2_lis.append(num2_lis)
    num_lis.append(num2_)
    print("")
print(num_lis)

#距離計算の関数
def length(arr, a):
    l = math.sqrt((arr[a][0] - arr[a + 1][0]) ** 2 + (arr[a][1] - arr[a + 1][1]) ** 2)
    return l

list = []
for j in range(len(num_lis)):
    l_sum = 0
    for i in  range(n):
        l2 = length(x[j], num // ((n - i) ** 10 ))
        l_sum += l2
    list.append(l2)

print(list)
print(sum(list)/len(list))
