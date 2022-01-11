from bisect import bisect_left

a = [1, 3, 5, 2, 4, 6]
n = len(a)

seq = []
for a_i in a:
    pos = bisect_left(seq, a_i)
    print(len(seq), pos)
    if len(seq) <= pos:
        seq.append(a_i)
    else:
        seq[pos] = a_i
    print(seq)
print(seq)
