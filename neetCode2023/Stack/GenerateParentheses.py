# Permutation + Backtrack
# backtrack is normally implemented with stack

from typing import List


def myGenerateParenthesis(n: int) -> List[str]:
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


def NEGenerateParenthesis(n: int) -> List[str]:
    # same but don't use nonlocal variable
    stack = []
    res = []

    def backtrack(openN, closedN):
        if openN == closedN == n:
            res.append("".join(stack))
            return

        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()
        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()

    backtrack(0, 0)
    return res


print(myGenerateParenthesis(3))
