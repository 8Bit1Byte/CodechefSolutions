'''
    Problem Name: Enormous Input Test
    Problem Code: INTEST
    Problem Link: https://www.codechef.com/problems/INTEST
    Solution Link: https://www.codechef.com/viewsolution/46835003
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