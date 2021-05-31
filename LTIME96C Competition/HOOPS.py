'''
    Problem Name: Hoop Jump
    Problem Code: HOOPS
    Problem Link: https://www.codechef.com/problems/HOOPS
    Solution Link: https://www.codechef.com/viewsolution/47135989
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


def solve(n):
    print(n//2+1)

if __name__ == '__main__':
    t = inp()
    for _ in range(t):
        n = inp()
        solve(n)