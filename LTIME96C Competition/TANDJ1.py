'''
    Problem Name: Tom And Jerry 1
    Problem Code: TANDJ1
    Problem Type: https://www.codechef.com/problems/school
    Problem Link: https://www.codechef.com/problems/TANDJ1
    Solution Link: https://www.codechef.com/viewsolution/47177732
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


def solve(a, b, c, d, k):
    x = abs(a-c)
    y = abs(b-d)
    total = x+y
    if total == K:
        print('YES')
    elif K > total:
        if (total-K)%2 == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')

if __name__ == '__main__':
    t = inp()
    for _ in range(t):
        a,b,c,d,K = mp()
        solve(a, b, c, d, K)