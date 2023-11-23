class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        SN = int((n*(n+1))/2)
        S = 0
        for val in nums:
            S+=val
        return SN-S