class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val={}

        for i in range(len(nums)):
            needed=target-nums[i]
            if needed in val:
                return [val[needed],i]
            else:
                val[nums[i]]=i
