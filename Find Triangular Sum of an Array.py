class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums)>1:
            newArr=[]
            for i in range(len(nums)-1):
                newArr.append((nums[i]+nums[i+1])%10)
            nums=newArr
        return nums[0]

# Recursive approach
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        newArr=[(nums[i]+nums[i+1])%10 for i in range(len(nums)-1)]
        return self.triangularSum(newArr)
