'''
    Problem Name: Birthday Gifts
    Problem Code: TWINGFT
    Problem Link: https://www.codechef.com/problems/TWINGFT
    Solution Link: https://www.codechef.com/viewsolution/47155859
'''

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


def solve(n, k, l):
    sort_ = sorted(l)[::-1]
    l1 = 0
    l2 = 0
    for i in range(k*2):
        if i%2 == 0:
            l1 += sort_[i]
        else:
            l2 += sort_[i]
            if i == k*2-1:
                l2 += sort_[i+1]
    print(max(l1, l2))


if __name__ == '__main__':
    t = inp()
    for _ in range(t):
        n, k = mp()
        l = li()
        solve(n, k, l)