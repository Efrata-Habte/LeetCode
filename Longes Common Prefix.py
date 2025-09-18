class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]

        common=""
        i=0

        while i<len(strs[0]) and i<len(strs[1]):
            if (strs[0][i]==strs[1][i]):
                common+=(strs[0][i])
            else:
                break
            i+=1

        for k in range(2,len(strs)):
            j=0
            ans=""
            while j<len(common) and j<len(strs[k]):
                if (strs[k][j]==common[j]):
                    ans+=(strs[k][j])
                else:
                    break
                j+=1
            common=ans

        return common



