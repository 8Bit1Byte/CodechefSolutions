'''
    Problem Name: Lazy Chef 
    Problem Code: LAZYCHF
    Problem Link: https://www.codechef.com/problems/LAZYCHF
    Solution Link: https://www.codechef.com/viewsolution/47021775
'''

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


def solve(x, m, d):
    print(min(x*m,x+d))

if __name__ == '__main__':
    t = inp()
    for _ in range(t):
        x,m,d = mp()
        solve(x, m, d)