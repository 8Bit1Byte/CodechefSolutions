from itertools import combinations
import numpy as np
from sys import maxsize
from sys import maxsize, stdin
from itertools import combinations

def takein():
    return (int(stdin.readline().rstrip('\r\n')))

def takesr():
    return (stdin.readline().rstrip('\r\n'))

def takesar():
    return (list(map(str, stdin.readline().rstrip('\r\n').split())))

def takeiar():
    return (list(map(int, stdin.readline().rstrip('\r\n').split())))

def takeivr():
    return (map(int, stdin.readline().rstrip('\r\n').split()))

def takesvr():
    return (map(str, stdin.readline().rstrip('\r\n').split()))

def solve():
    n, k = takeivr()

    l = [i for i in range(1, n+1)]
    per_ = list(combinations(l, k))

    max_ = - maxsize
    result = 0
    for i in per_:
        k = np.bitwise_xor.reduce(i)
        if k > max_:
            result = i
            max_ = k

    print(*result)

def main():
    global tt
    
    t = 1
    t = takein()
    
    for tt in range(1, t+1):
        solve()

main()