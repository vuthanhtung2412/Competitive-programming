from typing import List


def BFdailyTemperatures(temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)

    def recur(s: int, e: int):
        if e > s:
            for l in range(s, e):
                r = l + 1
                while r < e:
                    if temperatures[r] > temperatures[l]:
                        res[l] = r - l
                        recur(l + 1, r + 1)
                        break
                    r += 1

    recur(0, len(temperatures))

    return res


def NEdailyTemperatures(temperatures: List[int]) -> List[int]:
    # LIFO with condition (greater temperature)
    # Need to keep track of relevant indices (indices that value smaller to the current val)
    # Waiting till the bigger value appear
    l = len(temperatures)
    stack = [0]
    res = [0] * l

    for i in range(1, l):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            tmp = stack.pop()
            res[tmp] = i - tmp

        stack.append(i)

    return res


print(NEdailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(NEdailyTemperatures([55, 38, 53, 81, 61, 93, 97, 32, 43, 78]))
print(NEdailyTemperatures([34, 80, 80, 34, 34, 80, 80, 80, 80, 34]))  # it check from index 1 and 2 but not the rest
