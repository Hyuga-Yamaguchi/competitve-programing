n = int(input())

l = 10 ** n - ((9 ** n) * 2 - 8 ** n)
print(l % (10 ** 9 + 7))
