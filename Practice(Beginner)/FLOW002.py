'''
    Problem Name: Find Remainder
    Problem Code: FLOW002
    Problem Type: https://www.codechef.com/problems/school
    Problem Link: https://www.codechef.com/status/FLOW002
    Solution Link: https://www.codechef.com/viewsolution/46835115
'''

from sys import stdin

def main(t):
    curInx = t
    while curInx:
        a, b = map(int, stdin.readline().split())
        curInx -= 1
        print(a%b)

if __name__ == '__main__':
    t = int(stdin.readline())
    main(t)