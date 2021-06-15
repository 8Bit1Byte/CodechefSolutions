from __future__ import division, print_function

import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()


if sys.version_info[0] < 3:
    sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

input = lambda: sys.stdin.readline().rstrip("\r\n")

import queue

def minEdgeBFS(edges, u, v, n):
    visited = [0] * n
    distance = [0] * n
    Q = queue.Queue()
    distance[u] = 0
    Q.put(u)
    visited[u] = True
    while (not Q.empty()):
        x = Q.get()
        for i in range(len(edges[x])):
            if (visited[edges[x][i]]):
                continue
            distance[edges[x][i]] = distance[x] + 1
            Q.put(edges[x][i])
            visited[edges[x][i]] = 1
    print(distance, v)
    return distance[v]


def addEdge(edges, u, v):
    edges[u-1].append(v)
    edges[v-1].append(u)

t = int(input())
if __name__ == '__main__':
    n, q = map(int, input().split())
    edges = [[] for _ in range(n)]

    for i in range(n-1):
        e1, e2 = list(map(int, input().split())) 
        addEdge(edges, e1, e2)
    print(edges)
    total = 0
    for i in range(q):
        q1, q2 = map(int, input().split()) 
        # print([min(minEdgeBFS(edges, i, q1, n), minEdgeBFS(edges, i, q2, n), ) for i in range(0, n)])

    print(total)


'''
2
4 2
1 2
2 3
3 4
1 2
3 1
7 1
1 2
1 3
2 4
2 5
3 6
3 7
2 6
'''