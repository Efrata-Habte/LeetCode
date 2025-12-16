class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        digits=['1','2','3','4','5','6','7','8','9','0']
        for i in s:
            if i in digits:
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
