class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, index, l, r):
        if l == r:
            self.tree[index] = arr[l]
            return
        mid = (l + r) // 2
        self.build(arr, 2 * index + 1, l, mid)
        self.build(arr, 2 * index + 2, mid + 1, r)
        self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]

    def push(self, index, l, r):
        if self.lazy[index] != 0:
            self.tree[index] += (r - l + 1) * self.lazy[index]
            if l != r:  # propagate to children
                self.lazy[2 * index + 1] += self.lazy[index]
                self.lazy[2 * index + 2] += self.lazy[index]
            self.lazy[index] = 0

    def range_update(self, ql, qr, val, index=0, l=0, r=None):
        if r is None:
            r = self.n - 1
        self.push(index, l, r)
        if qr < l or ql > r:
            return
        if ql <= l and r <= qr:
            self.lazy[index] += val
            self.push(index, l, r)
            return
        mid = (l + r) // 2
        self.range_update(ql, qr, val, 2 * index + 1, l, mid)
        self.range_update(ql, qr, val, 2 * index + 2, mid + 1, r)
        self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]

    def range_query(self, ql, qr, index=0, l=0, r=None):
        if r is None:
            r = self.n - 1
        self.push(index, l, r)
        if qr < l or ql > r:
            return 0
        if ql <= l and r <= qr:
            return self.tree[index]
        mid = (l + r) // 2
        left = self.range_query(ql, qr, 2 * index + 1, l, mid)
        right = self.range_query(ql, qr, 2 * index + 2, mid + 1, r)
        return left + right
