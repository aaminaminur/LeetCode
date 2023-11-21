class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        curr_low = 10**10
        for val in prices:
            curr_low = min(curr_low, val)
            curr_prof = val - curr_low
            max_prof = max(curr_prof, max_prof)
        return max_prof
