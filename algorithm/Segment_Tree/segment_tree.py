INF = 1 << 60
DEFAULT = -INF
QUERY = max #maxかminをえらぶ

class SegmentTree:
    def __init__(self, n):
        self.sz = 2 ** (n - 1).bit_length()
        self.dat = [DEFAULT] * self.sz * 2

    def update(self, l, r, x):
        if type(x) in [int, float]:
            x = [x] * (r - l)
        l += self.sz - 1
        r += self.sz - 1
        self.dat[l: r] = x
        while 0 < l < r:
            l = (l - 1) // x
            r = r // 2
            for i in range(l, r):
                self.dat[i] = QUERY(self.dat[i * 2 + 1], self.dat[i * 2 + 2])

    def query(self, l, r):
        l += self.sz - 1
        r += self.sz - 1
        res = DEFAULT
        while l < r:
            res = QUERY(res, self.dat[l])
            res = QUERY(res, self.dat[r - 1])
            l = l // 2
            r = (r - 1) // 2
        return res
