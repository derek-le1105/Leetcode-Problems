class Solution:
    def isValid(self, s: str) -> bool:
        parenStack = []
        if len(s) % 2 != 0:
            return False
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                parenStack.insert(0, s[i])
            else:
                if len(parenStack) >= 1:
                    if (parenStack[0] == '(' and s[i] == ')'):
                        parenStack.pop(0) 
                    elif (parenStack[0] == '[' and s[i] == ']'):
                        parenStack.pop(0)
                    elif (parenStack[0] == '{' and s[i] == '}'):
                        parenStack.pop(0)
                    else:
                        return False
                else:
                    return False
        if len(parenStack) > 0:
            return False
        return True
            