'''
    Problem Name: Odd Even Multiple
    Problem Code: EOMUL
    Problem Link: https://www.codechef.com/problems/EOMUL
    Solution Link: https://www.codechef.com/viewsolution/47001786
'''

def solve(n):
    if n%3 != 0:
        return -1
    m = n//3
    if n%2 == 0:
        return 0
    return 1


if __name__ == '__main__':
    n = int(input())
    print(solve(n))