class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        length=len(nums)-1
        for i in range(length):
            if (nums[i]==nums[i+1]):
                nums[i]*=2
                nums[i+1]=0
            else:
                continue

        j=0
        for k in range(len(nums)):
            if nums[k]!=0:
                nums[j]=nums[k]
                j+=1

        while j<len(nums):
            nums[j]=0
            j+=1  

        return nums          

        
