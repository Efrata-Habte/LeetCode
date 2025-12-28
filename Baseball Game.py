class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        ops=['C',"D",'+']
        for i in operations:
            if i not in ops:
                stack.append(int(i))
            else:
                if stack:
                    n= len(stack)
                    if i=='+':
                        stack.append(stack[-1]+stack[n-2])
                    elif i=='C':
                        stack.pop()
                    else:
                        stack.append(stack[-1]*2)
        return sum(stack)
