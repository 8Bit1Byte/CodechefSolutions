'''
    Problem Name: Sum of Digits
    Problem Code: FLOW006
    Problem Type: https://www.codechef.com/problems/school
    Problem Link: https://www.codechef.com/status/FLOW006
    Solution Link: https://www.codechef.com/viewsolution/46835169
'''

from sys import stdin

def main(t):
    curInx = t
    while curInx:
        n = sum(map(int, list(input())))
        print(n)
        curInx -= 1

if __name__ == '__main__':
    t = int(stdin.readline())
    main(t)