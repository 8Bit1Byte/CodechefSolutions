from __future__ import division, print_function

import os
import sys
from io import BytesIO, IOBase
from math import gcd
from itertools import combinations, chain
import numpy as np

BUFSIZE = 8192
MOD = 998244353 

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

def nCr(n, r):
	p = 1
	k = 1

	if (n - r < r):
		r = n - r

	if (r != 0):
		while (r):
			p *= n
			k *= r
			m = gcd(p, k)
			p //= m
			k //= m
			n -= 1
			r -= 1
	else:
		p = 1
	return p

# n, r = map(int, input().split())

# import time

# t1 = time.time()
# x = nCr(n, r)
# t2 = time.time()
# print('--------------------')
# print(t2-t1)
# # print(x == factorial(n)//(factorial(n-r)*factorial(r)))
# print(time.time()-t2)
r = int(input())
k = int(input())
a = list(map(int, input().split()))
p = list(map(int, input().split()))

import time

t1 = time.time()
dc = np.array([ nCr(a[i], r) for i in range(k) if a[i]>=r and p[i] != 0 ])
dc_len = len(dc)
# sch_may = [i for i in range(k) if p[i] != 0 and a[i] >= r]
# sch_may_len = len(sch_may)
# print(dc)
# poss_comb = list(chain(*map(lambda x: combinations(range(k), x), range(2, k+1))))
# print(poss_comb)
case = 0
for i in chain(*map(lambda x: combinations(dc, x), range(2, dc_len+1))):
    case += np.prod(i)%MOD
print(case%MOD)

print(time.time() - t1)