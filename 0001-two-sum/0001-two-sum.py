class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        comps = {}
        size = len(nums)
        for i in range(size):
            num = nums[i]
            comp = target - num
            if comp in comps:
                return [i, comps[comp]]
            comps[num] = i
