# by exlploorex :

import os.path
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

t = int(input())

while t>0:
    t -= 1
    n, m = mp()
    a = li()
    b = li()
    max = 1e9
    map_ = dict()

    for i in range(n):
        if i == 0:
            map_[i] = 0
        elif a[i] != 0:
            map_[i] = 0
        else:
            map_[i] = max
    
    right = -1

    for i in range(n):
        if a[i] == 1:
            right = i
        if right != -1:
            if a[i] == 0:
                map_[i] = min(map_[i], i-right)
    
    left = -1

    for i in range(n-1, -1, -1):
        if a[i] == 2:
            left = i
        if left != -1:
            if a[i] == 0:
                map_[i] = min(map_[i], left-i)
    
    for i in range(m):
        j = b[i] - 1
        if map_[j] != max:
            prl(map_[j])
        else:
            prl(-1)
    
    pr('')
