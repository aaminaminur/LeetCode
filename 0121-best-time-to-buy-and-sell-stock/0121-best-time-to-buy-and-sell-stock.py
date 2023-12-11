class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        curMin = 10**10
        for price in prices:
            curMin = min(price, curMin)
            curProf = price - curMin
            maxProf = max(maxProf, curProf)
        return maxProf