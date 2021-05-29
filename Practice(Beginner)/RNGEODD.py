'''
    Problem Name: Range Odd
    Problem Code: RNGEODD
    Problem Link: https://www.codechef.com/problems/RNGEODD
    Solution Link: https://www.codechef.com/viewsolution/47002229
'''

def solve(l, r):
    return [i for i in range(l, r + 1) if i%2 != 0 ]


if __name__ == '__main__':
    l, r = map(int, input().split())
    print(*solve(l, r))
