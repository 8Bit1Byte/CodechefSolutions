'''
    Problem Name: Raju and His Trip
    Problem Code: VALTRI
    Problem Link: https://www.codechef.com/YTPP001/problems/VALTRI
    Solution Link: https://www.codechef.com/viewsolution/
'''

def solve(n):
    if n%5 == 0 or n%6 == 0:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    n = int(input())
    print(solve(n))