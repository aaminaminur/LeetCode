class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        size = len(nums)
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            j = i+1
            k = size-1
            while j<k:
                cursum = num + nums[j] + nums[k]
                if cursum > 0:
                    k -= 1
                elif cursum < 0:
                    j += 1
                else:
                    res.append([num, nums[j], nums[k]])
                    j += 1
                    while j<k and nums[j] == nums[j-1]:
                        j += 1                    
        return res
