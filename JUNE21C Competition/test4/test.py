from __future__ import division, print_function
from operator import sub

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

import numpy as np
import time


def myfunc(i):
    sub1 = nli[:i - 2][::-1]
    sub2 = nli[i:]
    if i == 1:
        return 0
    if np.isin(1, sub1):
        indx1 = np.where(sub1 == 1)[0][0] + 1
    else:
        indx1 = -1
    if np.isin(2, sub2):
        indx2 = np.where(sub2 == 2)[0][0]
    else:
        indx2 = -1
    if indx1 == -1 and indx2 == -1:
        return -1
    elif indx1 == -1:
        return indx2 + 1
    elif indx2 == -1:
        return indx1 + 1
    else:
        return min(indx1, indx2) + 1


vfunc = np.vectorize(myfunc)

t1 = time.time()
t = int(input())
for _ in range(t):
    # n, m = map(int, input().split())
    # nli = np.array(list(map(int, input().split())))
    # mli = np.array(list(map(int, input().split())))
    nli = np.array(np.random.randint(0, 3, 10000))
    mli = np.array(np.random.randint(0, 10000, 10000))    
    final = list(map(myfunc, mli))
    # print(*final)

print(time.time() - t1)
