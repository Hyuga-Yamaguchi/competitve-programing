"""逆ポーランド記法の実装"""

s = input()
ls = len(s)

stack = []
lis = []
for i in range(ls):
    stack.append(s[i])
    print(stack)
    if s[i] == "+":
        lis.append(int(stack[-3]) + int(stack[-2]))
        for j in range(3):
            stack.pop()
        stack.append(lis[0])
        lis.pop()
    elif s[i] == "-":
        lis.append(int(stack[-3]) - int(stack[-2]))
        for j in range(3):
            stack.pop()
        stack.append(lis[0])
        lis.pop()
    elif s[i] == "*":
        lis.append(int(stack[-3]) * int(stack[-2]))
        for j in range(3):
            stack.pop()
        stack.append(lis[0])
        lis.pop()
    elif s[i] == "/":
        lis.append(int(stack[-3]) / int(stack[-2]))
        for j in range(3):
            stack.pop()
        stack.append(lis[0])
        lis.pop()

print(stack[0])
