class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for val in nums:
            freq[val] = freq.get(val, 0)+1
        sortres = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(sortres[i][0])
        return res