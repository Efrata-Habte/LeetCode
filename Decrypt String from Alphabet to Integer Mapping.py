class Solution:
    def freqAlphabets(self, s: str) -> str:
        mapping={str(i):chr(96+i) for i in range(1,10)}
        mapping.update({f"{i}#" : chr(96+i) for i in range(10,27)})

        res=""
        i=len(s)-1

        while i>=0:
            if s[i]=='#':
                num=s[i-2:i+1]
                res=mapping[num]+res
                i-=3

            else:
                res=mapping[s[i]]+res
                i-=1
        return res
                


