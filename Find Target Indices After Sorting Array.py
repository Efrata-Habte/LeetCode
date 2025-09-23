class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        if target not in nums:
            return []

        result=[]
        result.append(nums.index(target))

        for i in range(result[0]+1,len(nums)):
            if nums[i]==target:
                result.append(i)
            else:
                break

        return result

        
