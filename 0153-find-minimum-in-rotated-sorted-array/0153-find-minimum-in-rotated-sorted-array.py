class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if nums[0] <= nums[-1]:
            return nums[0]
        
        left, right = 0, len(nums) - 1 
        
        while left <= right:
            mid = left + (right - left)//2
            midval = nums[mid]
            
            if (mid - 1 < 0 or nums[mid-1] > midval) and (mid+1 >= len(nums) or midval < nums[mid+1]):
                return midval
            
            if midval > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
                