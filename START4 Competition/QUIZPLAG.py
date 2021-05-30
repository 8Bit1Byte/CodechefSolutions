'''
    Problem Name: Plagiarism 
    Problem Code: QUIZPLAG
    Problem Link: https://www.codechef.com/START4C/problems/QUIZPLAG
    Solution Link: https://www.codechef.com/viewsolution/47048583
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


def solve(dict_):
    l = sorted(dict_)
    x = [i for i in l if dict_[i]>1]
    print(len(x), *x)

if __name__ == '__main__':
    t = inp()
    for _ in range(t):
        n, m, k = mp()
        l = [i for i in li() if i<=n]
        dict_ = Counter(l)
        solve(dict_)