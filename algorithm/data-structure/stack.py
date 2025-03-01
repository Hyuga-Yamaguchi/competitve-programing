from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, value):  # O(1)
        self.stack.append(value)

    def pop(self):  # O(1)
        if not self.stack:
            return None
        return self.stack.pop()

    def top(self):  # O(1)
        if not self.stack:
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def empty(self):
        return len(self.stack) == 0

    def show(self):
        return list(self.stack)


stack = Stack()

print("init:", stack.show())

stack.push(10)
print("push(10) ->", stack.show())

stack.push(20)
print("push(20) ->", stack.show())

stack.push(30)
print("push(30) ->", stack.show())

print("top() ->", stack.top())
print("size() ->", stack.size())

print("pop() ->", stack.pop(), ", Stack:", stack.show())
print("pop() ->", stack.pop(), ", Stack:", stack.show())

print("empty() ->", stack.empty())

print("pop() ->", stack.pop(), ", Stack:", stack.show())
print("empty() ->", stack.empty())

print("end:", stack.show())
