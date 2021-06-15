from sys import stdin
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
    dicto = dd(int)
    n = takein()
    l = takeiar()
    stro = str(l[0])
    sumo = l[0]
    ln = 1
    dicto[stro] = sumo
    minsum = sumo
    for i in range(1, n):
        stro += str(l[i])
        print(stro[:-2])
        sumo += l[i]
        ln += 1
        if stro not in dicto or stro[:-1] not in dicto:
            if minsum < sumo * (n - i - ln + 1):
                dicto[stro] = sumo
                if minsum < sumo:
                    ln += 1
            if minsum < l[i] * (n - i):
                stro = str(l[i])
                sumo = l[i]
                dicto[stro] = sumo
                if minsum < l[i]:
                    ln = 1
        else:
            dicto[stro] += sumo

    print(max(dicto.values()))
    print(dicto)


def main():
    global tt
    t = 1
    t = takein()
    for tt in range(1, t + 1):
        solve()
main()