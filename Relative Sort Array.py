class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count=Counter(arr1)
        j=0
        for i in arr2:
            while count[i]>0 and j<len(arr1):
                arr1[j]=i
                j+=1
                count[i]-=1
            del count[i]
        
        s=list(count)
        s.sort()
        for k in s:
            while count[k]>0 and j<len(arr1):
                arr1[j]=k
                j+=1
                count[k]-=1
        return arr1
