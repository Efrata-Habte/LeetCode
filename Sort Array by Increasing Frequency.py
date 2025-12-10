class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        count=Counter(nums)
        count=OrderedDict(sorted(count.items(),key=lambda x:x[1], reverse=True))
        ans=[]

        for i in count:
            while count[i] >0:
                ans.append(i)
                count[i]-=1
        return ans

        
