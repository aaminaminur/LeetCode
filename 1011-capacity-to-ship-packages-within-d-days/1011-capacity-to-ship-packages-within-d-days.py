class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(cap):
            D = 1
            weight = 0
            for w in weights:
                weight += w
                if weight > cap:
                    D += 1
                    weight = w
                    if D > days:
                        return False
            return True
        
        low = max(weights)
        high = sum(weights)
        while low<high:
            mid = low + (high-low)//2
            if feasible(mid):
                high = mid
            else:
                low = mid+1
        return low