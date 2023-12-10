class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        vals = {}
        for val in nums:
            if val in vals:
                return True
            vals[val] = 1
        return False