from __future__ import division, print_function

import os
import sys
from io import BytesIO, IOBase
# from collections import defaultdict
# import bisect
MOD = 1000000009
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


def solve(p: list, n: int):
    min_X = {}
    min_Y = {}
    max_X = {}
    max_Y = {}

    for i in p:
        x, y = i

        if y not in min_X:
            min_X[y] = x
            max_X[y] = x

        if x not in min_Y:
            min_Y[x] = y
            max_Y[x] = y

        min_X[y] = min(min_X[y], x)
        max_X[y] = max(max_X[y], x)
        min_Y[x] = min(min_Y[x], y)
        max_Y[x] = max(max_Y[x], y)

    X = [j for j in min_Y]
    Y = [j for j in min_X]

    xlen = len(X)
    ylen = len(Y)

    X.sort()
    Y.sort()

    area = MOD
    pref = list()
    suff = list()

    # Vertical DP
    mn = MOD
    mx = -MOD
    for j in X:
        mn = min(mn, min_Y[j])
        mx = max(mx, max_Y[j])
        pref.append((x - X[0]) * (mx - mn))

    X.reverse()

    mn = MOD
    mx = -MOD
    for j in X:
        mn = min(mn, min_Y[j])
        mx = max(mx, max_Y[j])
        suff.append((X[0] - x) * (mx - mn))

    X.reverse()
    suff.reverse()
    suff.append(0)

    for j in range(xlen):
        area = min(area, pref[j] + suff[j + 1])

    print(area)
    # Horizontal DP
    pref.clear()
    suff.clear()

    mn = MOD
    mx = -MOD
    for j in Y:
        mn = min(mn, min_X[j])
        mx = max(mx, max_X[j])
        pref.append((y- Y[0]) * (mx - mn))

    Y.reverse()

    mn = MOD
    mx = -MOD
    for j in Y:
        mn = min(mn, min_X[j])
        mx = max(mx, max_X[j])
        suff.append((Y[0] - y) * (mx - mn))

    Y.reverse()
    suff.reverse()
    suff.append(0)

    for j in range(ylen):
        area = min(area, pref[j] + suff[j + 1])
    print(area)

    return area


t = int(input())

while t > 0:
    t -= 1

    n = int(input())
    p = list()

    for i in range(n):
        x, y = map(int, input().split())
        p.append([x, y])

    print(solve(p, n))