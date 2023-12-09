class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        l, r = 0, size-1
        while l <= r:
            mid = l + (r-l)//2
            if (mid-1 < 0 or nums[mid-1] != nums[mid]) and (mid+1 == size or nums[mid+1] != nums[mid]):
                return nums[mid]
            leftsize = mid -1 if nums[mid-1] == nums[mid] else mid
            if leftsize % 2:
                r = mid - 1
            else:
                l = mid + 1