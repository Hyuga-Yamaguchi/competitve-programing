num = 0
for i in range(9):
    num += 19 * (10 ** (2 * i))

num2 = 0
for j in range(2007//9):
    num2 += num * (10 ** (j * 18))

print(num, num2)

print((num2 // 9) % 9)
print((num2 // 9) % 11)
