def isValid(s):
    stack = []
    for i in s:
        if i == "(" or i == "{" or i == "[":
            stack.append(i)
        if i == ")" or i == "}" or i == "]":
            if len(stack) == 0:
                return False
            if i == ")":
                val = stack.pop()
                if val != "(":
                    return False
            if i == "}":
                val = stack.pop()
                if val != "{":
                    return False
            if i == "]":
                val = stack.pop()
                if val != "[":
                    return False
        if len(stack) != 0:
            return False
        return True


print(isValid(s=")("))
