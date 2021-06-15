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

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    nli = list(map(int, input().split()))
    mli = list(map(int, input().split()))
    for i in mli:
        sub1 = nli[:i-2][::-1]
        len_ = len(sub1)
        sub2 = nli[i:]
        s1 = set(sub1)
        s2 = set(sub2)

        if i == 1:
            print(0, end=' ')
            continue
        if 1 in s1:
            indx1 = sub1.index(1)+1
        else:
            indx1 = -1
        if 2 in s2:
            indx2 = sub2.index(2)
        else:
            indx2 = -1
        if indx1 == -1 and indx2 == -1:
            print(-1, end=' ')
        elif indx1 == -1:
            print(indx2+1, end=' ')
        elif indx2 == -1:
            print(indx1+1, end=' ')
        else:
            print(min(indx1, indx2)+1, end=' ')
    print()
