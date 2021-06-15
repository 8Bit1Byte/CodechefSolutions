def maxXorSum(n, k):
    if k == 1:
        return n
    res = 1
    l = [1]
    while res <= n:
        res <<= 1
        l.append(res)
    print(l)
    # return res - 1


n, k = map(int, input().split())
maxXorSum(n, k)
