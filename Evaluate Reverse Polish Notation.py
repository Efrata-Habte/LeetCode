class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        op={'+': lambda a,b: a+b,
            '-':lambda a,b: a-b,
            '*':lambda a,b: a*b,
            '/':lambda a,b:int(a/b)}
        for i,j in enumerate(tokens):
            if j not in op:
                stack.append(int(j))
            else:
                b=stack.pop()
                a=stack.pop()
                stack.append(op[j](a,b))
        return stack[0]
