# Brute force approach
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans=[]
        for i,j in enumerate(boxes):
            summ=0
            k=0
            while k<len(boxes):
                if k==i or boxes[k]=='0':
                    k+=1
                    continue
                summ+=abs(i-k)
                k+=1
            ans.append(summ)
        return ans
