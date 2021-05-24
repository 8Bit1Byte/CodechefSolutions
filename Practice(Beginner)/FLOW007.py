'''
    Problem Name: Reverse The Number 
    Problem Code: FLOW007
    Problem Type: https://www.codechef.com/problems/school
    Problem Link: https://www.codechef.com/problems/FLOW007
    Solution Link: https://www.codechef.com/viewsolution/46835174
'''

from sys import stdin

def main(t):
    curInx = t
    while curInx:
        n = input()
        print(int(n[::-1]))
        curInx -= 1

if __name__ == '__main__':
    t = int(stdin.readline())
    main(t)