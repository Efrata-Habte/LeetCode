class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        mini=float('inf')
        for i,v in enumerate(prices):
            mini=min(mini,v)
            maxp=max(maxp,v-mini)
        return maxp
        
