'''
    Problem Name: Minimum Maximum 
    Problem Code: MNMX
    Problem Type: https://www.codechef.com/problems/school
    Problem Link: https://www.codechef.com/problems/MNMX
    Solution Link: https://www.codechef.com/viewsolution/46854288
'''


from sys import stdin

def main(t):
    for _ in range(t):
        n = stdin.readline()
        l = list(map(int, stdin.readline().split()))
        print((len(l)-1)*min(l))

if __name__ == '__main__':
    t = int(stdin.readline())
    main(t)