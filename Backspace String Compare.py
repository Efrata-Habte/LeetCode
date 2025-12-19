# Using two stacks 
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]

        for i in s:
            if i=='#':
                if stack1:
                    stack1.pop()
                continue
            stack1.append(i)

        for j in t:
            if j=='#':
                if stack2:
                    stack2.pop()
                continue
            stack2.append(j)
            
        return "".join(stack1) == "".join(stack2)
        

