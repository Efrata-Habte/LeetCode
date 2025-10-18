class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        move,point=0,0
        for move in range(len(nums)):
            if nums[move]!=0:
                nums[point]=nums[move]
                point+=1
        while point<len(nums):
            nums[point]=0
            point+=1
        return nums
