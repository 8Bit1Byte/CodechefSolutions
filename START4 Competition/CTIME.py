'''
    Problem Name: Cheating Time 
    Problem Code: CTIME
    Problem Link: https://www.codechef.com/problems/CTIME
    Solution Link: https://www.codechef.com/viewsolution/
'''

'''
NOTE : SOLUTION IS PARTIALLY ANSWER OR THIS WILL GIVE YOU HALF NUMBER
'''
def solve(n, k, f):
    l = []
    time_ = 0
    for i in range(n):
        inp = list(map(int, input().split()))
        if len(l) == 0:
            l.append(inp)
            time_ += inp[-1] - inp[0]
        else:
            for x, y in enumerate(l):    
                if inp[0] >= y[0] and inp[-1] <= y[-1]:
                    pass
                elif (inp[0] > y[0] and inp[0] < y[-1]) and inp[-1] > y[-1]:
                    l[x][-1] = inp[-1]
                    time_ += inp[-1] - y[-1]
                elif inp[0] < y[0] and (inp[-1] > y[0] and inp[-1] < y[-1]):
                    l[x][0] = inp[0]
                    time_ += y[0] - inp[0]
                else:
                    l.append(inp)
                    time_ += inp[-1] - inp[0]

    
    if f - time_ >= k:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k, f = map(int, input().split())
        solve(n, k, f)