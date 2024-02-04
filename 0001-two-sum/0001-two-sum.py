class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        comps = {}
        size = len(nums)
        for index in range(size):
            val = nums[index]
            comp = target - val
            if comp in comps.keys():
                return [index, comps[comp]]
            comps[val] = index
