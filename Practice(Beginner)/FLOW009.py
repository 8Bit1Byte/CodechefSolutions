'''
    Problem Name: Total Expenses
    Problem Code: FLOW009
    Problem Type: https://www.codechef.com/problems/school
    Problem Link: https://www.codechef.com/problems/FLOW009
    Solution Link: https://www.codechef.com/viewsolution/46835203
'''

from sys import stdin, stdout

def main(t):
    curInx = t
    while curInx:
        n, k = map(int, stdin.readline().split())
        if n > 1000:
            stdout.write(f'{n*k*90/100}'+'\n')
        else:
            stdout.write(f'{n*k}'+'\n')

        curInx -= 1

if __name__ == '__main__':
    t = int(stdin.readline())
    main(t)