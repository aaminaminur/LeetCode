class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = nums[0]
        for index in range(1, len(nums)):
            res = res^nums[index]
        return res
