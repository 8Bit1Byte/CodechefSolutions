'''
    Problem Name: Find Me 
    Problem Code: FINDMELI
    Problem Link: https://www.codechef.com/problems/FINDMELI
    Solution Link: https://www.codechef.com/viewsolution/47002542
'''

def solve(k, l):
    if k in l:
        return 1
    return -1


if __name__ == '__main__':
    n, k = input().split()
    l = list(input().split())
    print(solve(k, l))