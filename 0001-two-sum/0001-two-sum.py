class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = {}
        for index in range(len(nums)):
            comp = target - nums[index]
            if comp in comps:
                return [index, comps[comp]]
            comps[nums[index]] = index
