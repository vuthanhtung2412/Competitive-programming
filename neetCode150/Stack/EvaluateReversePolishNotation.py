from typing import List


def myEvalRPN(tokens: List[str]) -> int:
    operators = {'+', '-', '*', '/'}
    val = []
    ops = []
    o2v = []
    for c in tokens[::-1]:
        if c in operators:
            ops.append(c)
            o2v.append(2)
        else:
            val.append(int(c))
            if o2v:
                o2v[-1] -= 1
            while o2v and o2v[-1] == 0:
                match ops[-1]:
                    case '+':
                        tmp = val[-1] + val[-2]
                        val.pop()
                        val.pop()
                        val.append(tmp)
                    case '-':
                        tmp = val[-1] - val[-2]
                        val.pop()
                        val.pop()
                        val.append(tmp)
                    case '*':
                        tmp = val[-1] * val[-2]
                        val.pop()
                        val.pop()
                        val.append(tmp)
                    case '/':
                        if (val[-1] > 0) ^ (val[-2] > 0):
                            tmp = -(-val[-1] // val[-2])
                        else:
                            tmp = val[-1] // val[-2]
                        val.pop()
                        val.pop()
                        val.append(tmp)
                o2v.pop()
                ops.pop()
                if o2v:
                    o2v[-1] -= 1

    return val[0]


def NCEvalRPN(tokens: List[str]) -> int:
    # LIFO wait until an operator appear
    stack = []
    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(c))
    return stack[0]


print(myEvalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
print(myEvalRPN(["4", "-2", "/", "2", "-3", "-", "-"]))

# Test XOR
arr = [-132, 6]
a = 0
if arr[-1] > 0 ^ arr[-2] > 0:
    print(0)
    a = -(-arr[-1] // arr[-2])
else:
    print(1)
    a = arr[-1] // arr[-2]

print(a)
print(-132 < 0 ^ 6 < 0)
# ((-132 < 0) ^ 6) < 0
# (1 ^ 1) < 0
print(-132 < 0 < 0)
print(-132 < 0 == 0)
print((-132 < 0) ^ (6 < 0))
