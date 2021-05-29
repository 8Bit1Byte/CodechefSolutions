'''
    Problem Name: Prime Validation
    Problem Code: PRCHECK
    Problem Link: https://www.codechef.com/problems/PRCHECK
    Solution Link: https://www.codechef.com/viewsolution/47003223
'''
def primeNum(m):
    from math import sqrt
    if m == 0 or m == 1: 
        return False
    if m == 2 or m == 3:
        return True
    if m%2 == 0 or m%3 == 0: 
        return False
    
    for i in range(5, int(sqrt(m))+1):
        if m%i == 0 or m%(i+2) == 0:
            return False
    
    return True

def solve(n):
    return 1 if primeNum(n) else 0

if __name__ == '__main__':
    n = int(input())
    print(solve(n))