# using set (efficient)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        window=set()
        i=0
        for j in range(len(s)):
            while s[j] in window:
                window.remove(s[i])
                i+=1
            window.add(s[j])
            max_len=max(max_len,len(window))
        return max_len

# using list (less efficient)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window=[]
        i=0
        while i<len(s):
            if s[i] not in window:
                window.append(s[i])
                i+=1
            else:
                break
        max_len=len(window)

        for j in range(i,len(s)):
            while s[j] in window:
                window.pop(0)
            window.append(s[j])
            max_len=max(max_len,len(window))
        return max_len
