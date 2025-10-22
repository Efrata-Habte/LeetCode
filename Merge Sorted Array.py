class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        copy=nums1[:m]
        i,j=0,0
        k=0
        while i<m and j<n:
            if copy[i]<= nums2[j]:
                nums1[k]=copy[i]
                i+=1
            else:
                nums1[k]=nums2[j]
                j+=1
            k+=1
        if i<m:
            for p in range(i,m):
                nums1[k]=copy[i]
                k+=1
        elif j<n:
            for p in range(j,n):
                nums1[k]=nums2[j]
                k+=1
