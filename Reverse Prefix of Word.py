class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word=list(word)
        
        if ch in word:
            index=word.index(ch)
            word[:index+1]=reversed(word[:index+1])
        
        return "".join(word)
