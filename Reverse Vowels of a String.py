class Solution:
    def reverseVowels(self, s: str) -> str:
        strs=list(s)
        i,j=0,len(strs)-1
        vowles=['a','e','i','o','u','A',"E",'I','O','U']
        while i<j:
            if (strs[i] in vowles and strs[j] in vowles):
                strs[i],strs[j]=strs[j],strs[i]
                i+=1
                j-=1
            elif strs[i] in vowles:
                j-=1
            else:
                i+=1
        return "".join(strs)
