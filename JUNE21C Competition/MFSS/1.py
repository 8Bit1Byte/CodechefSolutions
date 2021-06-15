from collections import Counter
from itertools import combinations

t = int(input())
tim = 0
while t > 0:
    t -= 1
    n = int(input())        
    x = tuple(map(int, input().split()))
    
    y = Counter(x[s:e] for s, e in combinations(range(len(x)+1), 2))

    l1= []
    max = - 1000000009
    for i in y:
        value = sum(i)*y[i]
        if value > max:
            max = value
    print(max)