'''
    Problem Name: Find Second Largest
    Problem Code: SECLAR
    Problem Link: https://www.codechef.com/problems/SECLAR
    Solution Link: https://www.codechef.com/viewsolution/47002663
'''

def solve(n: list):
    n_ = n
    max_ = max(n_)
    n_.remove(max_)
    return max(n_)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    print(solve([a, b, c]))