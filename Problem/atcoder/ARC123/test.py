p = 37
q = 71
e = 79
c = 904
n = p * q
print(n)

for num in range(e):
    if num * (p - 1) * (q - 1) % e == e - 1:
        print(num)
        m = num
        break

d = (m * (p - 1) * (q - 1) + 1) // e
print(d)
M = (c ** d) % n
print(M)
