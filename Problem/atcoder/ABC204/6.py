v = 3; d = 4

low = v; high = d
while high - low > 2:
    c1 = (low * 2 + high) // 3
    c2 = (low + high * 2) // 3

    if c1 + d // (c1 + 1) > c2 + d // (c2 + 1):
        low = c1
    else:
        high = c2
print(low, high)
