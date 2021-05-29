'''
    Problem Name: Reverse Me
    Problem Code: REVMEE
    Problem Link: https://www.codechef.com/problems/REVMEE
    Solution Link: https://www.codechef.com/viewsolution/47002405
'''

def solve(n):
    return n[::-1]


if __name__ == '__main__':
    n = input()
    l = list(input().split())
    print(*solve(l))