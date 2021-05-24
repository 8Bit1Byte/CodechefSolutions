'''
    Problem Name: First and Last Digit 
    Problem Code: FLOW004
    Problem Type: https://www.codechef.com/problems/school
    Problem Link: https://www.codechef.com/problems/FLOW004
    Solution Link: https://www.codechef.com/viewsolution/46835130
'''

from sys import stdin

def main(t):
    curInx = t
    while curInx:
        n = stdin.readline()
        curInx -= 1
        print(int(n[0])+int(n[-2]))

if __name__ == '__main__':
    t = int(stdin.readline())
    main(t)