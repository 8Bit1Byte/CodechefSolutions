'''
    Problem Name: Good Number Or Not 
    Problem Code: ISGOODNM
    Problem Link: https://www.codechef.com/problems/ISGOODNM
    Solution Link: https://www.codechef.com/viewsolution/47005382
'''

def divisors(m):
    from math import sqrt
    l = set()
    for i in range(1, int(sqrt(m)+1)):
        if m%i == 0:
            l.add(i)
            l.add(m//i)
    l = list(l)
    l.sort()
    return l[:-1]

def solve(n):
    l = sum(divisors(n))
    if l == n:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    n = int(input())
    print(solve(n))