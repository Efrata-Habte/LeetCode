class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        correct=["()","{}","[]"]

        for i in s:
            if(i=='[' or i=='(' or i=='{'):
                stack.append(i)
            if (i==')'or i=='}' or i==']'):
                if (len(stack)==0):
                    return False
                else:
                    pair=stack.pop(-1)
                    res=pair+i
                    if (res not in correct):
                        return False

        if (len(stack)!=0):
            return False
        return True
                        

                    


        
