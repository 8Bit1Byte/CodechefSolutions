'''
    Problem Name: Good Number Or Not 
    Problem Code: ISGOODNM
    Problem Link: https://www.codechef.com/problems/ISGOODNM
    Solution Link: https://www.codechef.com/viewsolution/
'''


def print_factors(x):
    l = []
    for i in range(1, x + 1):
        if x % i == 0:
            l.append(i)
    return l

def solve(n):
    l = sum(print_factors(n)[:-1])
    if l == n:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    n = int(input())
    print(solve(n))