class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans={}
        copy=nums.copy()
        for i in range(len(nums)):
            if not nums:
                break
            maxi=max(nums)
            while maxi in nums:
                nums.remove(maxi)
            ans[maxi]=len(nums)

        answer=[]
        for j in copy:
            answer.append(ans[j])

        return answer



        
