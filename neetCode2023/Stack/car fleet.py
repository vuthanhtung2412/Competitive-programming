from typing import List


def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    # LIFO conditional
    # conditions out:
    # 1.take more time to complete the track
    # 2.start closer to the target
    # 3.Keep track of only the longest time won't work consider the seq of time (1321) there will be 3 fleet
    l = []
    le = len(position)
    for i in range(le):
        l.append((position[i], speed[i]))
    l = sorted(l, key=lambda x: x[0])
    print(l)

    stack = []
    res = 0
    for i in reversed(range(le)):
        while stack and (target - l[stack[-1]][0]) / l[stack[-1]][1] < (target - l[i][0]) / l[i][1]:
            stack.pop()
        if not stack:
            res += 1
        stack.append(i)

    return res



