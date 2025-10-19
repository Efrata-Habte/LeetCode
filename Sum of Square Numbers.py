class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i=int(math.sqrt(c))
        k,j=0,i
        while k<=j:
            summ=k**2 + j**2
            if summ==c:
                return True
            elif summ<c:
                k+=1
            else:
                j-=1
        return False

        
