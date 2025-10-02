class Solution:
    def maxArea(self, height: List[int]) -> int:
        length=len(height)
        left=0
        right=length-1
        max_water=0

        while left<right:
            width=right-left
            volume= min(height[left],height[right])*width
            max_water=max(max_water,volume)
            if height[left]>height[right]:
                right-=1
            else:
                left+=1

        return max_water
