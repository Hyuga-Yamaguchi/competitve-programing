class RollingHash:
    def __init__(self, s, b=31, m=10**9 + 7):
        self.n = len(s)
        self.b = b
        self.m = m
        self.prefix_hash = [0] * (self.n + 1)
        self.power = [1] * (self.n + 1)

        for i in range(self.n):
            self.prefix_hash[i + 1] = (self.prefix_hash[i] * b + ord(s[i])) % m
            self.power[i + 1] = (self.power[i] * b) % m

    def get_hash(self, l, r):
        hash_value = (
            self.prefix_hash[r] - self.prefix_hash[l] * self.power[r - 1]
        ) % self.m
        return hash_value if hash_value >= 0 else hash_value + self.m


s = "Hello world"
rh = RollingHash(s)

print(rh.get_hash(1, 5))
