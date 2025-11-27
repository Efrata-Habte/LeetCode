class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        prefixSum=[0]

        for i in range(n):
            prefixSum.append(prefixSum[i]+nums[i])

        for j in range(1,n+1):
            if prefixSum[j-1]==prefixSum[-1]-prefixSum[j]:
                return j-1
        return -1
        
