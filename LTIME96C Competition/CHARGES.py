'''
    Problem Name: Charges 
    Problem Code: CHARGES
    Problem Link: https://www.codechef.com/problems/CHARGES
    Solution Link: https://www.codechef.com/viewsolution/47278490
'''

def solve(n, k, s, l, gapI):
    gapIFinal = gapI
    for i in l:
        d_i = 0
        if i-1 == 0:
            d_i += 2 if s[0]== s[1] else 1
            if s[0] == 0:
                s[0] = 1
                gapIFinal = gapIFinal - d_i + (1 if d_i == 2 else 2)
            else:
                s[0] = 0
                gapIFinal = gapIFinal - d_i + (1 if d_i == 2 else 2)

        elif i == n:
            d_i += 2 if s[n-1]== s[n-2] else 1
            if s[n-1] == 0:
                s[n-1] = 1
                gapIFinal = gapIFinal - d_i + (1 if d_i == 2 else 2)
            else:
                s[n-1] = 0
                gapIFinal = gapIFinal - d_i + (1 if d_i == 2 else 2)

        else:
            d_i += 2 if s[i-1] == s[i-2] else 1
            d_i += 2 if s[i-1] == s[i] else 1
            if s[i-1] == 0:
                s[i-1] = 1
                m = (3 if d_i == 3 else (2 if d_i == 4 else 4))
                gapIFinal = gapIFinal - d_i + m
            else:
                s[i-1] = 0
                m = (3 if d_i == 3 else (2 if d_i == 4 else 4))
                gapIFinal = gapIFinal - d_i + m

        print(gapIFinal)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = list(map(int, list(input())))
        l = list(map(int, input().split()))
        dis = 0
        for i, j in enumerate(s):
            if i < n-1:                
                if j == s[i+1]:
                    dis += 2
                else:
                    dis += 1
        if k == 1:
            print(0)
        else:
            solve(n, k, s, l, dis)