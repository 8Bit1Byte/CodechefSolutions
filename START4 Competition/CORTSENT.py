'''
    Problem Name: Correct Sentence 
    Problem Code: CORTSENT
    Problem Link: https://www.codechef.com/problems/CORTSENT
    Solution Link: https://www.codechef.com/viewsolution/47064610
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


def checkLanguage(item):
    items = list(item)
    if all([ord(i) <= 109 and ord(i) >= 97 for i in items]):
        return 'lang_1'
    elif all([ord(i) <= 90 and ord(i) >= 78 for i in items]):
        return 'lang_2'
    else:
        return 'lang_none'


def solve(len_, list_):
    dict_ = {
        'lang_1':0,
        'lang_2':0, 
        'lang_none': 0
    }
    for i in range(len_):
        dict_[checkLanguage(list_[i])] += 1
    
    if dict_['lang_1']+dict_['lang_2'] == len_:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    t = inp()
    for _ in range(t):
        l = ls()
        solve(int(l[0]), l[1:])