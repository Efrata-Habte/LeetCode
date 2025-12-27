# Bubble sort approach
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]<nums[j]:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
# efficient approach
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=Counter(nums)
        print (count)
        n=len(nums)
        j=0
        for i in range (3):
            k=0
            while k<count[i] and j<n:
                nums[j]=i
                j+=1
                k+=1
