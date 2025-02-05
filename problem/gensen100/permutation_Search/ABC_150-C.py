import itertools

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

lis = list(itertools.permutations(range(1, n + 1)))
#print(lis)

for i in range(len(lis)):
    if p == list(lis[i]):
        a = i
    if q == list(lis[i]):
        b = i
print(abs(a - b))
