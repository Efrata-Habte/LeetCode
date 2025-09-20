class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter

        if len(words)==1:
            return list(words[0])

        common=Counter(words[0])

        for i in range(1,len(words)):
            ans={}
            count=Counter(words[i])
            for k in count:
                if k in common:
                    ans[k]=min(count[k],common[k])

            common=ans
        final=[]
        for m in common:
            for n in range(common[m]):
                final.append(m)
        return final
        

        
