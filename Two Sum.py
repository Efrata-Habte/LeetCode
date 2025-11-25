class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val={}

        for i in range(len(nums)):
            needed=target-nums[i]
            if needed in val:
                return [val[needed],i]
            else:
                val[nums[i]]=i

# O(Nlogn) solution 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2=list(nums)
        nums2.sort()
        n=len(nums)
        l,r=0,n-1
        while l<=r:
            if nums2[l]+nums2[r]>target:
                r-=1
            elif nums2[l]+nums2[r]<target:
                l+=1
            else:
                left=nums.index(nums2[l])
                nums[left]=None
                return [left,nums.index(nums2[r])]
        
