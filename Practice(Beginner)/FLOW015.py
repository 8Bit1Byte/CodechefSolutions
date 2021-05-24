'''
    Problem Name: Gregorian Calendar
    Problem Code: FLOW015
    Problem Type: https://www.codechef.com/problems/school
    Problem Link: https://www.codechef.com/problems/FLOW015
    Solution Link: https://www.codechef.com/viewsolution/46846520
'''

from sys import stdin, stdout
import datetime


def main(t):
    for _ in range(t):
        stdout.write(f'{datetime.datetime(int(stdin.readline()),1,1).strftime("%A").lower()}'+'\n')

if __name__ == '__main__':
    t = int(stdin.readline())
    main(t)