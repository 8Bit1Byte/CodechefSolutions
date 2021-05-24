'''
    Problem Name: Id and Ship 
    Problem Code: FLOW010
    Problem Type: https://www.codechef.com/problems/school
    Problem Link: https://www.codechef.com/problems/FLOW010
    Solution Link: https://www.codechef.com/viewsolution/46835228
'''

from sys import flags, stdin, stdout

def main(t):
    curInx = t
    idName = ['B', 'C', 'D', 'F']
    name = ['BattleShip', 'Cruiser', 'Destroyer', 'Frigate']
    while curInx:
        n = stdin.readline()[0]
        if n not in idName:
            indx = idName.index(str.upper(n))
        else:
            indx = idName.index(n)
        
        stdout.write(f'{name[indx]}'+'\n')
        curInx -= 1

if __name__ == '__main__':
    t = int(stdin.readline())
    main(t)
