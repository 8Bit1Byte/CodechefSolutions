t = int(input())
 
while t>0:
    t -= 1
    n = input()
    print(len(n))
    if len(n) <= 4:
        print(n)
    else:
        print(n[0]+str(len(n)-2)+n[-1])