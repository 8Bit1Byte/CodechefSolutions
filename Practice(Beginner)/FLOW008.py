'''
    Problem Name: Helping Chef
    Problem Code: FLOW008
    Problem Type: https://www.codechef.com/problems/school
    Problem Link: https://www.codechef.com/problems/FLOW008
    Solution Link: https://www.codechef.com/viewsolution/46835193
'''

from sys import stdin, stdout

def main(t):
    curInx = t
    while curInx:
        n = int(stdin.readline())
        if n < 10:
            stdout.write('Thanks for helping Chef!'+'\n')
        else:
            stdout.write(str(-1)+'\n')
        curInx -= 1

if __name__ == '__main__':
    t = int(stdin.readline())
    main(t)