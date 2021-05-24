'''
    Problem Name: Smallest Numbers of Notes
    Problem Code: FLOW005
    Problem Type: https://www.codechef.com/problems/school
    Problem Link: https://www.codechef.com/problems/FLOW005
    Solution Link: https://www.codechef.com/viewsolution/46835158
'''

from sys import stdin

def minNum(n):
    notes = [100, 50, 10, 5, 2, 1]
    noNote = 0
    remNote = n
    for i in notes:
        noNote += remNote//i
        remNote = remNote%i

    return noNote

def main(t):
    curInx = t
    while curInx:
        n = int(stdin.readline())
        curInx -= 1
        print(minNum(n))

if __name__ == '__main__':
    t = int(stdin.readline())
    main(t)