from itertools import combinations
from sys import maxsize

class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

A = [2, 2, -1, -5, 12, 1]
max = - maxsize

sum_ = list()
sum_.append(A[0])

obj_tree = Node(sum_[0])
result = sum_[0]

for i in range(len(A)-1):
    sum_.append(sum[i-1]+A[i])
    sum_[i] %= M
    int 
