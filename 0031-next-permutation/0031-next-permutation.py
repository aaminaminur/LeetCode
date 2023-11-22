class Solution:
    
    def reverse(self, nums, idx1, idx2) -> None:
        low = idx1
        high = idx2
        while low < high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1
        
    def swap(self, nums, idx1, idx2):
        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
        
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = -1
        n = len(nums)
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                idx = i
                break
        
        if idx == -1:
            self.reverse(nums, 0, n-1)
            return nums
        
        for i in range(n-1, -1, -1):
            if nums[i] > nums[idx]:
                self.swap(nums, i, idx)
                break
        
        self.reverse(nums, idx+1, n-1)
        return nums
        
        