class Solution:
    def similarPairs(self, words: List[str]) -> int:
        seen=[]

        for w in words:
            seen.append("".join(sorted(set(w))))

        count=0
        for i in range(len(seen)):
            for j in range(i+1,len(seen)):
                if seen[i]==seen[j]:
                    count+=1
        return count
