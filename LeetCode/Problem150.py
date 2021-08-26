from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            #print(stack)
            if not token in ['+', '-', '*', '/']:
                stack.append(token)
            else:
                op2 = int(stack.pop(-1))
                op1 = int(stack.pop(-1))
                if token == '+':
                    stack.append(op1 + op2)
                elif token == '-':
                    stack.append(op1 - op2)
                elif token == '/':
                    stack.append(int(op1 / op2))
                else:
                    stack.append(op1 * op2)
        return stack.pop(0)

ob = Solution()

tokens = ["2","1","+","3","*"]
#print(ob.evalRPN(tokens))

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(ob.evalRPN(tokens))