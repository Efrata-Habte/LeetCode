from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        count=sorted(count.items(), key=lambda x:x[1],reverse=True)
        result=""
        for i,j in count:
            result+=i*j
        return result


# another approach
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        chars = list(s)
        chars.sort(key=lambda x: (-count[x], x))
        return "".join(chars)
