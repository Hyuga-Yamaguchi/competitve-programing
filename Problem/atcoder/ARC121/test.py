from bisect import bisect, bisect_left, bisect_right

a = [1, 3, 5, 7, 9, 11]
print(bisect_left(a, 2))
print(bisect_left(a, 3))
print(bisect_left(a, 12))
