import numpy as np
import time
import random

# // -------------------TEST-2
arr = np.random.randint(0, 3, 100000)
print(np.isin(1, arr))
np.any(np.isin(1, arr))

if np.isin(1, arr):
    print(10)




# // -------------------TEST-1
# s = ' '.join([str(random.randint(0, 2)) for i in range(100000)])
# t = time.time()
# nli = np.array((np.random.randint(0, 3, 100000)))
# mli = np.array((np.random.randint(0, 3, 100000)))
# t2 = time.time()
# print(t2 - t)

# kli = np.array(list(map(int, s.split())))
# print(time.time() - t2)

# n = np.char.split(input()).reshape((1, ))
# print(n)
# print(n.shape)
# for i in n:
#     print(type(i))
# n = n.astype('i4')
# print(n)