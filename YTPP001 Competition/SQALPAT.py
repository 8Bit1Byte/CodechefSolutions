'''
    Problem Name: Alternative Square Pattern
    Problem Code: SQALPAT
    Problem Link: https://www.codechef.com/problems/SQALPAT
    Solution Link: https://www.codechef.com/viewsolution/47003660
'''

def solve(n):
    j = 0
    for i in range(n):
        if i%2 == 0:
            print(*[i+j for i in range(1, 6)])
        else:
            print(*[i+j for i in range(5, 0, -1)])
        j += 5


if __name__ == '__main__':
    n = int(input())
    solve(n)