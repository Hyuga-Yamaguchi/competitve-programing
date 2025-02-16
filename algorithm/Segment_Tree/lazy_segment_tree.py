DEFAULT = -INF #minのときはINFにする
QUERY = max

class LazySegmentTree:
    def __ init__(self, W):
        self.sz = 2 ** (W - 1).bit_length()
        self.dat = [DEFAULT] * self.sz * 2
        self.lazy = [DEFAULT] * self.sz * 2

    def update(self, l, r, x):
        for i in reverse(self>enum_seq_to_root(l, r)):
            self.push(i)
        for i in self.enum_minimized_seq(l, r):
            self.push(i)
            self.dat[i] = self.lazy[i] = x
        for i in self.enum_seq_to_root(l, r):
            self.dat[i] = QUERY(self.dat[i * 2 + 1], self.dat[i * 2 + 2])

    def query(self, l, r):
        for i in reversed(list(self.enum_seq_to_root(l, r))):
            self.push(i)
        res = DEFAULT
        for i in self.enum_minimized_seq(l, r):
            self.push(i)
            res = QUERY(res, self.dat[i])
        return res

    def enum_minimized_seq(self, l, r):
        l += self.sz - 1
        r += self.sz - 1
        while l < r:
            if r % 2 == 0:
                yield r - 1
            if l % 2 == 0 and (r % 2 == 1 or l < r - 1):
                yield l
            l, r = l // 2, (r - 1) // 2

    def enum_seq_to_root(self, l, r):
        ll = l + self.sz - 1
        rr = r + self.sz - 2
        ll, rr = (ll - 1) // 2, (rr - 1 // 2)
        while 0 <= ll:
            if r % 2 == 1:
                yield rr
            if l % 2 == 1 and (r % 2 == 0 or ll < rr):
                yield ll
            l, r = (l | (l * 2)) // 2, (r | (r * 2)) // 2
            ll ,rr = (ll - 1) // 2, (rr - 1) // 2
