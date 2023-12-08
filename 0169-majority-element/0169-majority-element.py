class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = None
        count = 0
        for elem in nums:
            if count == 0:
                maj = elem
                count += 1
            else:
                if elem == maj:
                    count += 1
                else:
                    count -= 1
        return maj