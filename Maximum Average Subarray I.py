class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ave=0
        summ=0
        for i in range (k):
            summ+=nums[i]
        ave=summ/k

        for j in range(k,len(nums)):
            summ=summ+nums[j]-nums[j-k]
            ave=max(ave,summ/k)

        return ave

        
