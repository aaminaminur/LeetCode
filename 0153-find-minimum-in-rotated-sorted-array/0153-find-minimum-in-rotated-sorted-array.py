class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1
        
        while left <= right:
            if nums[left] < nums[right]:
                res = min(nums[left], res)
                break
            
            mid = left + (right - left)//2
            midval = nums[mid]
            res = min(midval, res)
            
            if nums[left] <= midval:
                left = mid + 1
            else:
                right = mid - 1
        return res