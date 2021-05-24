'''
    Problem Name: Gross Salary
    Problem Code: FLOW011
    Problem Type: https://www.codechef.com/problems/school
    Problem Link: https://www.codechef.com/problems/FLOW011
    Solution Link: https://www.codechef.com/viewsolution/46844575
'''

from sys import stdin, stdout

def main(t):
    curInx = t
    while curInx:
        basSal = int(stdin.readline())
        if basSal < 1500:
            result = basSal*2
        else:
            result = 198*basSal/100 + 500 

        stdout.write(f'{result}'+'\n')
        
        curInx -= 1

if __name__ == '__main__':
    t = int(stdin.readline())
    main(t)
