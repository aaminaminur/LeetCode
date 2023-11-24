class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = None
        count = 0 
        for item in nums:
            if count == 0:
                maj = item
                count += 1
            else:
                if item == maj:
                    count += 1
                else:
                    count -= 1
        return maj