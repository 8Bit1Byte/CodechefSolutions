'''
    Problem Name: Find middle element
    Problem Code: PECEX1A
    Problem Link: https://www.codechef.com/problems/PECEX1A
    Solution Link: https://www.codechef.com/viewsolution/47002862
'''

def solve(m: list):
    m.sort()
    return m[2]


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        m = list(map(int, input().split()))
        print(solve(m))