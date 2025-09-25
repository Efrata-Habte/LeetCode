class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        summ=0
        piles.sort()
        for i in range (len(piles)-2,len(piles)//3-1,-2):
            summ+=piles[i]

        return summ
