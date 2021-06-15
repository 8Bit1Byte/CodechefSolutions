t = int(input())

while t > 0:
    t -= 1
    n = int(input())        
    l = list(map(int, input().split()))
    l_ = {}
    for i in range(n):
        for j in range(i, n):
            ind_ = tuple(l[i:j+1])
            if ind_ in l_:
                l_[ind_]+=1
            else:
                l_[ind_]=1

    l1= []
    for i in l_:
        l1.append(sum(i)*l_[i])
    print(max(l1))
