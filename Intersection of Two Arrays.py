class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]):
        intersection=set()
        nums2=set(nums2)
        for i in nums1:
            if i in nums2:
                intersection.add(i)
        return list(intersection)

# Fastest approach when we convert both nums to set

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]):
        nums1=set(nums1)
        nums2=set(nums2)
        return list(nums1&nums2)
