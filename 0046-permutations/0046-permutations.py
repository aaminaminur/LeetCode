class Solution:
    def swap(self, nums: List[int], idx1:int , idx2:int)-> None:
        nums[idx1], nums[idx2] = nums[idx2],nums[idx1]
    
    def permuteRec(self, idx: int, nums: List[int], res: List[List[int]]) ->None:
        if idx == len(nums):
            temp = []
            for val in nums:
                temp.append(val)
            res.append(temp)
        
        for i in range(idx, len(nums)):
            self.swap(nums, idx, i)
            self.permuteRec(idx+1, nums, res)
            self.swap(nums, idx, i)
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.permuteRec(0, nums, res)
        return res
