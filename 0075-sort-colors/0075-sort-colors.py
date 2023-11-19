class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(pos1, pos2):
            nums[pos1], nums[pos2] = nums[pos2], nums[pos1]

        size = len(nums)
        low = 0
        mid = 0
        high = size - 1
        while mid <= high:
            if nums[mid] == 0:
                swap(low, mid)
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                swap(mid, high)
                high -= 1
