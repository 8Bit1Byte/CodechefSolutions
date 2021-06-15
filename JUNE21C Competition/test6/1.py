from __future__ import division, print_function

import os
import sys
from io import BytesIO, IOBase
sys.setrecursionlimit(10**9)

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



def getFar(node, gr, n):
    ## bfs and get the farthest node
    done = [False]*(n+1)
    fd = -1
    far = None
    qu = [(node, 0)]
    done[node] = True
    while qu:
        nod, dis = qu.pop(0)
        if fd < dis:
            fd = dis
            far = nod
        for cnod in gr[nod]:
            if done[cnod]:
                continue
            done[cnod] = True
            qu.append((cnod, dis+1))
    return far

def fixHeight(nod, par, gr, H):
    isleaf = True
    for cnod in gr[nod]:
        if cnod == par:
            continue
        isleaf = False
        fixHeight(cnod, nod, gr, H)
        H[nod] = max(H[nod], 1 + H[cnod])
    if isleaf:
        H[nod] = 1

def dfs(nod, par, gr, H, li, cur):
    isleaf = True
    mx = 0
    for cnod in gr[nod]:
        if cnod == par:
            continue
        isleaf = False
        mx = max(mx, H[cnod])
    if isleaf:
        li.append(cur)
        return

    c = 0
    for cnod in gr[nod]:
        if cnod == par:
            continue
        if H[cnod] == mx and c == 0:
            dfs(cnod, nod, gr, H, li, cur+1)
            c+=1
        else:
            dfs(cnod, nod, gr, H, li, 1)
def breakIntoLines(nod, par, gr, li, n, cur):
    H = [0]*(n+1)
    fixHeight(nod, par, gr, H)
    dfs(nod, par, gr, H, li, 1)
    
    
def GETSOL(gr, n, k):
    if k==1:
        return 1
    u = getFar(1, gr, n)
    li = []
    breakIntoLines(u, 0, gr, li, n, 1)
    li.sort(reverse = True)
    size = 1
    total = 0
    i = 0
    while total < k:
        size += 1
        total += li[i]
        i+=1
    return size

for case in range(int(input())):
    n, k = map(int, input().split())
    gr = [[] for i in range(n+1)]
    for i in range(n-1):
        u,v = map(int, input().split())
        gr[u].append(v)
        gr[v].append(u)

    chad = GETSOL(gr, n, k)
    print(chad)