import heapq


class PriorityQueue:
    def __init__(self, heap_type="min"):
        self.heap = []
        self.heap_type = heap_type

    def push(self, value):  # O(logN)
        if self.heap_type == "max":
            heapq.heappush(self.heap, -value)
        else:
            heapq.heappush(self.heap, value)

    def pop(self):  # O(logN)
        if not self.heap:
            return None
        if self.heap_type == "max":
            return -heapq.heappop(self.heap)
        return heapq.heappop(self.heap)

    def top(self):  # O(1)
        if not self.heap:
            return None
        if self.heap_type == "max":
            return -self.heap[0]
        return self.heap[0]

    def size(self):  # O(1)
        return len(self.heap)

    def empty(self):  # O(1)
        return len(self.heap) == 0

    def show(self):  # O(N)
        return list(map(lambda x: -x if self.heap_type == "max" else x, self.heap))


# **デバッグ用の実行例**
print("=== PriorityQueue===")

# **最小ヒープ（Min Heap）**
min_heap = PriorityQueue("min")

print("\n--- Min Heap ---")
print("init:", min_heap.show())

min_heap.push(10)
print("push(10) ->", min_heap.show())

min_heap.push(20)
print("push(20) ->", min_heap.show())

min_heap.push(5)
print("push(5) ->", min_heap.show())

print("top() ->", min_heap.top())
print("size() ->", min_heap.size())

print("pop() ->", min_heap.pop(), ", Heap:", min_heap.show())
print("pop() ->", min_heap.pop(), ", Heap:", min_heap.show())

print("empty() ->", min_heap.empty())
print("pop() ->", min_heap.pop(), ", Heap:", min_heap.show())
print("empty() ->", min_heap.empty())

print("end:", min_heap.show())

# **最大ヒープ（Max Heap）**
max_heap = PriorityQueue("max")

print("\n--- Max Heap ---")
print("init:", max_heap.show())

max_heap.push(10)
print("push(10) ->", max_heap.show())

max_heap.push(20)
print("push(20) ->", max_heap.show())

max_heap.push(5)
print("push(5) ->", max_heap.show())

print("top() ->", max_heap.top())
print("size() ->", max_heap.size())

print("pop() ->", max_heap.pop(), ", Heap:", max_heap.show())
print("pop() ->", max_heap.pop(), ", Heap:", max_heap.show())

print("empty() ->", max_heap.empty())
print("pop() ->", max_heap.pop(), ", Heap:", max_heap.show())
print("empty() ->", max_heap.empty())

print("end:", max_heap.show())
