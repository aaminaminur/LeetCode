class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def swap(index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]
            
        
        size = len(nums)
        low = 0
        mid = 0
        high = size- 1
        while mid <= high:
            if nums[mid] == 0:
                swap(mid, low)
                mid+=1
                low+=1
            elif nums[mid] == 1:
                mid+=1
            else:
                swap(mid, high)
                high -= 1
        