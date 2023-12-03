class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        res = 0
        while left <= right:
            mid = left + (right-left) // 2
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                right = mid-1
            else:
                res = mid
                left = mid+1
        return res