'''
    Problem Name: Linear pattern
    Problem Code: LINPAT
    Problem Link: https://www.codechef.com/problems/LINPAT
    Solution Link: https://www.codechef.com/viewsolution/47003106
'''

def solve(m, n):
    if m<n:    
        print((m//2+1)*10, (m//2+1)*2, end=' ', sep=' ')
        m += 2
        solve(m, n)
    

if __name__ == '__main__':
    n = int(input())
    solve(0, n)