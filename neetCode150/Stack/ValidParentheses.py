def isValid(s: str) -> bool:
    # LIFO pop only when match the last element
    opens = {'(', '{', '['}
    closes = {')', '}', ']'}
    stack = []
    for c in s:
        if not stack and c in closes:
            return False
        else:
            if c in opens:
                stack.append(c)
            else:
                if c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False

    return not stack
