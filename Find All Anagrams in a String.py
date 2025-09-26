class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter 
        target=Counter(p)
        length=len(p)
        count=[]

        init=s[:length]
        if Counter(init)==target:
            count.append(0)
        for i in range(length,len(s)):
            init=s[i-length+1:i+1]
            if target==Counter(init):
                count.append(i-length+1)

        return count


            
