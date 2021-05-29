'''
    Problem Name: Closest Divisor 
    Problem Code: CLODIV
    Problem Link: https://www.codechef.com/problems/CLODIV
    Solution Link: https://www.codechef.com/viewsolution/47003378
'''

def solve(m, n):
    i = 0
    while m >= i:
        i += n
        
    return i - n


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(solve(a, b))
