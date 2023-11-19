class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        curr_min = prices[0]
        for i in range(len(prices)):
            curr_min = min(curr_min, prices[i])
            curr_prof = prices[i] - curr_min
            max_prof = max(max_prof, curr_prof)
        return max_prof
        