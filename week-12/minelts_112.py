import sys

class PQ(object):

    def __init__(self):
        self.d = {}
        self.N = 0

    def exch(self, i, j):
        self.d[i], self.d[j] = self.d[j], self.d[i]

    def insert(self, e):
        self.N += 1
        self.d[self.N] = e
        self.swim(self.N)

    def swim(self, k):
        while k > 1 and self.d[k] < self.d[k // 2]:
            self.exch(k, k // 2)
            k = k // 2

    def chk(self, n):
        if max(self.d.values()) > n:
            i = 1
            while self.d[i] != max(self.d.values()):
                i += 1
            self.d[i] = n
            self.swim(i)         

    def delMin(self):
        e = self.d[1]
        self.d[1], self.d[len(self.d)] = self.d[len(self.d)], self.d[1]
        del(self.d[self.N])
        self.N -= 1
        self.sink(1)
        return e

    def sink(self, k):
        while 2 * k <= self.N:
            j = 2 * k
            try:
                i = min([j, j + 1], key = self.d.__getitem__)
            except KeyError:
                i = j
            if self.d[k] < self.d[i]:
                break
            self.exch(k, i)
            k = i

    def getMax(self):
        return self.d[1]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self.N

def main():

    M = int(sys.argv[1])
    pq = PQ()
    for line in sys.stdin.readlines():
        n = int(line)
        if pq.size() < M:
            pq.insert(n)
        else:
            pq.chk(n)

    order = []
    for i in range(0, len(pq.d)):
        order.append(pq.delMin())
        i += 1

    for i in range(0, len(order)):
        print(order[len(order) - i - 1])
        i += 1

if __name__ == '__main__':
    main()