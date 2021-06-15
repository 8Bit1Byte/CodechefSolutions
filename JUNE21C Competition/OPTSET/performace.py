from itertools import combinations

n = int(input())

l = [i for i in range(1, n + 1)]
for k in range(1, n+1):
    per_ = list(combinations(l, k))
    l_u = []

    for i in per_:
        res = 0
        for j in i:
            res ^= j
        l_u.append((res, i))

    print(max(l_u)[0], '|', *max(l_u)[-1])


# =======================================================
# def maxXORInRange(L, R):
#     LXR = L ^ R
#     msbPos = 0
#     while (LXR):
#         msbPos += 1
#         LXR >>= 1
#     maxXOR, two = 0, 1

#     while (msbPos):
#         maxXOR += two
#         two <<= 1
#         msbPos -= 1
#     return maxXOR


# L, R = 8, 20
# print(maxXORInRange(L, R))

# from itertools import combinations

# n = int(input())

# l = [i for i in range(1, n + 1)]
# for k in range(1, n+1):
#     per_ = list(combinations(l, k))
#     l_u = []

#     for i in per_:
#         res = 0
#         for j in i:
#             res ^= j
#         l_u.append((res, i))

#     print(max(l_u)[0], '|', *max(l_u)[-1])
