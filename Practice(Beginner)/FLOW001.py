'''
    Problem Name: Add Two Numbers
    Problem Code: FLOW001
    Problem Type: https://www.codechef.com/problems/school
    Problem Link: https://www.codechef.com/problems/FLOW001
    Solution Link: https://www.codechef.com/viewsolution/46835083
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