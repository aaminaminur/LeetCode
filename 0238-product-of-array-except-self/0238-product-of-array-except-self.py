class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pref = 1
        res.append(pref)
        for i in range(len(nums)-1):
            pref = nums[i]*pref
            res.append(pref)
        
        posf = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * posf
            posf = posf * nums[i]
        
        return res