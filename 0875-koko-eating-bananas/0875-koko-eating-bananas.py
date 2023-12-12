class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def ischeck(mid):
            time = 0
            for ban in piles:
                time += math.ceil(ban/mid)
            return time <= h
        
        left, right = 1, max(piles)
        res = right
        while left<=right:
            mid = left + (right - left) // 2
            if ischeck(mid):
                right = mid - 1
                res = min(res, mid)
            else:
                left = mid + 1
        return res