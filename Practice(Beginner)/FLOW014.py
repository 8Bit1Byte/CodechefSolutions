'''
    Problem Name: Grade The Steel
    Problem Code: FLOW014
    Problem Type: https://www.codechef.com/problems/school
    Problem Link: https://www.codechef.com/problems/FLOW014
    Solution Link: https://www.codechef.com/viewsolution/46845982
'''


from sys import stdin, stdout

def main(t):
    curInx = t
    while curInx:
        conds = list(map(float, stdin.readline().split()))
        cond_1, cond_2, cond_3 = conds[0]>50, conds[1]<0.7, conds[2]>5600

        if cond_1 and cond_2 and cond_3:
            stdout.write(str(10)+'\n')
        elif cond_1 == True and cond_2 == True:
            stdout.write(str(9)+'\n')
        elif cond_2 == True and cond_3 == True:
            stdout.write(str(8)+'\n')
        elif cond_1 == True and cond_3 == True:
            stdout.write(str(7)+'\n')
        elif cond_1 or cond_2 or cond_3:
            stdout.write(str(6)+'\n')
        else:
            stdout.write(str(5)+'\n')

        curInx -= 1

if __name__ == '__main__':
    t = int(stdin.readline())
    main(t)
