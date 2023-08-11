from typing import List


def maxProfitFalse(prices: List[int]) -> int:
    # expand the end till it find the larger price
    # contract the start till it finds a smaller price
    # dynamic sliding window
    length = len(prices)
    if length < 2:
        return 0
    l = 0
    r = 1
    res = 0
    if res < prices[r] - prices[l]:
        res = prices[r] - prices[l]
    while r < length - 1:

        tmp = r
        while tmp < length - 1:
            if prices[tmp] > prices[r]:
                print(tmp)
                break
            tmp += 1
        r = tmp

        tmp = l
        while tmp < r:
            if prices[tmp] < prices[l]:
                l = tmp
                if res < prices[r] - prices[l]:
                    print(r)
                    print(l)
                    res = prices[r] - prices[l]
            tmp += 1

    return res

def maxProfitR(prices: List[int]) -> int:
    # keep track of smallest value and update profit with scan from l -> r bc of chronic order of price
    res = 0
    i = 0
    minPrice = 10000
    for i in range(len(prices)):
        if prices[i] < minPrice:
            minPrice = prices[i]
        if res < prices[i] - minPrice:
            res = prices[i] - minPrice

    return res


print(maxProfitR([11, 7, 1, 4, 2])) # i think there will always be bigger ending point
