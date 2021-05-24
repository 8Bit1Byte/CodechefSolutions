'''
    Problem Name: Chef and SnackDown
    Problem Code: SNCKYEAR
    Problem Type: https://www.codechef.com/problems/school
    Problem Link: https://www.codechef.com/problems/SNCKYEAR
    Solution Link: https://www.codechef.com/viewsolution/46856547
'''

from sys import stdin

def main(t):
    l = [2010, 2015, 2016, 2017, 2019]
    for _ in range(t):
        n = int(stdin.readline())
        print('HOSTED' if n in l else 'NOT HOSTED')

if __name__ == '__main__':
    t = int(stdin.readline())
    main(t)
