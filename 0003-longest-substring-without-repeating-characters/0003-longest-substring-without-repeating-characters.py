class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        i, j = 0, 0
        size = len(s)
        chSet = set()
        
        while j<size:
            ch = s[j]
            while ch in chSet and i<=j:
                chSet.remove(s[i])
                i += 1
            count = max(count, j-i+1)
            chSet.add(s[j])
            j += 1
        
        return count