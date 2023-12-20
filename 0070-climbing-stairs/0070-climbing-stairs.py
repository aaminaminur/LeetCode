class Solution:
    def climbStairs(self, n: int) -> int:
        
        def helper(n, dp):
            if n == 0: return 1
            if n < 0: return 0

            if dp[n] != -1:
                return dp[n]
            dp[n-1] = helper(n-1, dp)
            dp[n-2] = helper(n-2, dp)
            
            dp[n] = dp[n-1] + dp[n-2]
            
            return dp[n]
        
        dp = [-1]*(n+1)
        helper(n, dp)
        return dp[n]