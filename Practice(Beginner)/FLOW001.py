'''
    Problem Name: Add Two Numbers
    Problem Code: FLOW001
    https://www.codechef.com/problems/FLOW001
'''

from sys import stdin

def main(n):
    curInx = n
    while curInx:
        a, b = map(int, stdin.readline().split())
        curInx -= 1
        print(a+b)

if __name__ == '__main__':
    n = int(stdin.readline())
    main(n)