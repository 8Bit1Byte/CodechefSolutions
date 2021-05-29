'''
    Problem Name: Is Palindrome
    Problem Code: NUMPLIN
    Problem Link: https://www.codechef.com/problems/NUMPLIN
    Solution Link: https://www.codechef.com/viewsolution/47002736
'''

def solve(n):
    if n == n[::-1]:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    n = input()
    print(solve(n))