from collections import Counter
from itertools import combinations, starmap
# import time

t = int(input())
tim = 0
while t > 0:
    t -= 1
    n = int(input())        
    x = tuple(map(int, input().split()))
    # t1 = time.time()
    # y = Counter(x[s:e] for s, e in combinations(range(len(x)+1), 2) if sum(x[s:e]) > 0)
    # y = Counter(map(x.__getitem__, starmap(slice, combinations(range(len(x)+1), 2))))
    
    y = Counter(x[s:e] for s, e in combinations(range(len(x)+1), 2))

    l1= []
    max = - 1000000009
    for i in y:
        value = sum(i)*y[i]
        if value > max:
            max = value
    # print(max)
    print(list(combinations(range(len(x)+1), 2)))
    #     l1.append(sum(i)*y[i])
    # print(max(l1))
    # print(y)
    # tim += time.time() - t1

# print(tim)

'''
{
    (5,): 3, 
    (5, 5): 2, 
    (10,): 1, 
    (10, 8): 1, 
    (10, 8, -20): 1, 
    (10, 8, -20, 5): 1, 
    (10, 8, -20, 5, 5): 1, 
    (10, 8, -20, 5, 5, 5): 1, 
    (8,): 1, 
    (8, -20): 1, 
    (8, -20, 5): 1, 
    (8, -20, 5, 5): 1, 
    (8, -20, 5, 5, 5): 1, 
    (-20,): 1, 
    (-20, 5): 1, 
    (-20, 5, 5): 1, 
    (-20, 5, 5, 5): 1, 
    (5, 5, 5): 1
}

[10, 18, -2, 3, 8, 13, 8, -12, -7, -2, 3, -20, -15, -10, -5, 5, 10, 15]
'''