'''
    Problem Name: Prime Finding
    Problem Code: PRPRME
    Problem Link: https://www.codechef.com/problems/PRPRME
    Solution Link: https://www.codechef.com/viewsolution/47003813
'''

def primeNum(m):
    from math import sqrt
    if m == 0 or m == 1: # O(1) constant case time (base case)
        return False
    if m == 2 or m == 3: # O(1) constant case time (base case)
        return True
    if m%2 == 0 or m%3 == 0: # O(1)
        return False
    
    for i in range(5, int(sqrt(m))+1):
        if m%i == 0 or m%(i+2) == 0:
            return False
    
    return True

def solve(m):
    i = 0
    j = 1
    while i < m:
        if primeNum(j):
            print(j, end=' ')
            i += 1
        j += 1


if __name__ == '__main__':
    n = int(input())
    solve(n)