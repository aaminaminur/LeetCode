class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ss = sorted(s)
        st = sorted(t)
        for index in range(len(ss)):
            if ss[index] != st[index]:
                return False
        return True