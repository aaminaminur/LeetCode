class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        
        res = []
        
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
                continue
            else:
                res[-1][1] = max(interval[1], res[-1][1])
            
        return res
