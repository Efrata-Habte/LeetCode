class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        return x==x[::-1]

# Mathimatical Approach

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        orginal=x
        rem=0

        while x>0:
            digit=x%10
            rem=rem*10+digit
            x=x//10

        return orginal==rem
