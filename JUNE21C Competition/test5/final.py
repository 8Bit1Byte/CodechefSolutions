from __future__ import division, print_function

import os
import sys
from io import BytesIO, IOBase
from collections import defaultdict
import bisect

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

while t > 0:
    t -= 1
    n = int(input())
    k = n
    line = defaultdict(list)

    while k > 0:
        x, y = map(int, input().split())
        if y in line[x]:
            pass
        else:
            bisect.insort(line[x], y)
        k -= 1


    sum_ = 0
    x_cord = sorted(line)
    len_ = len(x_cord)

    if n == 1:
        print(0)
        continue

    for i, j in enumerate(x_cord):
        if len(line[j]) % 2 == 0:
            pass
        else:
            if i < len_ - 1:
                x1 = x_cord[i - 1]
                x2 = x_cord[i + 1]
                d1 = j - x1
                d2 = x2 - j
                # line_1 = [
                #     d1 * (line[x1][k + 1] - line[x1][k])
                #     for k in range(0,
                #                    len(line[x1]) - 1)
                # ]                    
                line_1 = []
                for k in range(0, len(line[x1]) - 1, 2):
                    line_1.append(d1*(line[x1][k + 1] - line[x1][k]))
                # line_2 = [
                #     d2 * (line[x2][k + 1] - line[x2][k])
                #     for k in range(0,
                #                    len(line[x2]) - 1)
                # ]
                line_2 = []
                for k in range(0, len(line[x2]) - 1, 2):
                    line_2.append(d1*(line[x2][k + 1] - line[x2][k]))
                if line_1 and line_2:
                    sum_ += min(min(line_1), min(line_2))
            else:
                x1 = x_cord[i - 1]
                d1 = j - x1
                line_1 = []
                for k in range(0, len(line[x1]) - 1, 2):
                    line_1.append(d1*(line[x1][k + 1] - line[x1][k]))
                if line_1:
                    sum_ += min(line_1)
    print(sum_)
'''
3
1
100 100
4
1 100
100 100
100 1
1 1
5
1 100
100 100
100 1
1 1
50 50

'''