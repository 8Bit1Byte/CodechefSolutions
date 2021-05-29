'''
    Problem Name: HCF and LCM 
    Problem Code: FDGHLM
    Problem Link: https://www.codechef.com/problems/FDGHLM
    Solution Link: https://www.codechef.com/viewsolution/47003480
'''
def gcd(m, n):
    if n == 0:
        return m
    return gcd(n, m%n) 

def lcm(m, n):
    prod = m*n
    return prod//gcd(m, n)


def solve(a, b):
    hcf_ = gcd(a, b)
    print(hcf_, lcm(a, b))


if __name__ == '__main__':
    a, b = map(int, input().split())
    solve(a, b)