class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]

        def flip(sub_arr,k):
            sub_arr[:k]= sub_arr[:k][::-1]

        n=len(arr) 
        for i in range(n,1,-1):
            max_idx= arr.index(max(arr[:i]))
            if max_idx!=i-1:
                if max_idx!=0:
                    flip(arr,max_idx+1)
                    ans.append(max_idx+1)
                flip(arr,i)
                ans.append(i)
        return ans
