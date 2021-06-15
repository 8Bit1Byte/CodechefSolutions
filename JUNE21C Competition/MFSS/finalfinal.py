from sys import maxsize, stdin
from collections import defaultdict as dd
import numpy as np

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
    dicto = dd(lambda : np.array([0, 0]))
    n = takein()

    l = takeiar()

    for i in range(n):
        stro = ""
        sumo = 0
        for j in range(i, n):
            sumo += l[j]
            stro += str(l[j])
            if stro not in dicto:
                dicto[stro][0] = sumo
                dicto[stro][1] = 1
            else:
                dicto[stro][1] += 1
    arr = np.array(list(dicto.values()))
    arr_sum = arr[:,0]*arr[:,1]
    print(np.max(arr_sum))
    dicto = None


def main():
    global tt
    
    t = 1
    t = takein()
    
    for tt in range(1, t+1):
        solve()

main()