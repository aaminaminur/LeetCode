class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        for item in intervals:
            if not res or res[-1][1] < item[0]:
                res.append(item)
                continue
            temp = res[-1]
            temp[-1] = max(temp[-1], item[-1])
            res[-1] = temp
        return res