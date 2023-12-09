class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]
        array_length = len(nums)
        for index in range(1, array_length):
            result = nums[index] ^ result
        return result
        