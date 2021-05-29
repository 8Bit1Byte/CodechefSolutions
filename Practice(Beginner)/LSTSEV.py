'''
    Problem Name: Not Last 
    Problem Code: LSTSEV
    Problem Link: https://www.codechef.com/problems/LSTSEV
    Solution Link: https://www.codechef.com/viewsolution/47001893
'''

def solve(n):
    if n[-2] == '7':
        return 1
    return 0


if __name__ == '__main__':
    n = input()
    print(solve(n))