'''
    Problem Name: Enormous Input Test
    Problem Code: INTEST
    https://www.codechef.com/problems/INTEST
'''

from sys import stdin

def main(n, k):
    result = 0
    for i in range(n):
        inp = int(stdin.readline())
        if not inp%k:
            result += 1
    
    return result

if __name__ == '__main__':
    n, k = map(int, stdin.readline().split())
    print(main(n, k))