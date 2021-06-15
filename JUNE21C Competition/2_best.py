# by exlploorex :

import os.path
from math import gcd, floor, ceil
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


def solve(D,d,P,Q):
    d1 = D//d
    d2 = D%d
    total = d*(P*d1+Q*((d1)*(d1-1)//2))+ d2*(P+Q*d1) 

    print(total)


if __name__ == '__main__':
    t = inp()
    for _ in range(t):
        D,d,P,Q = mp()
        solve(D,d,P,Q)