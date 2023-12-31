class Solution:
    def maxPower(self, s: str) -> int:
        power = 0
        slow, fast = 0, 0
        word_size = len(s)
        while fast < word_size:
            ch = s[fast]
            if s[slow] == ch:
                power = max(power, fast-slow+1)
                fast += 1
                continue
            else:
                slow = fast
        return power
