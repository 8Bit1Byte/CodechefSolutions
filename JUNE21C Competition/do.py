# by exlploorex :

import os.path
from math import gcd, floor, ceil, inf
from collections import *
import sys
mod = 1000000007
INF = float('inf')
def st(): return list(sys.stdin.readline().strip())
def li(): return list(map(int, sys.stdin.readline().split()))
def ls(): return list(sys.stdin.readline().split())
def mp(): return map(int, sys.stdin.readline().split())
def inp(): return int(sys.stdin.readline())
def pr(n): return sys.stdout.write(str(n)+"\n")
def prl(n): return sys.stdout.write(str(n)+" ")

# for standard i/o
if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')


def solve(nli, mli):
    for i in mli:
        sub1 = nli[:i-1]
        sub2 = nli[i:]
        if i == 1:
            prl(0)
            continue
        if '1' in sub1:
            indx1 = sub1[::-1].index('1')
        else:
            indx1 = -1
        if '2' in sub2:
            indx2 = sub2.index('2')
        else:
            indx2 = -1
        if indx1 == -1 and indx2 == -1:
            prl(-1)
        elif indx1 == -1:
            prl(indx2+1)
        elif indx2 == -1:
            prl(indx1+1)
        else:
            prl(min(indx1, indx2)+1)
    pr('')
if __name__ == '__main__':
    t = inp()
    for _ in range(t):
        n, m = mp()
        nli = ''.join(sys.stdin.readline().split())
        mli = li()
        solve(nli, mli)