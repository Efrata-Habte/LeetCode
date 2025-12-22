#Brute force algorithm
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i,j in enumerate(nums1):
            next_element=-1
            if j in nums2:
                index=nums2.index(j)
                k=index+1
                while k<len(nums2):
                    if nums2[k]>j:
                        next_element=nums2[k]
                        break
                    k+=1
                ans.append(next_element)
        return ans

# optimized O(n+m) solution
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_element_map={}
        stack=[]

        for num in nums2:
            while stack and stack[-1]<num:
                next_element_map[stack.pop()]=num
            stack.append(num)

        for num in stack:
            next_element_map[num]=-1
        
        return [next_element_map[num] for num in nums1]
