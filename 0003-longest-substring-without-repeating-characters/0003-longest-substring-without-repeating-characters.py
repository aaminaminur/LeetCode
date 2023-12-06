class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        res = 0
        for right in range(len(s)):
            ch = s[right]
            while ch in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(ch)
            cur_len = right - left + 1
            res = max(cur_len, res)
        return res