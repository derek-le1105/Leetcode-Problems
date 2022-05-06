class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        if len(s) == 1:
            return False
        
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if len(stack) >= 1:
                    if char == ')':
                        if stack[len(stack)-1] == '(':
                            stack.pop(len(stack)-1)
                        else:
                            return False
                    elif char == '}':
                        if stack[len(stack)-1] == '{':
                            stack.pop(len(stack)-1)
                        else:
                                return False
                    elif char == ']':
                        if stack[len(stack)-1] == '[':
                            stack.pop(len(stack)-1)
                        else:
                            return False
                else:
                    return False
        if len(stack) != 0:
            return False
        else:
            return True