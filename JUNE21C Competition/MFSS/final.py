from sys import maxsize, stdin
from collections import defaultdict as dd

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
    dicto = dd(list)
    n = takein()

    l = takeiar()

    for i in range(n):
        stro = ""
        sumo = 0
        for j in range(i, n):
            sumo += l[j]
            stro += str(l[j])
            if stro not in dicto:
                dicto[stro].append(sumo)
                dicto[stro].append(1)
            else:
                dicto[stro][1] += 1

    maxx = - maxsize
    for first, second in dicto.values():
        maxx = max(maxx, int(first)*int(second))

    print(maxx)
    dicto = None


def main():
    global tt
    
    t = 1
    t = takein()
    
    for tt in range(1, t+1):
        solve()

main()