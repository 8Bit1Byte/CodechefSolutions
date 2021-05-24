'''
    Problem Name: Valid Triangles
    Problem Code: FLOW013
    Problem Type: https://www.codechef.com/problems/school
    Problem Link: https://www.codechef.com/problems/FLOW013
    Solution Link: https://www.codechef.com/viewsolution/46844856
'''

from sys import stdin, stdout

def main(t):
    curInx = t
    while curInx:
        ang_sum = sum(map(int, stdin.readline().split()))
        stdout.write(f'{"YES" if ang_sum == 180 else "NO"}'+'\n')

        curInx -= 1

if __name__ == '__main__':
    t = int(stdin.readline())
    main(t)
