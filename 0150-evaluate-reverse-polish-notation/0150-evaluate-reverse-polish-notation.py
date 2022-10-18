class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokenStack = []
        for op in tokens:
            if op not in "+-/*":
                tokenStack.append(int(op))
            else:
                op1 = tokenStack.pop(-1)
                op2 = tokenStack.pop(-1)
                if op == "+":
                    tokenStack.append(op1 + op2)
                elif op == "-":
                    tokenStack.append(op2 - op1)
                elif op == "*":
                    tokenStack.append(op1 * op2)
                elif op == "/":
                    tokenStack.append(int(op2 / op1))
        return tokenStack[-1]