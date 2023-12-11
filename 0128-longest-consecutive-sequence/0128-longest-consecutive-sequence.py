class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxlen = 0
        for num in nums:
            if num-1 not in numset:
                curlen = 0
                while num+curlen in numset:
                    curlen += 1
                maxlen = max(curlen, maxlen)
        return maxlen