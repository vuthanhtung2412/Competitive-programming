from typing import List


def carFleet1(target: int, position: List[int], speed: List[int]) -> int:
    # LIFO conditional
    # conditions out:
    # 1.take more time to complete the track
    # 2.start closer to the target

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


def carFleet2(target: int, position: List[int], speed: List[int]) -> int:
    # Only keep track of the car on top of the fleet
    # conditions:
    # 1.take more time to complete the track
    # 2.start closer to the target

    l = [(p, s) for p, s in zip(position, speed)]
    l = sorted(l, key=lambda x: x[0])
    print(l)

    curr = 0
    res = 0
    for i in reversed(range(len(l))):
        if (target - l[i][0]) / l[i][1] > curr:
            curr = (target - l[i][0]) / l[i][1]
            res += 1

    return res


def CarFleet3(target: int, position: List[int], speed: List[int]) -> int:
    # Big O based on the size of target
    l = [-1]*target
    for i in range(len(position)):
        l[position[i]] = i
    curr = 0
    res = 0
    for i in reversed(range(target)):
        tmp = (target - position[l[i]]) / speed[l[i]]
        if l[i] != -1 and tmp > curr:
            curr = tmp
            res += 1

    return res

