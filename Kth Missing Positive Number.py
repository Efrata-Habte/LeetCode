class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i=0
        p=0
        track=[0]
        ans=0
        if arr[0]>1:
            i+=arr[0]-1
            track.append(i)
            if i>=k:
                while i>k:
                    i-=1
                return track[0]+i
        for j in range(1,len(arr)):
            p=(arr[j]-arr[j-1]-1)
            i+=p
            track.append(i)
            if i>=k:
                while track[-1]>k:
                    track[-1]-=1
                ans=arr[j-1]+(track[-1]-track[len(track)-2])
                return ans                
           
        return arr[-1]+(k-i)
