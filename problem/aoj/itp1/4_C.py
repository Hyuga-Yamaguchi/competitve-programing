from decimal import Decimal

while True:
    x = input().split()
    a = int(x[0]); op = x[1]; b = int(x[2])
    #print(a, op, b)
    if op == "?":
        break
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a // b)
