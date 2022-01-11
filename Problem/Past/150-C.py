import itertools

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))


#print(p, q)

#1,2,3の順列作成
lis = list(itertools.permutations(range(1, n + 1)))

#print(lis)

print(abs(lis.index(p) - lis.index(q)))
