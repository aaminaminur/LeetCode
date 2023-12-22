class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cur_min = 10**10
        
        for price in prices:
            cur_min = min(price, cur_min)
            cur_prof = price - cur_min
            max_profit = max(max_profit, cur_prof)
            
        return max_profit