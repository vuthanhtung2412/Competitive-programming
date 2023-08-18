# Permutation + Backtrack
# backtrack is normally implemented with stack

from typing import List


def generateParenthesis(n: int) -> List[str]:
    res = []
    stack = ["("]
    opens = n - 1
    r = 1

    def backtrack():
        nonlocal opens
        nonlocal r
        if opens == 0:
            for i in range(r):
                stack.append(")")
            res.append("".join(stack))
            for i in range(r):
                stack.pop()
        else:
            stack.append("(")
            opens -= 1
            r += 1
            backtrack()
            stack.pop()
            opens += 1
            r -= 1

            if r > 0:
                stack.append(")")
                r -= 1
                backtrack()
                stack.pop()
                r += 1

    backtrack()
    return res


print(generateParenthesis(3))
