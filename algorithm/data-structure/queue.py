from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, value):  # O(1)
        self.queue.append(value)

    def pop(self):  # O(1)
        if not self.queue:
            return None
        return self.queue.popleft()

    def front(self):  # O(1)
        if not self.queue:
            return None
        return self.queue[0]

    def size(self):  # O(1)
        return len(self.queue)

    def empty(self):  # O(1)
        return len(self.queue) == 0

    def show(self):  # O(N)
        return list(self.queue)


queue = Queue()

print("init:", queue.show())

queue.push(10)
print("push(10) ->", queue.show())

queue.push(20)
print("push(20) ->", queue.show())

queue.push(30)
print("push(30) ->", queue.show())

print("top() ->", queue.front())
print("size() ->", queue.size())

print("pop() ->", queue.pop(), ", queue:", queue.show())
print("pop() ->", queue.pop(), ", queue:", queue.show())

print("empty() ->", queue.empty())

print("pop() ->", queue.pop(), ", queue:", queue.show())
print("empty() ->", queue.empty())

print("end:", queue.show())
