class UnorderedMap:
    def __init__(self):
        self.data = {}

    def insert(self, key, value):
        self.data[key] = value

    def erase(self, key):
        if key in self.data:
            del self.data[key]

    def find(self, key):
        return self.data.get(key, None)

    def size(self):
        return len(self.data)

    def empty(self):
        return len(self.data) == 0

    def show(self):
        return list(self.data.items())
